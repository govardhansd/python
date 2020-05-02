from factorial_iterative import factorial_iterative
def ratio(x,N,e):
    temp=1
    a=1
    for i in range(1,N+1):
        temp=temp+(x**i/factorial_iterative(i))
        if temp-a>0:
            if temp-a<e:
                break
            else:
                a=temp
                continue
    return temp,i
x=float(input("enter the value of x"))
N=int(input("enter the number of times to be added"))
e=float(input("enter the small positive number"))
ratio,N_stop=ratio(x,N,e)
print("the output of the ratio is {:.3f} for N={}".format(ratio,N_stop))