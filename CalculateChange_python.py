bill = float(input('How much is your bill:'))
pay = float(input('How much is payment:'))
change = round(pay - bill, 2)
print('Hi!Your Change is {:.2f}' .format( change))