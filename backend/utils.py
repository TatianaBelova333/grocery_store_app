from decimal import Decimal


def calculate_total_price(
        item_price: Decimal, discount: int, quantity: int
) -> Decimal:
    if discount > 0:
        item_price *= Decimal((100 - discount / 100))

    total_price = Decimal(item_price * quantity)
    return total_price
