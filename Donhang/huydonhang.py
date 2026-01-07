def huy_don_hang():
    try:
        ma_don = int(input("Nhập mã đơn cần hủy: "))
    except:
        print("❌ Mã đơn không hợp lệ!")
        return

    don = next((d for d in don_hang_list if d["ma_don"] == ma_don), None)
    if not don:
        print("❌ Không tìm thấy đơn hàng!")
        return

    if don["trang_thai"] == "Hoàn thành":
        print("❌ Đơn hàng đã thanh toán, không thể hủy!")
        return
    confirm = input(f"⚠️ Bạn có chắc muốn hủy đơn {ma_don}? (y/n): ").lower()
    if confirm != "y":
        print("❎ Đã hủy thao tác.")
        return
    if don["trang_thai"] == "Đã hủy":
        print("⚠️ Đơn hàng này đã bị hủy trước đó!")
        return

    # 🔄 HOÀN TRẢ KHO
    for item in don["danh_sach_mon"]:
        kho = lay_so_luong_ton(item["ten_mon"])
        if kho:
            kho["so_luong"] += item["so_luong"]
        else:
            kho_nguyen_lieu.append({
                "ten": item["ten_mon"].lower(),
                "so_luong": item["so_luong"]
            })

    # 🔓 GIẢI PHÓNG BÀN NẾU CÓ
    for ban in ban_list:
        if ban["ma_don"] == ma_don:
            ban["trang_thai"] = "Trống"
            ban["ma_don"] = None

    don["trang_thai"] = "Đã hủy"
    save_data()
    print(f"✅ Đã hủy thành công đơn hàng mã {ma_don}")
