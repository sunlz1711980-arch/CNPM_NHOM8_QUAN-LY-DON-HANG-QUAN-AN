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
    # ================== HIỂN THỊ MÓN CÒN BÁN ==================
def hien_thi_menu_con_ban(menu_list):
    ds_con_ban = [mon for mon in menu_list if mon["trang_thai"] == "Còn bán"]

    if not ds_con_ban:
        print("Hiện không có món nào còn bán.")
        return
# ================== TÌM KIẾM MÓN ==================
def tim_kiem_mon(menu_list):
    tu_khoa = input("Nhập tên món cần tìm: ").lower()
    ket_qua = [mon for mon in menu_list if tu_khoa in mon["ten_mon"].lower()]

    if not ket_qua:
        print("❌ Không tìm thấy món.")
        return

    hien_thi_menu(ket_qua)

def sap_xep_menu_theo_ten(menu_list):
    ds_sap_xep = sorted(menu_list, key=lambda mon: mon["ten_mon"])
    hien_thi_menu(ds_sap_xep)
def sap_xep_menu_theo_gia(menu_list):
    ds_sap_xep = sorted(menu_list, key=lambda mon: mon["gia"])
    hien_thi_menu(ds_sap_xep)
    hien_thi_menu(ds_con_ban)

# ================== MENU CHÍNH ==================
def main():
    while True:
        print("\n===== QUẢN LÍ MENU =====")
        print("1. Thêm món")
        print("2. Xem danh sách menu")
        print("3. Ngừng / mở bán món")
        print("4. Xem món còn bán")
        print("5. Tìm kiếm món")
        print("0. Thoát")

        chon = input("Chọn chức năng: ")

        if chon == "1":
            add_item(menu_list)
        elif chon == "2":
            hien_thi_menu(menu_list)
        elif chon == "3":
            cap_nhat_trang_thai_mon(menu_list)
        elif chon == "4":
            hien_thi_menu_con_ban(menu_list)
        elif chon == "5":
            tim_kiem_mon(menu_list)
        elif chon == "0":
            print("Thoát chương trình.")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

            print("2. Xem danh sách menu")
            print("3. Ngừng / mở bán món")
            print("4. Xem món còn bán")
            print("5. Tìm kiếm món")
            print("0. Thoát")

        chon = input("Chọn chức năng: ")

        if chon == "1":
            add_item(menu_list)
        elif chon == "2":
            hien_thi_menu(menu_list)
        elif chon == "3":
            cap_nhat_trang_thai_mon(menu_list)
        elif chon == "4":
            hien_thi_menu_con_ban(menu_list)
        elif chon == "5":
            tim_kiem_mon(menu_list)
        elif chon == "0":
            print("Thoát chương trình.")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")
