def factorial_iterative(number):
    if number<=1:
        return 1
    if number>1:
        fact=1
        for i in range(1,number+1):
            fact=fact*i
        return fact
number=int(input('enter the number:'))
print(f'the factorial of {number} is ',factorial_iterative(number))