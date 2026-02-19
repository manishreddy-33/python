"""#print 1 to 100 natural numbers
i=0
while i<=100:
    print(i)
    i+=1"""

"""#print even numbers between 1 to 40
i=2
while i<=40:
    print(i)
    i+=2"""

"""#print odd numbers between 1 to50
i=1
while i<=50:
    print(i)
    i+=2"""
    
"""#find which number is even and odd from the list of numbers
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        print("Even:", numbers[i])
    else:
        print("Odd:", numbers[i])
    i += 1"""

#sum of even numbers from upto 'n'
n = int(input("Enter the value of n: "))
i = 2
sum_even = 0
while i <= n:
    sum_even = sum_even + i
    i = i + 2

print("Sum of even numbers =", sum_even)
