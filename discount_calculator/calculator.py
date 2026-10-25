def calculate_discount(price: float, discount: float) -> float:
    final_price = price * (1 - min(discount, 1.0))
    return max(0.0, final_price)