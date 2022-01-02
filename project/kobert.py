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



#토큰화
tokenizer = get_tokenizer()
tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)


small_model = torch.load('/content/drive/MyDrive/Colab Notebooks/data/final_model_0.56.pt')

def predict(predict_sentence):

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

            for i in range(58):
                if np.argmax(logits) == i:
                    test_eval.append(le.inverse_transform(np.array([i])))

        print(">> 입력하신 내용에서 " + test_eval[0] + " 느껴집니다.")
        print(list(test_eval[0]))
 

end = 1
while end == 1 :
    sentence = input("하고싶은 말을 입력해주세요 : ") + ' *'
    if sentence == '0' :
        break
    predict(sentence)
    print("\n")

