from fastapi import FastAPI

app = FastAPI()

@app.get("/") #decorate
def index():
    return {"data": {"name":"Hello, World!"}}

@app.get("/unpublished")
def unpublished():
    return {"data": {"name":"Unpublished"}}

@app.get("/blog/{id}") 
def show(id: int):
    return {"data": {"name":"About Us", "id": id}}

@app.get("/blog/{id}/comments")
def comments(id: int):
    return {"data": {"name":"Comments", "id": id}}