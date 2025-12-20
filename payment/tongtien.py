def calculate_total(self):
        subtotal = sum(qty * price for _, qty, price in self.items)
        vat = subtotal * self.vat_rate
        total = subtotal + vat + self.extra_fee
        return round(total, 2)