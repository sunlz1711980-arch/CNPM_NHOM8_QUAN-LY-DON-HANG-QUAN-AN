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
