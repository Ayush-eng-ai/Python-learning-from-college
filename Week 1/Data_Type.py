#Data Type 1
#Integer
a = 5
b = 10
c = a + b
print("Sum:", c)
print(type(c))

#Float
x = 5.5
y = 10.5
z = x + y
print("Sum:", z)
print(type(z))

#String
first_name = "Ayush"
last_name = "Rajput"
full_name = first_name + " " + last_name
print("Full Name:", full_name)
print(type(full_name))



#Boolean
is_student = True
is_employed = False
print("Is Student:", is_student)
print("Is Employed:", is_employed)
print(type(is_student))
print(type(is_employed))


#List
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print("Fruits:", fruits)
print(type(fruits))

#Tuple
coordinates = (10.0, 20.0)
print("Coordinates:", coordinates)
print(type(coordinates))

#Dictionary
person = {"name": "Ayush", "age": 20}
print("Person:", person)
print(type(person))         

#Set
unique_numbers = {1, 2, 3, 4, 5}
print("Unique Numbers:", unique_numbers)
print(type(unique_numbers))

#Type Conversion
#Implicit Conversion
num = 5
print("Integer:", num)
print("Float:", float(num))
print("String:", str(num))
print("Boolean:", bool(num))
print(type(num))
print(type(float(num)))
print(type(str(num)))
print(type(bool(num)))

#Explicit Conversion
num_str = "10"
num_int = int(num_str)
num_float = float(num_str)
num_bool = bool(num_str)
print("String:", num_str)
print("Integer:", num_int)
print("Float:", num_float)
print("Boolean:", num_bool)
print(type(num_str))
print(type(num_int))
print(type(num_float))
print(type(num_bool))


#Type Casting
a = 5
b = 2
c = a / b  # Division results in float
d = a // b # Floor division results in integer
print("Division:", c)
print("Floor Division:", d)
print(type(c))
print(type(d))

#Type Checking
var1 = 10
var2 = 10.5 
var3 = "Hello"
var4 = True
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(isinstance(var1, int))
print(isinstance(var2, float))
print(isinstance(var3, str))
print(isinstance(var4, bool))
print(isinstance(var1, float))  # False
print(isinstance(var2, int))    # False
print(isinstance(var3, bool))   # False
print(isinstance(var4, str))    # False
print(isinstance(var1, (int, float)))  # True
print(isinstance(var2, (int, float)))  # True
print(isinstance(var3, (str, list)))   # True
print(isinstance(var4, (bool, int)))   # True
print(isinstance(var1, (str, list)))   # False
print(isinstance(var2, (str, list)))   # False
print(isinstance(var3, (int, float)))  # False
print(isinstance(var4, (str, list)))   # False
print(isinstance(var1, object))  # True
print(isinstance(var2, object))  # True
print(isinstance(var3, object))  # True
print(isinstance(var4, object))  # True
print(isinstance(var1, type(var2)))  # False
print(isinstance(var2, type(var3)))  # False
print(isinstance(var3, type(var4)))  # False
print(isinstance(var4, type(var1)))  # False
print(isinstance(var1, type(var1)))  # True
print(isinstance(var2, type(var2)))  # True
print(isinstance(var3, type(var3)))  # True
print(isinstance(var4, type(var4)))  # True
print(isinstance(var1, (int, str)))  # True
print(isinstance(var2, (float, bool)))  # True
print(isinstance(var3, (str, int)))  # True
print(isinstance(var4, (bool, float)))  # True
print(isinstance(var1, (list, dict)))  # False
print(isinstance(var2, (list, dict)))  # False
print(isinstance(var3, (list, dict)))  # False
print(isinstance(var4, (list, dict)))  # False
print(isinstance(var1, (int, float, str, bool)))  # True
print(isinstance(var2, (int, float, str, bool)))  # True
print(isinstance(var3, (int, float, str, bool)))  # True
print(isinstance(var4, (int, float, str, bool)))  # True
print(isinstance(var1, (list, dict, set)))  # False
print(isinstance(var2, (list, dict, set)))  # False
print(isinstance(var3, (list, dict, set)))  # False
print(isinstance(var4, (list, dict, set)))  # False
print(isinstance(var1, (int, float, str, bool, list, dict, set)))  # True
print(isinstance(var2, (int, float, str, bool, list, dict, set)))  # True
print(isinstance(var3, (int, float, str, bool, list, dict,  set)))  # True
print(isinstance(var4, (int, float, str, bool, list, dict, set)))  # True   
print(isinstance(var1, (int, float, str, bool, list, dict, set, tuple)))  # True
print(isinstance(var2, (int, float, str, bool, list, dict,      set, tuple)))  # True
print(isinstance(var3, (int, float, str, bool, list, dict, set, tuple)))  # True
print(isinstance(var4, (int, float, str, bool, list, dict,
        set, tuple)))  # True
print(isinstance(var1, (int, float, str, bool, list, dict, set, tuple, complex)))  # True
print(isinstance(var2, (int, float, str, bool, list, dict, set, tuple, complex)))  # True
print(isinstance(var3, (int, float, str, bool, list, dict, set, tuple, complex)))  # True
print(isinstance(var4, (int, float, str, bool, list, dict,  set, tuple, complex)))  # True
print(isinstance(var1, (int, float, str, bool, list, dict, set, tuple, complex, bytes)))  # True
print(isinstance(var2, (int, float, str, bool, list, dict, set, tuple, complex, bytes)))  # True
print(isinstance(var3, (int, float, str, bool, list, dict, set, tuple, complex, bytes)))  # True
print(isinstance(var4, (int, float, str, bool, list, dict, set, tuple, complex, bytes)))  # True
print(isinstance(var1, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray)))  # True
print(isinstance(var2, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray)))  # True 




print(isinstance(var3, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray)))  # True
print(isinstance(var4, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray)))  # True

print(isinstance(var1, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview)))  # True
print(isinstance(var2, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview)))  # True
print(isinstance(var3, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview)))  # True
print(isinstance(var4, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview)))  # True
print(isinstance(var1, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range)))  # True
print(isinstance(var2, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range)))  # True
print(isinstance(var3, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range)))  # True
print(isinstance(var4, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range)))  # True
print(isinstance(var1, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range, frozenset)))  # True
print(isinstance(var2, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range, frozenset)))  # True
print(isinstance(var3, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range, frozenset)))  # True

print(isinstance(var4, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range, frozenset)))  # True
print(isinstance(var1, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range, frozenset, None)))  # True
print(isinstance(var2, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range, frozenset, None)))  # True
print(isinstance(var3, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range, frozenset, None)))  # True
print(isinstance(var4, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range, frozenset, None)))  # True
print(isinstance(var1, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range, frozenset, None, type)))  # True
print(isinstance(var2, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range, frozenset, None, type)))  # True
print(isinstance(var3, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range, frozenset, None, type)))  # True

print(isinstance(var4, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range, frozenset, None, type)))  # True
print(isinstance(var1, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range, frozenset, None, type, object)))  # True
print(isinstance(var2, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range, frozenset, None, type, object)))  # True

print(isinstance(var3, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range, frozenset, None, type, object)))  # True
print(isinstance(var4, (int, float, str, bool, list, dict, set, tuple, complex, bytes, bytearray, memoryview, range, frozenset, None, type, object)))  # True










