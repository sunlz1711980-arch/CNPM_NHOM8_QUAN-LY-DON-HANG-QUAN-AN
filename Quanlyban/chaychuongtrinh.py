def menu_quan_ly_ban():
    while True:
        clear_screen()
        print("=== QUẢN LÝ BÀN ===")
        print("1. Khởi tạo sơ đồ bàn")
        print("2. Gán đơn vào bàn")
        print("3. Xem danh sách bàn")
        print("0. Quay lại")

        c = nhap_lua_chon(["1", "2", "3", "0"])

        if c == "1":
            clear_screen()
            print("=== KHỞI TẠO SƠ ĐỒ BÀN ===")
            khoi_tao_ban()
            pause()

        elif c == "2":
            clear_screen()
            print("=== GÁN ĐƠN VÀO BÀN ===")
            gan_don_vao_ban()
            pause()

        elif c == "3":
            clear_screen()
            print("=== DANH SÁCH BÀN ===")
            if not ban_list:
                print("⚠️ Chưa có bàn nào!")
            else:
                for b in ban_list:
                    print(f"Bàn {b['ma_ban']} | {b['trang_thai']} | Mã đơn: {b['ma_don']}")
            pause()

        elif c == "0":
            break
