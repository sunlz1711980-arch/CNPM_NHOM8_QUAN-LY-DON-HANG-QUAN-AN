def update_item(menu_list):
    print("\n--- CẬP NHẬT MÓN ĂN ---")
    name = input("Nhập tên món cần sửa: ")
    for item in menu_list:
        if item["name"].lower() == name.lower():
            new_price = float(input(f"Nhập giá mới cho {name}: "))
            item["price"] = new_price
            print("✅ Cập nhật thành công!")
            return
    print("❌ Không tìm thấy món ăn này.")