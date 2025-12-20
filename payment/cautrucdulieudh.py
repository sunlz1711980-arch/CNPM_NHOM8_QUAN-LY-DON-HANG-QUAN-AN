from datetime import datetime

class Order:
    def __init__(self, order_id, items, extra_fee=0, vat_rate=0.1):
        """
        items: list of tuple (ten_mon, so_luong, don_gia)
        """
        self.order_id = order_id
        self.items = items
        self.extra_fee = extra_fee
        self.vat_rate = vat_rate
        self.status = "Chưa thanh toán"