def hien_thi_menu(danh_sach):
    if not danh_sach:
        print("Danh sách hiện đang trống.")
        return
    print("=" * 80)
    print(f"{'ID':<5} {'Tên món':<25} {'Giá':<10} {'Loại':<15} {'Trạng thái':<20}")
    print("-" * 80)
    for mon in danh_sach:
        print(f"{mon['id']:<5} {mon['ten_mon']:<25} {mon['gia']:<10} {mon['loai']:<15} {mon['trang_thai']:<20}")
    print("=" * 80)
