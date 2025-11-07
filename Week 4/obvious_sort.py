l = [1, 3, 1, 789, 2345, 6, 8901, 23456, 34567]
# l.sort()
# print(l)
'''Let us write a piece of code that that does what we just now explained'''

l = [12,3,4,45,67,87,78,34,23,56,1,23,22,34]
x = []
while(len(l)>0):
    min = l[0]
    for i in range(len(l)):
        if l[i] < min:
            min = l[i]
    x.append(min)
    l.remove(min)

print(l)
print(x)

           