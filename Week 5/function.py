def add(a,b):
    ans = (a+b)
    return ans

a = 2 
b= 15
ans = add(a,b)+10
print(ans)

def discount(cost,d):
    ans = cost - (cost *(d/100))
    return ans
print("Enter the cost price:")
c = int(input())
print("Enter the discount percentage:")
d = int(input())
final_price = discount(c,d)
print("The final price after discount is:",final_price)

