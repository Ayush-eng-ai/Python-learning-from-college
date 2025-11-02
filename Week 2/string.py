#An Interesting Cipher: More on Strings
# This is Popularly called the Caesar Cipher in cryptography
# Each letter is replaced by the next letter in the alphabet
alpha = 'abcdefghijklmnopqrstuvwxyz'
print(alpha[0]) # Output: a
print(alpha[1]) # Output: b
print(alpha[25]) # Output: z
print(alpha[-1]) # Output: z
print(alpha[-3]) # Output: x
n = len(alpha)
print(n) # Output: 26
i = 6 
i = i%26
print(alpha[i]) # Output: g
print(alpha[i-1]) # Output: f
print(alpha[i+1]) # Output: h
print(alpha[n-1]) # Output: z   
print(alpha[n-2]) # Output: y
print(alpha[n-3]) # Output: x
print(alpha[n-4]) # Output: w
print(alpha[-n]) # Output: a
print(alpha[-(n-1)]) # Output: b
print(alpha[-(n-2)]) # Output: c

s = 'Ayush'
# I expect to output tvebstibo
t = ' '
print((alpha.index(s[0]) + 1) % 26)
alpha. index(s[0])
t += alpha[ (alpha.index(s[0]) + 1) % 26 ]
alpha. index(s[1])  






