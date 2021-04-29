#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input("Enter a number to check if it is a prime number"))
count = 0

for i in range(1, n+1):
    if not n % i:    # if n%i ==0
        count +=1
if (n==0) or (n == 1) or (n>=3):
    print(n, "is not a prime number")
else:
    print(n, "is a prime number")

