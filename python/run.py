from app import create_app, db
from app.models import User
from flask import send_file, render_template, request, jsonify
import pandas as pd
import os

app = create_app()
app.app_context().push()

@app.route('/api/users/export', methods=['GET'])
def export_users():
    users = User.query.all()
    
    data = []
    for user in users:
        data.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
        })
    
    df = pd.DataFrame(data)
    export_path = 'temp/users_export.csv'
    os.makedirs('temp', exist_ok=True)
    df.to_csv(export_path, index=False)
    
    return send_file(export_path, as_attachment=True, download_name='users.csv')

@app.route('/api/users/import', methods=['POST'])
def import_users():
    if 'file' not in request.files:
        return jsonify({'error': 'ファイルがアップロードされていません'}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'ファイルが選択されていません'}), 400
        
    if not file.filename.endswith('.csv'):
        return jsonify({'error': 'CSVファイルのみ対応しています'}), 400
    
    try:
        df = pd.read_csv(file)
        for _, row in df.iterrows():
            user = User(
                username=row['username'],
                email=row['email']
            )
            db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'ユーザデータのインポートが完了しました'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'インポート中にエラーが発生しました: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='10.73.219.95', port=5000, debug=True) 