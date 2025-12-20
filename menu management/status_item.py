def toggle_status(menu_list):
    print("\n--- ẨN MÓN / ĐÁNH DẤU HẾT HÀNG ---")
    name = input("Nhập tên món cần thay đổi trạng thái: ")
    for item in menu_list:
        if item["name"].lower() == name.lower():
            item["is_available"] = not item["is_available"]
            trang_thai = "Còn hàng" if item["is_available"] else "Hết hàng/Ẩn"
            print(f"✅ Món '{name}' hiện đang ở trạng thái: {trang_thai}")
            return
    print("❌ Không tìm thấy món ăn này.")