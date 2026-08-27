#basic
from fastapi import FastAPI
app = FastAPI()

from enum import Enum

@app.get("/")
async def read_root():
    return {"message":"Hello World"}

# path parameter
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# order
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

# pre-deined values
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    
    # if model_name is ModelName.alexnet:
    #     return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if ModelName.alexnet == model_name:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}  
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}    