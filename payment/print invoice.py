def thanh_toan_don_hang():
    ma_don = int(input("Nhập mã đơn cần thanh toán: "))

    for don in "don_hang_list":
        if don["ma_don"] == ma_don:

            if don["trang_thai"] == "Hoàn tất":
                print("❌ Đơn hàng đã thanh toán!")
                return

            # Nhập phí
            tien_mon = don["tong_tien"]
            phu_phi = float(input("Nhập phụ phí (nếu không có nhập 0): "))
            vat = float(input("Nhập VAT (ví dụ 0.1 cho 10%, nếu không có nhập 0): "))

            tong_thanh_toan = "tinh_tong_thanh_toan"(tien_mon, phu_phi, vat)

            print("Tổng cần thanh toán:", tong_thanh_toan, "VND")

            # Chọn phương thức thanh toán
            print("Chọn phương thức thanh toán:")
            print("1. Tiền mặt")
            print("2. Quẹt thẻ")
            print("3. QR Pay")

            chon = input("Chọn: ")

            if chon == "1":
                phuong_thuc = "Tiền mặt"
            elif chon == "2":
                phuong_thuc = "Quẹt thẻ"
            elif chon == "3":
                phuong_thuc = "QR Pay"
            else:
                print("❌ Phương thức không hợp lệ")
                return

            # Cập nhật đơn hàng
            don["tong_tien"] = tong_thanh_toan
            don["phuong_thuc"] = phuong_thuc
            don["trang_thai"] = "Hoàn tất"

            print("✅ Thanh toán thành công!")
            "in_hoa_don"(don)
            return

    print("❌ Không tìm thấy đơn hàng!")
