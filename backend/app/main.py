# Gọi thư viện FastAPI
from fastapi import FastAPI

# Tạo đối tượng app từ class FastAPI
app = FastAPI()

# Tạo decorator cho app.get("/") 
# Khi có người dùng truy cập vào trang chủ (web root), hàm này sẽ chạy
@app.get("/")
def read_root():
    return {"message": "Chao mung ban den voi Ebook2LateX!"}