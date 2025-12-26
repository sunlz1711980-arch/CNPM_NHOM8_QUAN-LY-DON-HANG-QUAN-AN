def nhan_don_online():
    global ma_don_tu_tang

    ten_khach = input("Nhập tên khách online: ")
    dia_chi = input("Nhập địa chỉ giao hàng: ")
    tong_tien = float(input("Nhập tổng tiền: "))

    don_hang = {
        "ma_don": ma_don_tu_tang,
        "ten_khach": ten_khach,
        "dia_chi": dia_chi,
        "loai": "Online",
        "tong_tien": tong_tien,
        "trang_thai": "Chờ xác nhận"
    }

    don_hang_list.append(don_hang)
    ma_don_tu_tang += 1
    print("✅ Đã nhận đơn online!")