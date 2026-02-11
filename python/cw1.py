import random

apple = 15.5
orange = 20
grape = 10.25

total = apple + orange + grape
print("Total volume sold is:", total)

total_int = int(total)
print("Total volume as integer is:", total_int)

total_str = str(total)
print("Total volume as string is:", total_str)

bonus = random.randint(5, 10)
print("Random bonus volume is:", bonus)

final = total + bonus
print("Final volume is:", final)
