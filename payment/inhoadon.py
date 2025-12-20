def print_invoice(order, payment_method):
    print("\n===== HÓA ĐƠN THANH TOÁN =====")
    print(f"Mã đơn: {order.order_id}")
    print(f"Thời gian: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("-----------------------------")

    for name, qty, price in order.items:
        print(f"{name} x{qty} - {qty * price} VND")

    print("-----------------------------")
    print(f"Phụ phí: {order.extra_fee} VND")
    print(f"TỔNG TIỀN: {order.calculate_total()} VND")
    print(f"Thanh toán bằng: {payment_method}")
    print("Trạng thái: Hoàn tất")
    print("=============================\n")