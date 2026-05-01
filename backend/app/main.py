from fastapi import FastAPI

app = FastAPI(title="Ebook2LateX API")

@app.get("/")
def read_root():
    return {"message": "Backend Ebook2LateX đã chạy thành công!"}