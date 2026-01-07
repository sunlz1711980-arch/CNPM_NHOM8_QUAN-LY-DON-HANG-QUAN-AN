def thanh_toan_theo_ma_don():
    try:
        ma_don = int(input("Nhập mã đơn: "))
    except:
        print("❌ Mã đơn không hợp lệ!")
        return

    don = next((d for d in don_hang_list if d["ma_don"] == ma_don), None)
    if not don:
        print("❌ Không tìm thấy đơn hàng!")
        return

    ban = next((b for b in ban_list if b["ma_don"] == ma_don), None)

    hien_thi_hoa_don(don)

    if xac_nhan_thanh_toan():
        cap_nhat_thanh_toan(don, ban)# Epic: Thanh toán

