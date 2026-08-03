from fastapi import FastAPI

app = FastAPI()

@app.get("/") #decorate
def index():
    return {"data": {"name":"Hello, World!"}}

@app.get("/blog/{id}") 
def about(id: int):
    return {"data": {"name":"About Us", "id": id}}