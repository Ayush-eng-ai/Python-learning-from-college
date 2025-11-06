l = [1,2,3,4,5,6,7,8,9,10]
# target = 5
# i = 0
# found = False
# while i < len(l):
#     if l[i] == target:
#         found = True
#         break
#     i += 1
# if found:
#     print(f'Found {target} at index {i}')
# else:
#     print(f'{target} not found in the list')


import random
l = [1,3,456,789,567172,2345,6789,8901,23456,34567]
a = 567172
#for i in range(100):
    #l.append(random.randint(1,365))
flag =0
for i in range(len(l)):
    if (a==l[i]):
        print("Hip Hip Hurray, Element found")
        flag = 1
        break
if flag == 0:
    print("Element not found")