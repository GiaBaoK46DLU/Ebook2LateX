from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

# Tải các biến từ file .env
load_dotenv()

# Lấy chuỗi kết nối từ file .env
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Khởi tạo Engine (Động cơ kết nối)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Tạo Session (Phiên làm việc với Database)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class để sau này các bảng (models) kế thừa
Base = declarative_base()

# Dependency để lấy Database Session cho từng Request (Dùng cho API)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()