from app import create_app, db
from app.models import User

app = create_app()

def init_admin():
    with app.app_context():
        # 检查是否已存在管理员账号
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            # 创建新的管理员账号，使用明文密码
            admin = User(
                username='admin',
                password='admin123',  # 直接使用明文密码
                role='admin'
            )
            db.session.add(admin)
            try:
                db.session.commit()
                print('管理员账号创建成功！')
                print('用户名: admin')
                print('密码: admin123')
            except Exception as e:
                db.session.rollback()
                print('创建失败:', str(e))
        else:
            # 更新现有管理员账号的密码为明文
            admin.password = 'admin123'
            try:
                db.session.commit()
                print('管理员密码已重置！')
                print('用户名: admin')
                print('密码: admin123')
            except Exception as e:
                db.session.rollback()
                print('密码重置失败:', str(e))

if __name__ == '__main__':
    init_admin() 