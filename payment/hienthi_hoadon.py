def hien_thi_hoa_don(don):
    print("\n" + "="*30)
    print(f"HÓA ĐƠN MÃ: {don['ma_don']}")
    for item in don["danh_sach_mon"]:
        print(f"{item['ten_mon']:<15} x{item['so_luong']} {item['gia']*item['so_luong']}")
    print(f"TỔNG CỘNG: {don['tong_tien']}")
    print("="*30)
