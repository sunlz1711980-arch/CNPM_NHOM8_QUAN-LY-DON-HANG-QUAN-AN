def xac_nhan_thanh_toan():
    return input("Xác nhận thanh toán? (y/n): ").lower() == "y"
def cap_nhat_thanh_toan(don, ban=None):
    while True:
        ngay = input("Nhập ngày (DD): ").strip()
        thang = input("Nhập tháng (MM): ").strip()
        nam = input("Nhập năm (YYYY): ").strip()

        if not (ngay.isdigit() and thang.isdigit() and nam.isdigit()):
            print("❌ Ngày tháng năm phải là số!")
            continue

        if not (1 <= int(ngay) <= 31 and 1 <= int(thang) <= 12):
            print("❌ Ngày hoặc tháng không hợp lệ!")
            continue

        break

    don["trang_thai"] = "Hoàn thành"
    don["ngay"] = f"{nam}-{thang.zfill(2)}-{ngay.zfill(2)}"
    don["thang"] = f"{nam}-{thang.zfill(2)}"
    don["nam"] = nam

    if ban:
        ban["trang_thai"] = "Trống"
        ban["ma_don"] = None

    save_data()
    print("✅ Thanh toán hoàn tất!")
