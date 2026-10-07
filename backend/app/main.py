from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def reed_root():
    return {"message": " Hello, 4eBooks tracker API"}
