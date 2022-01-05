from fastapi import FastAPI, File, UploadFile, APIRouter
from typing import List
import os
from typing import Optional
from pydantic import BaseModel,EmailStr
from fastapi.responses import FileResponse, Response
import io
from starlette.responses import StreamingResponse
import uvicorn

app = FastAPI()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR,'Img/')




# @app.post('/Img/{file_name}')
# def predict(file: UploadFile = File(...)):
#     file_bytes = file.file.read()
#     image = Image.open(io.BytesIO(file_bytes))
#     new_image = prepare_image(image)
#     result = predict(image)
#     bytes_image = io.BytesIO()
#     new_image.save(bytes_image, format = 'PNG')
#     return Response(content = bytes_image.getvalue(), headers = result, media_type = "image/png")



@app.get('/Img/{file_name}')
async def post_image(file_name:str):
    return FileResponse(''.join([IMG_DIR,file_name])) 
    

# class Item(BaseModel):
#         pass
# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None