from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get():
    return {"message": "Hello World"}

@app.post("/")
async def post():
    pass

@app.post("/")
async def post():
    pass

@app.post("/")
async def post():
    pass

