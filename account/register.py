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
