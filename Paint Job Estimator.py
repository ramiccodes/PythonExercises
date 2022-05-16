squarefeet = int(input("Please enter the square feet of wall space to be painted: "))
paint = int(input("Please enter the price of paint per gallon: "))
sq_multiply = squarefeet / 112
paint_gallon = 1
labor_hours = 8
sq_paint_total = round(paint_gallon * sq_multiply, 2)
sq_labor_total = round(labor_hours * sq_multiply, 2)
paint_cost = paint * sq_paint_total
labor_price = sq_labor_total * 35


print("The number of gallons of paint required is", sq_paint_total)
print("The hours of labor required is", sq_labor_total)
print("The cost of paint is $", paint_cost)
print("The price of labor is $", labor_price)
print("The total cost of this paint job is $", round(labor_price + paint_cost, 2))