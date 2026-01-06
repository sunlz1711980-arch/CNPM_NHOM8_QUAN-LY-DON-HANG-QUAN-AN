def show_menu():
    for i, item in enumerate(menu_list, 1):
        print(f"{i}. {item['name']} - {item['price']} ({'Còn' if item['is_available'] else 'Hết'})")
# ================== HIỂN THỊ MENU DẠNG BẢNG ==================
def hien_thi_menu(menu_list):
    if not menu_list:
        print("Menu hiện đang trống.")
        return

    print("=" * 80)
    print(f"{'ID':<5} {'Tên món':<25} {'Giá':<10} {'Loại':<15} {'Trạng thái':<20}")
    print("-" * 80)

    for mon in menu_list:
        print(
            f"{mon['id']:<5} "
            f"{mon['ten_mon']:<25} "
            f"{mon['gia']:<10} "
            f"{mon['loai']:<15} "
            f"{mon['trang_thai']:<20}"
        )

    print("=" * 80)
