from db_config import DatabaseConnection

class ComputerManager:
    def __init__(self):
        self.db = DatabaseConnection()

    def add_computer(self, company_id, serial_number, ip_address, mac_address, status, manager):
        try:
            connection = self.db.connect()
            cursor = connection.cursor()
            
            query = """INSERT INTO computers 
                    (company_id, serial_number, ip_address, mac_address, status, manager)
                    VALUES (%s, %s, %s, %s, %s, %s)"""
            values = (company_id, serial_number, ip_address, mac_address, status, manager)
            
            cursor.execute(query, values)
            connection.commit()
            print("电脑信息添加成功！")
            
        except Exception as e:
            print(f"添加电脑信息失败: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def update_computer(self, id, **kwargs):
        try:
            connection = self.db.connect()
            cursor = connection.cursor()
            
            set_clause = ", ".join([f"{key} = %s" for key in kwargs.keys()])
            query = f"UPDATE computers SET {set_clause} WHERE id = %s"
            values = tuple(kwargs.values()) + (id,)
            
            cursor.execute(query, values)
            connection.commit()
            print("电脑信息更新成功！")
            
        except Exception as e:
            print(f"更新电脑信息失败: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete_computer(self, id):
        try:
            connection = self.db.connect()
            cursor = connection.cursor()
            
            query = "DELETE FROM computers WHERE id = %s"
            cursor.execute(query, (id,))
            connection.commit()
            print("电脑信息删除成功！")
            
        except Exception as e:
            print(f"删除电脑信息失败: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def get_computer(self, id=None):
        try:
            connection = self.db.connect()
            cursor = connection.cursor(dictionary=True)
            
            if id:
                query = "SELECT * FROM computers WHERE id = %s"
                cursor.execute(query, (id,))
                return cursor.fetchone()
            else:
                query = "SELECT * FROM computers"
                cursor.execute(query)
                return cursor.fetchall()
                
        except Exception as e:
            print(f"查询电脑信息失败: {e}")
            return None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close() 