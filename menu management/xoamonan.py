def xoa_mon_an():
    hien_thi_menu(menu_list)

    try:
        id_mon = int(input("Nhập ID món cần xóa: "))
    except:
        print("❌ ID phải là số!")
        return

    mon = tim_mon_theo_id(id_mon)
    if not mon:
        print("❌ Không tìm thấy món!")
        return

    confirm = input(f"⚠️ Bạn chắc chắn muốn xóa '{mon['ten_mon']}'? (y/n): ")
    if confirm.lower() == "y":
        menu_list.remove(mon)
        save_data()
        print("✅ Đã xóa món ăn!")
    else:
        print("❎ Hủy xóa.")
