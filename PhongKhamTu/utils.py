from PhongKhamTu import dao
<<<<<<< HEAD
=======


>>>>>>> c742fa719d8ffa1e1e5c999c866f59d3bb8270b7
def count_cart(cart):
    total_amount = 0

    if cart:
        for c in cart.values():
            total_amount += c['soLuong'] * c['giaThuoc']

    return total_amount

<<<<<<< HEAD
=======

>>>>>>> c742fa719d8ffa1e1e5c999c866f59d3bb8270b7
def total_bill(month):
    total = 0
    month_stats = dao.bill_stats(month)
    for s in month_stats:
        total = total + s[1]
    return total