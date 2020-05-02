def factorial_recursive(number):
    if number<=1:
        return 1
    if number>1:
        return number*factorial_recursive(number-1)
number=int(input('enter the number:'))
print(f'the factorial of {number} is',factorial_recursive(number))