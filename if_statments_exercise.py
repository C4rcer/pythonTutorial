price = 1000000  # price of the house
has_good_credit = False  # do they have good credit bool

if has_good_credit:
    down_payment = 0.1 * price  # working out 10% of the house as down for good credit
else:
    down_payment = 0.2 * price  # working out 20% of the house as down for not good credit
print(f"Down payment: ${down_payment}")  # formatted print statement
