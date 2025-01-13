from app import db
from app.models import User
from werkzeug.security import generate_password_hash

def update_database():
    try:
        # 添加新字段
        db.engine.execute("""
            ALTER TABLE users
            ADD COLUMN IF NOT EXISTS email VARCHAR(120),
            ADD COLUMN IF NOT EXISTS phone VARCHAR(20),
            ADD COLUMN IF NOT EXISTS department VARCHAR(50),
            ADD COLUMN IF NOT EXISTS create_time DATETIME DEFAULT CURRENT_TIMESTAMP,
            ADD COLUMN IF NOT EXISTS last_login DATETIME
        """)
        
        # 更新管理员密码
        admin = User.query.filter_by(username='admin').first()
        if admin:
            admin.set_password('admin123')
            db.session.commit()
            print("数据库更新成功！")
        else:
            print("未找到管理员账号")
            
    except Exception as e:
        print("更新失败:", str(e))
        db.session.rollback()

if __name__ == '__main__':
    update_database() 