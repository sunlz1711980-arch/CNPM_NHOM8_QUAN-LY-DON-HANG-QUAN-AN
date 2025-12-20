def choose_payment_method():
    print("Chọn phương thức thanh toán:")
    print("1. Tiền mặt")
    print("2. Quét thẻ")
    print("3. QR Pay")

    choice = input("Nhập lựa chọn (1/2/3): ")

    methods = {
        "1": "Tiền mặt",
        "2": "Quẹt thẻ",
        "3": "QR Pay"
    }

    return methods.get(choice, None)