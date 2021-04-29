#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    number = input("enter a positiv number: ")
    digits = len(number)
    summ = 0
    
    if not number.isdigit():
        print(number, "is invalid entry. Enter a numeric value")
        
    elif int(number) >= 0:
        for i in range(digits):
            summ = summ + int(number[i])**digits
            
        if summ == int(number):
            print(number, "is an Amstrong number.")
        else:
            print(number, "is not an Amstrong number")
            break

