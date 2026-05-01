import uuid
import random
from faker import Faker
from app.database import SessionLocal
from app.models import User, Document

# Khởi tạo Faker với ngôn ngữ tiếng Việt
fake = Faker('vi_VN')

def seed_fake_data():
    db = SessionLocal()
    print("Bắt đầu tạo 50 người dùng ngẫu nhiên...")
    try:
        for _ in range(50):
            # Tạo User giả
            user = User(
                user_id=uuid.uuid4(),
                username_email=fake.unique.email(),
                password_hash="fake_hashed_pwd",
                full_name=fake.name(),
                role=random.choice(["Viewer", "Editor"])
            )
            db.add(user)
            db.flush() # Lấy user_id tạm thời

            # Mỗi User có ngẫu nhiên từ 2-5 tài liệu
            num_docs = random.randint(2, 5)
            for _ in range(num_docs):
                doc = Document(
                    id=uuid.uuid4(),
                    user_id=user.user_id,
                    file_name=fake.file_name(extension="pdf"),
                    file_path_url=f"/uploads/{fake.file_name(extension='pdf')}",
                    status=random.choice(["Pending", "Completed", "Error"])
                )
                db.add(doc)
                
        db.commit()
        print("Đã tạo thành công 50 người dùng và các tài liệu đi kèm!")
    except Exception as e:
        db.rollback()
        print(f"Lỗi: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_fake_data()