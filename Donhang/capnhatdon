def cap_nhat_trang_thai_don():
    ma_don = int(input("Nhập mã đơn cần cập nhật: "))

    for don in don_hang_list:
        if don["ma_don"] == ma_don:
            print("Trạng thái hiện tại:", don["trang_thai"])
            don["trang_thai"] = input("Nhập trạng thái mới: ")
            print("✅ Đã cập nhật trạng thái!")
            return

    print("❌ Không tìm thấy đơn!")