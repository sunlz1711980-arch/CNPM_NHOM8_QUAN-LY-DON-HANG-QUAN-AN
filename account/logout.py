#US-003: Đăng xuất
def logout(current_user):
    if current_user:
        print(f"🔓 Tài khoản '{current_user['username']}' đã đăng xuất.")
    else:
        print("⚠️ Chưa có tài khoản nào đăng nhập.")