l = [1,2,3,4,5,5,75,67,89,45]
sum = 0 
for i in range(len(l)):
    sum = sum+l[i]
print("The sum of the elements in the list is:",sum)


import random
l = [1,2,3,4,5,5,75,67,89,45]
l = random.sample(list(range(10000)),1000)
sum = 0 
for i in range(len(l)):
    sum = sum+l[i]
print("The sum of the elements in the list is:",sum)


import random
#write a piece of code to find the dot product.
x=[1,7,3,4]
y=[5,2,4,3]
dot_product = (1*5)+(7*2)+(3*4)+(4*3)
print("The dot product of the two lists is:",dot_product)


x=[1,7,3,4]
y=[5,2,4,3]
dot_product = 0
for i in range(len(x)):
    dot_product += x[i] * y[i]
print("The dot product of the two lists is:",dot_product)