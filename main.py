from fastapi import FastAPI

#This is instantiating FastAPI
app = FastAPI()

#Setting a path operation
@app.get("/")
async def root():
    return {"message": "Hello, World"}