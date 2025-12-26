def tao_don_hang_tai_quan():
    global ma_don_tu_tang

    ten_khach = input("Nhập tên khách hàng: ")
    tong_tien = float(input("Nhập tổng tiền: "))

    don_hang = {
        "ma_don": ma_don_tu_tang,
        "ten_khach": ten_khach,
        "loai": "Tại quán",
        "tong_tien": tong_tien,
        "trang_thai": "Đang xử lý"
    }

    don_hang_list.append(don_hang)
    ma_don_tu_tang += 1
    print("✅ Đã tạo đơn hàng tại quán!")