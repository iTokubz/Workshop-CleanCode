def calculate_total_price(prices):
    total_price = 0
    for price in prices:
        total_price += price
    return total_price


def calculate_total_tax(taxes):
    total_tax = 0
    for tax in taxes:
        total_tax += tax
    return total_tax


def calculate_total(prices, taxes):
    total_price = calculate_total_price(prices)
    total_tax = calculate_total_tax(taxes)
    return total_price + total_tax
