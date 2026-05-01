import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Tải các biến môi trường từ tập tin .env
load_dotenv()

# Lấy chuỗi kết nối từ biến môi trường
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Tạo Engine (Nguồn kết nối chính)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Tạo SessionLocal (Phiên làm việc với database)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Tạo Base class cho các models
Base = declarative_base()