def login():
    global current_user

    if not users:
        print("❌ Chưa có tài khoản nào được đăng ký!")
        input("\nNhấn Enter để quay lại...")
        return False

    while True:
        username = input("Tên đăng nhập: ").strip()
        if username == "":
            print("❌ Tên đăng nhập không được để trống!")
            continue

        user_found = next((u for u in users if u["username"] == username), None)
        if not user_found:
            print("❌ Tài khoản không tồn tại!")
            continue
        break

    while True:
        password = input("Mật khẩu: ").strip()
        if password == "":
            print("❌ Mật khẩu không được để trống!")
            continue

        if password != user_found["password"]:
            print("❌ Sai mật khẩu!")
            continue
        break

    current_user = user_found
    print(f"✅ Xin chào {username}")

    if current_user["role"] == "quan_ly":
        print("🔑 Quyền: Quản lý")
    else:
        print("👷 Quyền: Nhân viên")

    return True
