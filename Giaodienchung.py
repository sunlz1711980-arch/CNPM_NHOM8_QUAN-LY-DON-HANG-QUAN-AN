
users = []
current_user = None

def entry_ui():
    global current_user

    while True:
        print("\n====== CHÀO MỪNG ĐẾN HỆ THỐNG ======")
        print("1. Đăng ký")
        print("2. Đăng nhập")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            register(users)

        elif choice == "2":
            user = login(users)
            if user:
                current_user = user
                main_ui()

        elif choice == "0":
            exit()

        else:
            print("Lựa chọn không hợp lệ.")


def main_ui():
    global current_user

    while True:
        print("\n====== HỆ THỐNG CHÍNH ======")
        print("1. Chức năng demo")
        print("2. Đăng xuất")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            print("👉 Chức năng demo")

        elif choice == "2":
            logout(current_user)
            current_user = None
            break
