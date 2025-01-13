from app import create_app, db
from app.models import User

app = create_app()
with app.app_context():
    # 创建一个默认用户
    if not User.query.filter_by(username='admin').first():
        # 直接创建用户，明文存储密码
        user = User(username='admin', password='admin123')
        db.session.add(user)
        db.session.commit()
        print("默认用户创建成功！")
        print("用户名: admin")
        print("密码: admin123") 