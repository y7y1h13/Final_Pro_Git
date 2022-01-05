#!/usr/bin/env python
# coding: utf-8


import sys
sys.path.insert(0,'/home/bigdata/KoBERT')
import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import gluonnlp as nlp
import numpy as np
from tqdm import tqdm, tqdm_notebook
#kobert
from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model
#transformers
from transformers import AdamW
from transformers.optimization import get_cosine_schedule_with_warmup



#BERT 모델, Vocabulary 불러오기
bertmodel, vocab = get_pytorch_kobert_model()
device = torch.device('cpu')

# 입력 데이터 생성
class BERTDataset(Dataset):
    def __init__(self, dataset, sent_idx, label_idx, bert_tokenizer, max_len,
                 pad, pair):
        transform = nlp.data.BERTSentenceTransform(
            bert_tokenizer, max_seq_length=max_len, pad=pad, pair=pair)

        self.sentences = [transform([i[sent_idx]]) for i in dataset]
        self.labels = [np.int32(i[label_idx]) for i in dataset]

    def __getitem__(self, i):
        return (self.sentences[i] + (self.labels[i], ))

    def __len__(self):
        return (len(self.labels))

#토큰화
tokenizer = get_tokenizer()
tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)

max_len = 100
batch_size = 32
warmup_ratio = 0.2
num_epochs = 15
max_grad_norm = 1
log_interval = 200
learning_rate =  1e-5

# KoBERT 학습 모델
class BERTClassifier(nn.Module):
    def __init__(self,
                 bert,
                 hidden_size = 768,
                 num_classes=7,
                 dr_rate=0.2,
                 params=None):
        super(BERTClassifier, self).__init__()
        self.bert = bert
        self.dr_rate = dr_rate
                 
        self.classifier = nn.Sequential(
            nn.Linear(hidden_size, num_classes)   )         
        if dr_rate:
            self.dropout = nn.Dropout(p=dr_rate)
    
    def gen_attention_mask(self, token_ids, valid_length):
        attention_mask = torch.zeros_like(token_ids)
        for i, v in enumerate(valid_length):
            attention_mask[i][:v] = 1
        return attention_mask.float()

    def forward(self, token_ids, valid_length, segment_ids):
        attention_mask = self.gen_attention_mask(token_ids, valid_length)
        
        _, pooler = self.bert(input_ids = token_ids, token_type_ids = segment_ids.long(), attention_mask = attention_mask.float().to(token_ids.device))
        if self.dr_rate:
            out = self.dropout(pooler)
        return self.classifier(out)

#BERT 모델 불러오기
model = BERTClassifier(bertmodel).to(device)

# label encoder 
from joblib import dump, load
from sklearn.preprocessing import LabelEncoder
le = load('labelEncoder.joblib')

# pretrain된 model 불러오기
statedict = torch.load('final_model_0.56.pt', map_location=device)['state']
statedict['classifier.0.weight'] = statedict['classifier.weight']
statedict['classifier.0.bias'] = statedict['classifier.bias']
del statedict['classifier.weight']
del statedict['classifier.bias']

device = torch.device('cpu')
small_model = BERTClassifier(bertmodel)
small_model.load_state_dict(statedict)
small_model.eval()

class Predict:
    def __init__(self):
        self.predict_sentence = None
        
        
    def predict(self, predict_sentence):
        self.predict_sentence = predict_sentence
        
        data = [predict_sentence, '0']
        dataset_another = [data]

        another_test = BERTDataset(dataset_another, 0, 1, tok, max_len, True, False)
        test_dataloader = torch.utils.data.DataLoader(another_test, batch_size=batch_size, num_workers=4)

        small_model.eval()

        for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_dataloader):
            token_ids = token_ids.long().to(device)
            segment_ids = segment_ids.long().to(device)

            valid_length= valid_length
            label = label.long().to(device)

            out = small_model(token_ids, valid_length, segment_ids)


            test_eval=[]
            for i in out:
                logits=i
                logits = logits.detach().cpu().numpy()

                for i in range(7):
                    if np.argmax(logits) == i:
                        test_eval.append(le.inverse_transform(np.array([i])))

            return list(test_eval[0])[0]
        
        