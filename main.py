from fastapi import FastAPI

app = FastAPI()

@app.get("/") #decorate
def index():
    return {"data": {"name":"Hello, World!"}}

@app.get("/about") 
def about():
    return {"data": {"name":"About Us"}}