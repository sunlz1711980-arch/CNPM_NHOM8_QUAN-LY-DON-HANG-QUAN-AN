def tinh_tong_thanh_toan(tien_mon, phu_phi=0, vat=0):
    tong = tien_mon + phu_phi
    tong += tong * vat
    return tong
