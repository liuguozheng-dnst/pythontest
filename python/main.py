from computer_manager import ComputerManager
from software_manager import SoftwareManager
from item_manager import ItemManager

def print_menu():
    print("\n=== 物品管理系统 ===")
    print("1. 电脑管理")
    print("2. 软件管理")
    print("3. 其他物品管理")
    print("0. 退出")

def computer_menu():
    print("\n=== 电脑管理 ===")
    print("1. 添加电脑")
    print("2. 更新电脑信息")
    print("3. 删除电脑")
    print("4. 查看电脑信息")
    print("0. 返回主菜单")

def software_menu():
    print("\n=== 软件管理 ===")
    print("1. 添加软件")
    print("2. 更新软件信息")
    print("3. 删除软件")
    print("4. 查看软件信息")
    print("0. 返回主菜单")

def item_menu():
    print("\n=== 其他物品管理 ===")
    print("1. 添加物品")
    print("2. 更新物品信息")
    print("3. 删除物品")
    print("4. 查看物品信息")
    print("0. 返回主菜单")

def main():
    computer_mgr = ComputerManager()
    software_mgr = SoftwareManager()
    item_mgr = ItemManager()

    while True:
        print_menu()
        choice = input("请选择操作: ")

        if choice == "1":
            while True:
                computer_menu()
                sub_choice = input("请选择操作: ")
                
                if sub_choice == "1":
                    # 添加电脑
                    company_id = input("请输入公司编号: ")
                    serial_number = input("请输入序列号: ")
                    ip_address = input("请输入IP地址: ")
                    mac_address = input("请输入物理地址: ")
                    status = input("请输入使用状态(在用/闲置/维修/报废): ")
                    manager = input("请输入管理者: ")
                    computer_mgr.add_computer(company_id, serial_number, ip_address, 
                                           mac_address, status, manager)
                
                elif sub_choice == "2":
                    # 更新电脑信息
                    id = input("请输入要更新的电脑ID: ")
                    print("请输入要更新的信息（直接回车跳过）：")
                    updates = {}
                    for field in ["status", "manager", "ip_address", "mac_address"]:
                        value = input(f"新的{field}: ")
                        if value:
                            updates[field] = value
                    if updates:
                        computer_mgr.update_computer(id, **updates)

                elif sub_choice == "3":
                    # 删除电脑
                    id = input("请输入要删除的电脑ID: ")
                    computer_mgr.delete_computer(id)

                elif sub_choice == "4":
                    # 查看电脑信息
                    id = input("请输入要查看的电脑ID（直接回车查看所有）: ")
                    if id:
                        print(computer_mgr.get_computer(id))
                    else:
                        print(computer_mgr.get_computer())

                elif sub_choice == "0":
                    break

        elif choice == "2":
            while True:
                software_menu()
                sub_choice = input("请选择操作: ")
                
                if sub_choice == "1":
                    # 添加软件
                    name = input("请输入软件名称: ")
                    status = input("请输入使用状态(在用/闲置/过期): ")
                    user = input("请输入使用人员: ")
                    license_count = input("请输入许可证数量: ")
                    software_mgr.add_software(name, status, user, license_count)

                elif sub_choice == "2":
                    # 更新软件信息
                    id = input("请输入要更新的软件ID: ")
                    print("请输入要更新的信息（直接回车跳过）：")
                    updates = {}
                    for field in ["status", "user", "license_count"]:
                        value = input(f"新的{field}: ")
                        if value:
                            updates[field] = value
                    if updates:
                        software_mgr.update_software(id, **updates)

                elif sub_choice == "3":
                    # 删除软件
                    id = input("请输入要删除的软件ID: ")
                    software_mgr.delete_software(id)

                elif sub_choice == "4":
                    # 查看软件信息
                    id = input("请输入要查看的软件ID（直接回车查看所有）: ")
                    if id:
                        print(software_mgr.get_software(id))
                    else:
                        print(software_mgr.get_software())

                elif sub_choice == "0":
                    break

        elif choice == "3":
            while True:
                item_menu()
                sub_choice = input("请选择操作: ")
                
                if sub_choice == "1":
                    # 添加物品
                    name = input("请输入物品名称: ")
                    status = input("请输入使用状态(在用/闲置/维修/报废): ")
                    user = input("请输入使用人员: ")
                    item_mgr.add_item(name, status, user)

                elif sub_choice == "2":
                    # 更新物品信息
                    id = input("请输入要更新的物品ID: ")
                    print("请输入要更新的信息（直接回车跳过）：")
                    updates = {}
                    for field in ["status", "user"]:
                        value = input(f"新的{field}: ")
                        if value:
                            updates[field] = value
                    if updates:
                        item_mgr.update_item(id, **updates)

                elif sub_choice == "3":
                    # 删除物品
                    id = input("请输入要删除的物品ID: ")
                    item_mgr.delete_item(id)

                elif sub_choice == "4":
                    # 查看物品信息
                    id = input("请输入要查看的物品ID（直接回车查看所���）: ")
                    if id:
                        print(item_mgr.get_item(id))
                    else:
                        print(item_mgr.get_item())

                elif sub_choice == "0":
                    break

        elif choice == "0":
            print("感谢使用！再见！")
            break

if __name__ == "__main__":
    main() 