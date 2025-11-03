print("hello world ")
for x in range(10):
    print(x, end = ' ')

d = 3
m = 11
y = 2025
print("Today's date is" ,d,m,y, sep ='/')
print(d,m,y,sep ='-')



num = int(input())
for i in range(1, 11):
    print(num, 'x',i, '=',num*i)
    print(f'{num} x {i} =  {num*i}')
    print('{0} x {1} = {2}'.format(num,i, num*i))
    print('%d x %d = % ' %(num, i, num*i))



pi = 22/7
print(f'Value of PI = {pi:.3f}')
print('Value of PI = {0:.4f}' .format(pi))
print('Value of PI = %.5f' %(pi))





print('{0}'.format(1))
print('{0}'.format(11))
print('{0}'.format(111))
print('{0}'.format(1111))
print('{0}'.format(11111))
print('{0}'.format(111111))
print('{0}'.format(1111111))



print('{0:7d}'.format(1))
print('{0:7d}'.format(11))
print('{0:7d}'.format(111))
print('{0:7d}'.format(1111))
print('{0:7d}'.format(11111))
print('{0:7d}'.format(111111))
print('{0:7d}'.format(1111111))

