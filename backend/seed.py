import uuid
from app.database import SessionLocal
from app.models import User, Document, FormulaEntry

def seed_data():
    db = SessionLocal()
    
    try:
        print("Đang tạo dữ liệu...")

        # 1. Tạo User
        test_user = User(
            user_id=uuid.uuid4(),
            username_email="teo@dalat.edu.vn",
            password_hash="hashed_password_here",
            full_name="Lê Văn Tèo",
            role="Admin"
        )
        db.add(test_user)
        db.flush() # Lưu tạm để lấy ID gán cho Document

        # 2. Tạo Document
        test_doc = Document(
            id=uuid.uuid4(),
            user_id=test_user.user_id,
            file_name="Giao_trinh_Toan_12.pdf",
            file_path_url="/uploads/toan12.pdf",
            status="Completed"
        )
        db.add(test_doc)
        db.flush()

        # 3. Tạo Công thức LaTeX (FormulaEntry)
        formula = FormulaEntry(
            id=uuid.uuid4(),
            document_id=test_doc.id,
            latex_content=r"\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            order_index=1
        )
        db.add(formula)

        # Lưu vĩnh viễn vào Database
        db.commit()
        print("Tạo dữ liệu thành công! Kiểm tra pgAdmin4 để xem kết quả.")

    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
        db.rollback() # Hoàn tác nếu bị lỗi
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()