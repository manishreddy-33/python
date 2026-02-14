# read input numbers from user
"""num = input()
print(type(num)) # checking the type of number
print(num)"""
# implicit type conversion
"""num1 = int(input())
val = float(input())
print(type(num1), type(val)) # checking the type of number
res = num1 + val
print(res)"""


"""num1 = input() # read string type number
print(type(num1)) #checking the type of number
res = num1 + 10
print(res)"""
#to overcome above problem by usng explicit type conversion
"""

num1=input () #read string type number
res = int(num1) +10
print(res)
"""
#converting integer to float and boolean
num = 12
print(float(num))
print(str(num))
print(bool(num))
