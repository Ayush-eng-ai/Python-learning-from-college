s = 'VIBGYOR'
t = 'VIBGYOR'


print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
print(s[6])

for i in range(7):
    print(s[i])

#Example of a nested for Loop

for i in range(7):
    for j in range (7):
        print(i,j,s[i], s[j])
        count = count+1


print("The total ways in which the two brothers can wear 7 different colours:",count)


# Second Example
students = ["A", "B", "C"]
subjects = ["Math", "Science", "English"]

for student in students:
    for subject in subjects:
        print(student, subject)

