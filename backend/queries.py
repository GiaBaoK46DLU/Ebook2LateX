from sqlalchemy import func
from app.database import SessionLocal
from app.models import User, Document, FormulaEntry

def thong_ke_tai_lieu():
    print("--- THỐNG KÊ TÀI LIỆU THEO NGƯỜI DÙNG ---")
    db = SessionLocal()
    
    # Dùng hàm func.count() kết hợp outerjoin để đếm, gom nhóm bằng group_by
    results = db.query(User.full_name, func.count(Document.id))\
                .outerjoin(Document)\
                .group_by(User.user_id).all()
                
    for name, count in results:
        print(f"Người dùng: {name} | Đã tải lên: {count} tài liệu")
    db.close()

def tim_kiem_cong_thuc(keyword):
    print(f"\n--- TÌM KIẾM CÔNG THỨC VỚI TỪ KHÓA: '{keyword}' ---")
    db = SessionLocal()
    
    # Dùng .ilike() để tìm kiếm chuỗi không phân biệt hoa thường (tương tự LIKE %keyword% trong SQL)
    results = db.query(FormulaEntry)\
                .filter(FormulaEntry.latex_content.ilike(f"%{keyword}%")).all()
                
    if not results:
        print("Không tìm thấy công thức nào.")
    for formula in results:
        print(f"ID: {formula.id}\nNội dung LaTeX: {formula.latex_content}\n")
    db.close()

if __name__ == "__main__":
    thong_ke_tai_lieu()
    tim_kiem_cong_thuc("sqrt")