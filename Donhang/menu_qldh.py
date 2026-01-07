
def menu_quan_ly_don_hang():
    while True:
        clear_screen()
        print("=== QUẢN LÝ ĐƠN HÀNG ===")
        print("1. Tạo đơn mới")
        print("2. Xem danh sách đơn")
        print("0. Quay lại")

        c = nhap_lua_chon(["1","2","0"])

        if c == "1":
            clear_screen()
            print("=== TẠO ĐƠN HÀNG ===")
            tao_don_hang()
            pause()

        elif c == "2":
            clear_screen()
            print("=== DANH SÁCH ĐƠN ===")
            for d in don_hang_list:
                print(f"Mã: {d['ma_don']} | Tổng: {d['tong_tien']} | Trạng thái: {d['trang_thai']}")
            pause()

        elif c == "0":
            break
