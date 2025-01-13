from db_config import DatabaseConnection

class ItemManager:
    def __init__(self):
        self.db = DatabaseConnection()

    def add_item(self, name, status, user):
        try:
            connection = self.db.connect()
            cursor = connection.cursor()
            
            query = """INSERT INTO other_items 
                    (name, status, user)
                    VALUES (%s, %s, %s)"""
            values = (name, status, user)
            
            cursor.execute(query, values)
            connection.commit()
            print("物品信息添加成功！")
            
        except Exception as e:
            print(f"添加物品信息失败: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def update_item(self, id, **kwargs):
        try:
            connection = self.db.connect()
            cursor = connection.cursor()
            
            set_clause = ", ".join([f"{key} = %s" for key in kwargs.keys()])
            query = f"UPDATE other_items SET {set_clause} WHERE id = %s"
            values = tuple(kwargs.values()) + (id,)
            
            cursor.execute(query, values)
            connection.commit()
            print("物品信息更新成功！")
            
        except Exception as e:
            print(f"更新物品信息失败: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete_item(self, id):
        try:
            connection = self.db.connect()
            cursor = connection.cursor()
            
            query = "DELETE FROM other_items WHERE id = %s"
            cursor.execute(query, (id,))
            connection.commit()
            print("物品信息删除成功！")
            
        except Exception as e:
            print(f"删除物品信息失败: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def get_item(self, id=None):
        try:
            connection = self.db.connect()
            cursor = connection.cursor(dictionary=True)
            
            if id:
                query = "SELECT * FROM other_items WHERE id = %s"
                cursor.execute(query, (id,))
                return cursor.fetchone()
            else:
                query = "SELECT * FROM other_items"
                cursor.execute(query)
                return cursor.fetchall()
                
        except Exception as e:
            print(f"查询物品信息失败: {e}")
            return None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close() 