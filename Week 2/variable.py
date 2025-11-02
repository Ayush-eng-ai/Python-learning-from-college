# Variables: A Programmer's perspective
# A variable is a named location in memory that stores a value.
# Variables can hold different types of data, such as numbers, strings, lists, etc.
# In Python, you don't need to declare the type of a variable explicitly; it is inferred from the value assigned to it.
# Here are some examples of variable assignments in Python:

ram_bank_balance = 100000 
# ram's bank balance, note that this is positive

ram_loan = 500000
#ram'sloan, this is to be returened by him and hence will count
#as negative 




Lakshman_bank_balance = 2000000
Lakshman_loan= 1000000
#net_income  is the total bank balance  of the two brothers.

net_income = ram_bank_balance +Lakshman_bank_balance
#net_liablity is the total loan of the two brothers.
net_liablity = ram_loan + Lakshman_loan
#final_value is the net worth of the two brothers.
#It is calculated by subtracting the net liability from the net income.

final_value = net_income - net_liablity
# final_value is the family's final money (could be +ve or -ve)
print(final_value)
print("So,the family has",final_value)


# Variables Revisited Dynamic Typing
# In Python, variables are dynamically typed, meaning that the type of a variable is determined at runtime based on the value assigned to it.
a=10 # a is an integer
print(type(a)) # Output: <class 'int'>

a="India"
print(type(a)) # Output: <class 'str'>

n = 10
print(type(n)) # Output: <class 'int'>
print(n)
n=n/2
print(type(n)) # Output: <class 'float'>
print(n)

x=y=z=5
print(x,y,z) # Output: 5 5 5

x,y = 1,2
print(x,y) # Output: 1 2
x,y = y,x
print(x,y) # Output: 2 1

count=0
count += 1
count += 1
print(count) # Output: 2

print("alpha" in "A variable name can only contain alpha-numeric characters and underscores" )
print("alpha" in "  A variable name must start with a letter or the underscore character")



x= 5
print(1< x < 10) # Output: True
print(1 < x < 20) # Output: False
print(x < 10 < x*10  < 100)
print(10 < x  < 20 < x*10<100)
print(4 == x > 4) # Output: False
print(4 <= x >= 4) # Output: True




#### Escape chracters and type of quotes
print("It's a beautiful day")
print('it\'s a beautiful day')
print('We are from \'IIT\' Madras')
print("We are from 'IIT' Madras")
print('My name is Ayush. \t\t I am from Farrukhabad') #for space
print("My name is Ayush. \n I am from Farrukhabad") # for new line

x = "this is string "
y = 'this is also a string'
z = """This is a
second line
third line""" #multiple line string
'''first line 
second
third line
fourth line''' #multiple line comment

print(z)
print(x)
print(y)




