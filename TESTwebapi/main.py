from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: Union[str,None] = None
    
@app.post("/items/")
def create_item(item: Item):
    print(f"データを登録します:{item.name},{item.price},{item.description}")
    return item