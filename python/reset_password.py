from app import create_app, db
from app.models import User

app = create_app()

def reset_password():
    with app.app_context():
        username = input('请输入要重置密码的用户名: ')
        user = User.query.filter_by(username=username).first()
        
        if not user:
            print('用户不存在')
            return
        
        new_password = input('请输入新密码: ')
        confirm_password = input('请再次输入新密码: ')
        
        if new_password != confirm_password:
            print('两次输入的密码不一致')
            return
        
        user.set_password(new_password)
        
        try:
            db.session.commit()
            print('密码重置成功')
        except Exception as e:
            db.session.rollback()
            print('密码重置失败:', str(e))

if __name__ == '__main__':
    reset_password() 