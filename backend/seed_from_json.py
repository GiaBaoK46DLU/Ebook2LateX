import uuid
import json
from app.database import SessionLocal
from app.models import FormulaEntry, Document

def seed_from_json():
    db = SessionLocal()
    try:
        # Lấy một Document ID bất kỳ để gán công thức vào (vì công thức cần thuộc về 1 tài liệu)
        sample_doc = db.query(Document).first()
        if not sample_doc:
            print("Chưa có tài liệu nào trong Database để gán công thức.")
            return

        with open('data.json', 'r', encoding='utf-8') as f:
            formulas_data = json.load(f)
            
        for item in formulas_data:
            new_formula = FormulaEntry(
                id=uuid.uuid4(),
                document_id=sample_doc.id,
                latex_content=item["latex_content"],
                order_index=item["order_index"]
            )
            db.add(new_formula)
            
        db.commit()
        print("Đã nhập dữ liệu công thức từ JSON thành công!")
    except Exception as e:
        db.rollback()
        print(f"Lỗi: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_from_json()