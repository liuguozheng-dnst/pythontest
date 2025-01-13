from db_config import DatabaseConnection

class SoftwareManager:
    def __init__(self):
        self.db = DatabaseConnection()

    def add_software(self, name, status, user, license_count):
        try:
            connection = self.db.connect()
            cursor = connection.cursor()
            
            query = """INSERT INTO software 
                    (name, status, user, license_count)
                    VALUES (%s, %s, %s, %s)"""
            values = (name, status, user, license_count)
            
            cursor.execute(query, values)
            connection.commit()
            print("软件信息添加成功！")
            
        except Exception as e:
            print(f"添加软件信息失败: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def update_software(self, id, **kwargs):
        try:
            connection = self.db.connect()
            cursor = connection.cursor()
            
            set_clause = ", ".join([f"{key} = %s" for key in kwargs.keys()])
            query = f"UPDATE software SET {set_clause} WHERE id = %s"
            values = tuple(kwargs.values()) + (id,)
            
            cursor.execute(query, values)
            connection.commit()
            print("软件信息更新成功！")
            
        except Exception as e:
            print(f"更新软件信息失败: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete_software(self, id):
        try:
            connection = self.db.connect()
            cursor = connection.cursor()
            
            query = "DELETE FROM software WHERE id = %s"
            cursor.execute(query, (id,))
            connection.commit()
            print("软件信息删除成功！")
            
        except Exception as e:
            print(f"删除软件信息失败: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def get_software(self, id=None):
        try:
            connection = self.db.connect()
            cursor = connection.cursor(dictionary=True)
            
            if id:
                query = "SELECT * FROM software WHERE id = %s"
                cursor.execute(query, (id,))
                return cursor.fetchone()
            else:
                query = "SELECT * FROM software"
                cursor.execute(query)
                return cursor.fetchall()
                
        except Exception as e:
            print(f"查询软件信息失败: {e}")
            return None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close() 