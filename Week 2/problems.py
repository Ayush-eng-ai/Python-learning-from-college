# problem 1: Find whether the given number is even or odd 
num = int(input("Enter a number: "))
if(num % 2 == 0):
    print(f"{num} is an even number")
    print("Enjoy your day")

else:
    print(f"{num} is an odd number")        
    print("Have a nice day")
    

# Problem 2: Find whether the given number ends with 0  or 5 or  any other number
num = int(input("Enter a number: "))
last_digit = num % 10
if(last_digit == 0):
    print(f"{num} ends with 0")
    print("Enjoy your day")
elif(last_digit == 5):
    print(f"{num} ends with 5")
    print("Have a nice day")
else:
    print(f"{num} ends with {last_digit}")  
    print("any other number")


# Problem 3: Find the grade of student based on the given marks from 0 to 100.
marks = int(input("Enter your marks: "))
if(marks >= 90 and marks <= 100):
    print("Your grade is A")
    print("Excellent")
elif(marks >= 80 and marks < 90):
    print("Your grade is B")
    print("Very Good")
elif(marks >= 70 and marks < 80):
    print("Your grade is C")
    print("Good")
elif(marks >= 60 and marks < 70):
    print("Your grade is D")
    print("Average")
elif(marks >= 0 and marks < 60):
    print("Your grade is E")
    print("Below Average")
else:
    print("Invalid marks")


# Problem 4: convert the given flowchart into a python code 
print('Travel from city A to city B')
Time = int(input('Enter the time in hours: '))
longer =int(input('Is it a longer route? (1 for Yes / 0 for No): '))
if(Time <= 1 and longer == 0):
    print('Take a taxi')
elif(Time <= 1 and longer == 1):
    print('Take a bus')
elif(Time > 1 and Time <= 3 and longer == 0):
    print('Take a bus')
elif(Time > 1 and Time <= 3 and longer == 1):
    print('Take a train')
elif(Time > 3 and longer == 0):
    print('Take a train')   
elif(Time > 3 and longer == 1):
    print('Take a flight')  
else:
    print('Invalid input')      
print('Have a safe journey!')
# Problem 4: Second type solve the problem 
print('Travel from city A to city B')
Time = int(input('Enter the time : '))
longer = int(input('Define Longer:'))
if(Time >=longer):
    Price = int(input('Enter the price: '))
    Higher = int(input('Define Higher:'))
    if(Price >= Higher):
        print('Take a Train')
    else:
        print('Take a Coach')
else:
    Price = int(input('Enter the price: '))
    Higher = int(input('Define Higher:'))
    if(Price >= Higher):
        print('Take a Flight') 
    else:
        print('Red eye Flight')
print('Have a safe journey!')
print('Arrive city B ')


