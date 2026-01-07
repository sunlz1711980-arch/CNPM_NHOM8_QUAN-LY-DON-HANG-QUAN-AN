# ================== QUẢN LÝ ĐƠN HÀNG ==================
def tao_don_hang():
    global ma_don_tu_tang
    hien_thi_menu(menu_list)

    danh_sach_chon = []
    tong_tien = 0

    while True:
        id_mon = input("Nhập ID món muốn đặt (hoặc '0' để kết thúc): ").strip()
        if id_mon == "0":
            break

        if not id_mon.isdigit():
            print("❌ ID phải là số!")
            continue

        mon_tim_thay = next((m for m in menu_list if m["id"] == int(id_mon)), None)
        if not mon_tim_thay:
            print("❌ ID món không tồn tại!")
            continue

        # 🔗 LIÊN KẾT KHO
        kho_mon = lay_so_luong_ton(mon_tim_thay["ten_mon"])
        if not kho_mon or kho_mon["so_luong"] <= 0:
            print("❌ Món này đã hết hàng, vui lòng chọn món khác!")
            continue

        print(f"📦 Số lượng còn trong kho: {kho_mon['so_luong']}")

        try:
            sl = int(input(f"Số lượng cho món {mon_tim_thay['ten_mon']}: "))
        except:
            print("❌ Số lượng phải là số!")
            continue

        if sl <= 0:
            print("❌ Số lượng phải lớn hơn 0!")
            continue

        if sl > kho_mon["so_luong"]:
            print(f"❌ Không đủ hàng! Chỉ còn {kho_mon['so_luong']} phần.")
            continue

        # ✅ TRỪ KHO
        kho_mon["so_luong"] -= sl

        danh_sach_chon.append({
            "ten_mon": mon_tim_thay["ten_mon"],
            "gia": mon_tim_thay["gia"],
            "so_luong": sl
        })

        tong_tien += mon_tim_thay["gia"] * sl
        print(f"✅ Đã thêm {sl} x {mon_tim_thay['ten_mon']}")

    if danh_sach_chon:
        bay_gio = datetime.now()
        don_moi = {
            "ma_don": ma_don_tu_tang,
            "danh_sach_mon": danh_sach_chon,
            "tong_tien": tong_tien,
            "ngay": bay_gio.strftime("%Y-%m-%d"),
            "thang": bay_gio.strftime("%Y-%m"),
            "trang_thai": "Chưa thanh toán"
        }

        don_hang_list.append(don_moi)
        print(f"✅ Tạo đơn thành công! Mã đơn: {ma_don_tu_tang}")
        ma_don_tu_tang += 1
        save_data()
    else:
        print("⚠️ Đơn hàng trống.")
