def calc_discount(price, percentage):
    discounted = price - (price * percentage / 100)
    print("Discount applied:", discounted)
    return discounted

def add_tax(price, tax):
    return price + price * tax / 100
