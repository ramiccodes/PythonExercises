enter = int(input("Enter an integer:"))
div_3 = 3
div_4 = 4
if enter % div_3 == 0:
    print("This integer is divisible by 3.")
else:
    print("This integer is not divisible by 3.")
if enter % div_4 == 0:
    print("This integer i divisible by 4.")
else:
    print("This integer is not divisible by 4.")
if enter % div_4 and div_3 != 0:
    print("This integer is not divisible by 3 and 4.")

