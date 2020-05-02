from factorial_iterative import factorial_iterative
def ratio(x,n):
    return x**n/factorial_iterative(n)
x=float(input("enter the value of x"))
n=int(input("enter the value of n"))
ratio=ratio(x,n)
print("the output of the ratio is {:.3f}".format(ratio))