#operators and Expressions 1
#Arithmetic Operators(+,-,/,//,%,**)

a = 10
b = 3
print("Addition:", a + b)        # Addition
print("Subtraction:", a - b)     # Subtraction
print("Multiplication:", a * b)  # Multiplication
print("Division:", a / b)        # Division
print("Floor Division:", a // b) # Floor Division
print("Modulus:", a % b)         # Modulus
print("Exponentiation:", a ** b) # Exponentiation





#Comparison Operators(Relational Operators)(==,!=,>,<,>=,<=)
x = 5
y = 10
print("Equal:", x == y)           # Equal
print("Not Equal:", x != y)       # Not Equal
print("Greater Than:", x > y)     # Greater Than
print("Less Than:", x < y)        # Less Than
print("Greater Than or Equal To:", x >= y) # Greater Than or Equal To
print("Less Than or Equal To:", x <= y)    # Less Than or Equal To




#Logical Operators(and,or,not)
a = True
b = False
print("Logical AND:", a and b)  # Logical AND
print("Logical OR:", a or b)    # Logical OR
print("Logical NOT:", not a)     # Logical NOT



#Assignment Operators(=,+=,-=,*=,/=,//=,%=,**=)
x = 10
print("Initial Value:", x)
x += 5
print("After += 5:", x)
x -= 3
print("After -= 3:", x)
x *= 2
print("After *= 2:", x)
x /= 4
print("After /= 4:", x)
x //= 2
print("After //= 2:", x)
x %= 3
print("After %= 3:", x)
x **= 2
print("After **= 2:", x)



#Bitwise Operators(&,|,^,~,<<,>>)
a = 5  # Binary: 0101
b = 3  # Binary: 0011
print("Bitwise AND:", a & b)  # Bitwise AND
print("Bitwise OR:", a | b)   # Bitwise OR
print("Bitwise XOR:", a ^ b)  # Bitwise XOR
print("Bitwise NOT:", ~a)      # Bitwise NOT
print("Left Shift:", a << 1)   # Left Shift
print("Right Shift:", a >> 1)  # Right Shift



#Membership Operators(in,not in)
fruits = ["apple", "banana", "cherry"]
print("Is 'apple' in fruits?", "apple" in fruits)       # Membership IN
print("Is 'grape' not in fruits?", "grape" not in fruits) # Membership NOT IN
#Identity Operators(is,is not)
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)         # Identity IS
print("x is z:", x is z)         # Identity IS
print("x is not z:", x is not z) # Identity IS NOT
print("x == z:", x == z)         # Equality ==
print("x != z:", x != z)         # Inequality !=


#Operator Precedence
a = 10
b = 5
c = 2
result = a + b * c - (a / b) ** c
print("Result:", result)  # Result: 19.0
#Parentheses have the highest precedence, followed by exponentiation, multiplication/division, and finally addition/subtraction.


#Expressions
x = 5
y = 10
z = 15
result = (x + y) * z / (y - x)
print("Expression Result:", result)  # Expression Result: 45.0
#The expression (x + y) * z / (y - x) is evaluated step-by-step according to operator precedence and parentheses.
#In this case, (x + y) is evaluated first, then multiplied by z, and finally divided by (y - x).
#The final result is 45.0.
#Expressions can be more complex and can include multiple operators and operands.
#Understanding operator precedence and using parentheses can help ensure that expressions are evaluated as intended.
#It's important to note that Python follows the standard mathematical rules for operator precedence.
#Using parentheses can help clarify the order of operations in complex expressions.
#This code demonstrates the use of various operators and expressions in Python.
#You can run this code in a Python environment to see the output of each operation.
#Feel free to modify the values of variables and experiment with different operators and expressions to further understand their behavior.
#You can also combine multiple operators in a single expression to see how they interact with each other.
#This code serves as a basic introduction to operators and expressions in Python programming.
#Practice using operators and expressions in your own Python programs to become more comfortable with them.
#Remember to always test your code and verify the results to ensure that your expressions are working as expected.


#Happy coding!


#Type Conversion
#Explicit Conversion
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)
print("String:", num_str)
print("Integer:", num_int)
print("Float:", num_float)
print(type(num_str))
print(type(num_int))
print(type(num_float))




#logical Operators (and,or,not)
is_student = True
has_id = False
print("Is Student and Has ID:", is_student and has_id)  # Logical AND
print("Is Student or Has ID:", is_student or has_id)    # Logical OR
print("Is Not Student:", not is_student)                 # Logical NOT
print(type(is_student))
print(type(has_id))
print(type(is_student and has_id))

print(type(is_student or has_id))
print(type(not is_student))
print(type(True))
print(type(False))
print(type(1))
print(type(0))
print(type(None))
print(type([]))
print(type({}))
print(type(()))
print(type(set()))
print(type(""))
print(type("Hello"))
print(type(3.14))
print(type(42))
print(type(-1))
print(type(0.0))
print(type(1.0))
print(type(-3.14))
print(type(2 + 3j))
print(type(5 > 3))
print(type(5 < 3))
print(type(5 == 5))
print(type(5 != 3))
print(type(5 >= 3))
print(type(5 <= 3))
print(type(5 and 3))
print(type(5 or 3))
print(type(not 5))
print(type(5 & 3))
print(type(5 | 3))
print(type(5 ^ 3))

print(type(~5))
print(type(5 << 1))
print(type(5 >> 1))
print(type(5 is 5))
print(type(5 is not 3))
print(type(5 in [1, 2, 3, 4, 5]))
print(type(6 not in [1, 2, 3, 4, 5]))
print(type(5 + 3))
print(type(5 - 3))
print(type(5 * 3))
print(type(5 / 3))
print(type(5 // 3))
print(type(5 % 3))
print(type(5 ** 3))
x = 5
x += 3
print(type(x))
# Assignment operators cannot be used directly inside print(type(...)), so these lines are removed.
# print(type(5 -= 3))
# print(type(5 *= 3))
# print(type(5 /= 3))
# print(type(5 //= 3))
# print(type(5 %= 3))
# print(type(5 **= 3))


r = 5  # Example radius
area = 3.14159 * r ** 2  # Calculate area of circle
print("Area of circle with radius", r, "is:", area)



