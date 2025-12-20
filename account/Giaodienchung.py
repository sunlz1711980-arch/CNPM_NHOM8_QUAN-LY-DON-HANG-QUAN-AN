
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
            print("Thoát chương trình.")
            break   # ✅ thay exit() bằng break

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

        else:
            print("Lựa chọn không hợp lệ.")  # ✅ bổ sung

# US-001: Đăng ký tài khoản
def register(users):
    print("\n====== ĐĂNG KÝ TÀI KHOẢN ======")

    username = input("Nhập tên đăng nhập: ")

    # Kiểm tra trùng username
    for user in users:
        if user["username"] == username:
            print("❌ Tên đăng nhập đã tồn tại!")
            return

    password = input("Nhập mật khẩu: ")
    confirm_password = input("Nhập lại mật khẩu: ")

    # Kiểm tra xác nhận mật khẩu
    if password != confirm_password:
        print("❌ Mật khẩu không khớp!")
        return

    # Lưu user
    users.append({
        "username": username,
        "password": password
    })

    print("✅ Đăng ký thành công!")

def login(users):
    print("\n--- ĐĂNG NHẬP ---")
    username = input("Tên đăng nhập: ")
    password = input("Mật khẩu: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print("✅ Đăng nhập thành công!")
            return user

    print("❌ Sai tên đăng nhập hoặc mật khẩu.")
    return None

# US-002: Đăng nhập
def forgot_password(users):
    print("\n====== QUÊN MẬT KHẨU ======")

    username = input("Nhập tên đăng nhập: ")

    for user in users:
        if user["username"] == username:
            new_password = input("Nhập mật khẩu mới: ")
            confirm_password = input("Nhập lại mật khẩu mới: ")

            if new_password != confirm_password:
                print("❌ Mật khẩu không khớp!")
                return

            user["password"] = new_password
            print("✅ Đổi mật khẩu thành công!")
            return

    print("❌ Không tìm thấy tài khoản!")

#US-003: Đăng xuất
def logout(current_user):
    if current_user:
        print(f"🔓 Tài khoản '{current_user['username']}' đã đăng xuất.")
    else:
        print("⚠️ Chưa có tài khoản nào đăng nhập.")
def entry_ui():
    global current_user

    while True:
        print("\n====== CHÀO MỪNG ĐẾN HỆ THỐNG ======")
        print("1. Đăng ký")
        print("2. Đăng nhập")
        print("3. Quên mật khẩu")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            register(users)

        elif choice == "2":
            user = login(users)
            if user:
                current_user = user
                main_ui()

        elif choice == "3":
            forgot_password(users)

        elif choice == "0":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ.")
def main():
    entry_ui()
if __name__ == "__main__":
    main()
