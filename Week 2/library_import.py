import math
print(math.log(10))
print(math.sqrt(16))
print(math.factorial(5))
print(math.sin(90))
print(math.cos(0))
print(math.tan(45)) 
print(math.pi)
print(math.e)
print(math.pow(2,3))
print(math.ceil(4.2))



#Let us simulate a coin toss.
import random
a = random.random()
print(a)
if a < 0.5:
    print('Heads')
else:
    print('Tails')

#Let us simulate the sum of two dice rolls.
dice1 = (random.randrange(1,7) ) # from 1 to 6
dice2 =(random.randrange(1,7))
total = dice1 + dice2
print(f'You rolled a {dice1} and a {dice2}. Total is {total}')


print(random.randint(1,100))
print(random.random())
print(random.choice(['apple', 'banana', 'cherry']))



# import calendar
import calendar as c
print(c.month(2024,6))
print(c.month(2024,6))
print(c.isleap(2020))
print(c.calendar(2025))

from calendar import*
print(calendar(2026))

from calendar import month as m 
print(m(2024,6))


