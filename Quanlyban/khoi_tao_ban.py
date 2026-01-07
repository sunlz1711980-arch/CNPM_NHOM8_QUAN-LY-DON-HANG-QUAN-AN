def khoi_tao_ban():
    so = int(input("Số lượng bàn muốn tạo: "))
    ban_list.clear()
    for i in range(1, so+1):
        ban_list.append({"ma_ban": i, "trang_thai": "Trống", "ma_don": None})
    print(f"✅ Đã khởi tạo {so} bàn.")
    save_data()
