def add_item(menu_list):
    print("\n--- THÊM MÓN ĂN MỚI ---")
    name = input("Nhập tên món ăn: ")
    price = float(input("Nhập giá tiền: "))
    menu_list.append({
        "name": name,
        "price": price,
        "is_available": True  # Mặc định là còn hàng
    })
    print(f"✅ Đã thêm món '{name}' vào menu.")