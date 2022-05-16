import math
import random
firstnum = random.randint(0,1000)
secondnum = random.randint(0,1000)
sum = firstnum + secondnum
print("               Addition Quiz")
print("================================================")
print("             What is", firstnum, "+", secondnum, "?")
answer = int(input("Please write your answer here: "))

if answer == sum:
    print("You got the correct answer!")
else:
    print("That's the incorrect answer. The right answer is", sum)
