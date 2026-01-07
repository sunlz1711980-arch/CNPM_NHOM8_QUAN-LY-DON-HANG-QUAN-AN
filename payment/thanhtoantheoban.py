# ================== THANH TOÁN ==================
def thanh_toan_theo_ban():
    try:
        so_ban = int(input("Nhập số bàn: "))
    except:
        print("❌ Số bàn không hợp lệ!")
        return

    ban = next((b for b in ban_list if b["ma_ban"] == so_ban), None)
    if not ban or not ban["ma_don"]:
        print("❌ Bàn không có đơn hàng!")
        return

    don = next((d for d in don_hang_list if d["ma_don"] == ban["ma_don"]), None)
    if not don:
        print("❌ Không tìm thấy đơn hàng!")
        return

    hien_thi_hoa_don(don)

    if xac_nhan_thanh_toan():
        cap_nhat_thanh_toan(don, ban)
