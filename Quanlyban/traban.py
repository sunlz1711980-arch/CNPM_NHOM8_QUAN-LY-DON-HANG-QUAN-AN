def tra_ban():
    ma_ban = int(input("Nhập số bàn: "))

    for ban in ban_list:
        if ban["ma_ban"] == ma_ban:
            ban["trang_thai"] = "Trống"
            ban["ma_don"] = None
            print("✅ Đã trả bàn!")
            return

    print("❌ Không tìm thấy bàn!")