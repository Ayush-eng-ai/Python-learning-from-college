
''' Simple rule
     Use 'for' when number of repetition is known.
     use 'while' when the repetition depends on  a codition.
     '''



'''using while loop Problem Solving'''
'''Problem 1: Find the factorial of the given number'''
num = int(input("Enter a number: "))
fact =1 
if (num<0):
    print("Not Defined")
else:
    while(num>0):
        fact = fact *num
        num= num -1
    print(fact)
    
'''using for loop Problem Solving'''
'''Problem 1: Find the factorial of the given number'''
num = int(input("Enter a number: "))
fact =1 
if (num<0):
    print("Not Defined")
else:
    for i in range(num, 1, -1 ):
        fact = fact *i
    print (fact)



# using while Loop 
'''Problem 2: Find the number of digits in the given number'''
num = abs(int(input("Enter a number: ")))
digits = 1 
while(num>10):
    num = num// 10
    digits += 1
print(digits)


# using for loop 

'''Problem 2: Find the number of digits in the given number'''
num = abs(int(input("Enter a number: ")))
strNum = str(num)
digits = 0
for c in strNum:
    digits = digits + 1
print(digits)



#Using the while Loop
'''Problem 3: Reverse the digits in the given number'''
num = int(input('Enter a number: '))
absNum = abs(num)
rev = absNum % 10
absNum = absNum //10
while(absNum >0):
    r = absNum % 10
    absNum = absNum //10
    rev = rev * 10 + r
if(num>0):
    print(rev)
else:
    print(rev = 2*rev)


#Using for Loop
'''Problem 3: Reverse the digits in the given number'''
num = int(input('Enter a number: '))
absStrNum = str(abs(num))
rev = ""
for c in absStrNum:
    rev = c + rev
if(num>=0):
    print(rev)
else:
    print('-' + rev)



#Using While Loop 
'''Problem 4: find Whether the entered numbeer is palindrome or not'''
num = int(input('Enter a number: '))
absNum = abs(num)
rev = absNum % 10
absNum = absNum//10
while(absNum >0):
    r = absNum % 10
    absNum = absNum //10
    rev = rev * 10 +r
if(num<0):
    rev = rev - 2 *rev
if(rev == num):
    print("palindrome")
else:
    print("Not a palindrome")



#Using While Loop 
'''Problem 4: find Whether the entered numbeer is palindrome or not'''
num = int(input('Enter a number: '))
absStrNum = str(abs(num))
rev = ''
for c in absStrNum:
    rev = c + rev
if(num < 0):
    rev = "-" + rev 
if(num == int(rev)):
    print("palindrome")
else:
    print("Not a palindrome")
    


 


