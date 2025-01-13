from app import create_app, db
from app.models import User

app = create_app()

def test_user():
    with app.app_context():
        # 测试添加用户
        user = User(
            username='test_user',
            role='user',
            email='test@example.com',
            phone='12345678901',
            department='测试部门'
        )
        user.set_password('test123')
        
        try:
            db.session.add(user)
            db.session.commit()
            print('测试用户创建成功')
            
            # 测试密码验证
            if user.check_password('test123'):
                print('密码验证成功')
            else:
                print('密码验证失败')
                
        except Exception as e:
            db.session.rollback()
            print('测试失败:', str(e))
        finally:
            # 清理测试数据
            User.query.filter_by(username='test_user').delete()
            db.session.commit()

if __name__ == '__main__':
    test_user() 