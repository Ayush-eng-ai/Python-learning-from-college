import random
print(random.random())

l =[]
for i in range(50):
    l.append(random.randint(1,365))
print(l)
i = 0
flag =0 #denotes that there is no repetition
while(i<=len(l)-1):
    if(l[i]==l[i+1]):
        print('Repeats',l[i],l[i+1])
        flag = 1 
        break
    i = i + 1  
if flag == 0:
    print('There is no repetition.')