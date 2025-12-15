def entry_ui():
    """
    Giao diện đầu vào của hệ thống
    Hiển thị ngay khi người dùng truy cập vào web/app
    """

    while True:
        print("\n====== CHÀO MỪNG ĐẾN HỆ THỐNG ======")
        print("1. Đăng ký tài khoản (nếu chưa có)")
        print("2. Đăng nhập (nếu đã có)")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            register()

        elif choice == "2":
            login()
            # TODO: nếu đăng nhập thành công -> vào hệ thống chính
            break

        elif choice == "0":
            exit()

        else:
            print("Lựa chọn không hợp lệ.")
def register():
    pass  # US-001 Đăng ký tài khoản nhân viên


def login():
    pass  # US-002 Đăng nhập

