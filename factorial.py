def factorial(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n * factorial(n-1)

num=int(input("Enter Number: "))
if num<0:
    print("Number should be greater than 0")
elif num==0:
    print("Factorial of your number is: 1")
else:
    print("Factorial of your number is:",factorial(num))