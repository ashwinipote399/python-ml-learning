# number basics

num = 2
float_num = 1.35 # decimalnumber  

#print the orginial and decimal number
print(num)
print(float_num)

#print the number with string 
print(str(num)  +  "is my favourite number")

#basic arithmetic operation 

#sum operator
print(1 + 2)

#difference or minus operator
print(1 - 2)

#divide operator
print(2 /3)

#multiplication operator
print(2*3)


# floor division operator means (Divide and take only the whole number part (ignore decimal)).
print(2//3) 


#  modules operator where we take remainder value only. 
print(2%3)  

#print absolute number
print(abs(-2))  # --> returns only the value, no sign (+ or −).

#print powers operator and  power function
print(3 ** 4)
print(pow(3 , 4))  # 3^4

#print maximum number
print(max(4, 1))

#print minimum number
print(min(2, 3, 4, 6))

#print roundoff number
print(round(3.78))

#in python importing is used to use functions or tools from another file or library.
from math import *
print(ceil(9.1))  # --> Round a number UP to the nearest whole number.
print(ceil(3.2))

#print squareroot of a number
print(sqrt(81))