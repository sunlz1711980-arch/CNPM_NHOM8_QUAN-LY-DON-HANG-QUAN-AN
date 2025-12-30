def chuyen_ban():
    ban_cu = int(input("Nhập bàn hiện tại: "))
    ban_moi = int(input("Nhập bàn muốn chuyển sang: "))

    ban_nguon = next((b for b in ban_list if b["ma_ban"] == ban_cu), None)
    ban_dich = next((b for b in ban_list if b["ma_ban"] == ban_moi), None)

    if not ban_nguon or not ban_dich:
        print("❌ Bàn không tồn tại!")
        return

    if ban_nguon["trang_thai"] == "Trống":
        print("❌ Bàn nguồn đang trống!")
        return

    if ban_dich["trang_thai"] == "Có khách":
        print("❌ Bàn đích đang có khách!")
        return

    ban_dich["trang_thai"] = "Có khách"
    ban_dich["ma_don"] = ban_nguon["ma_don"]

    ban_nguon["trang_thai"] = "Trống"
    ban_nguon["ma_don"] = None

    print("✅ Chuyển bàn thành công!")