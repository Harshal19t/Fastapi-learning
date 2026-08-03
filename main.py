from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/blog") #decorate
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    return {"data": {"name":"Hello, World!"}}

@app.get("/unpublished")
def unpublished():
    return {"data": {"name":"Unpublished"}}

@app.get("/blog/{id}") 
def show(id: int):
    return {"data": {"name":"About Us", "id": id}}

@app.get("/blog/{id}/comments")
def comments(id: int, limit: int = 10):
    return {"data": {"name":"Comments", "id": id, "limit": limit}}