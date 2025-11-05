#Using break Keyword  

#25f1002575@ds.study.iitm.ac.in
email = input()
for c in email:
    if(c == '@'):
        break
    print(c, end = ' ')

#Continue Keyword
email = input()
for c in email:
    if(c == '@'):
        print(' ')
        continue
    print(c, end = ' ')

#pass keyword
for x in range(11):
    if(x % 3 == 0):
        print(x)
    else:
        pass