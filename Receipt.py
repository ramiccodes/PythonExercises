price = float(input("Enter the price of the item:"))
rate = float(100)
tax = int(input("Enter the tax rate:"))
tax_rate = tax / rate
tax_price = price * tax_rate
item_price = price + tax_price
item_num = 1
total = 0.0
total += item_price
#=========================================================

print("Item      Price      Tax Rate(%)    Item Price")

print("==============================================")
print(item_num,"        ",price,"        ",tax, "%","        ",item_price)

item = input("Are there more items?(y/n):")

while item == "y":
    price = float(input("Enter the price of the item:"))
    rate = float(100)
    tax = int(input("Enter the tax rate:"))
    tax_rate = tax / rate
    tax_price = price * tax_rate
    item_price = price + tax_price
    total += item_price
    item_num += 1
    print("Item      Price      Tax Rate(%)    Item Price")
    print("==============================================")
    print(item_num,"        ",price,"        ",tax, "%","        ",item_price)
    item = input("Are there more items?(y/n):")
if item == "y":
    price = float(input("Enter the price of the item:"))
    rate = float(100)
    tax = int(input("Enter the tax rate:"))
    tax_rate = tax / rate
    tax_price = price * tax_rate
    item_price = price + tax_price
    total += item_price
    item_num += 1
    print("Item      Price      Tax Rate(%)    Item Price")
    print("==============================================")
    print(item_num,"        ",price,"        ",tax, "%","        ",item_price)
    item = input("Are there more items?(y/n):")

print("==============================================")

if total >= 1000:
    discount = 0.03
    total_discount = total * discount
    total_deduct = total - total_discount
    print("Total amount + 3% discount:", total_deduct)
else:
    print("Total amount:", total)





 
