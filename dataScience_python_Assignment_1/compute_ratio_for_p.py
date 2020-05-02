from factorial_iterative import factorial_iterative
def ratio(x,n=100):
    temp=0
    for i in range(0,n+1):
        temp=temp+(x**i/factorial_iterative(i))
    return temp
p=int(input("enter the value of p"))
q=int(input("enter the value of q"))
v1=ratio(p)*ratio(q)
r=p+q
v2=ratio(r)
print('v1:',v1)
print('v2:',v2)
print("v1-v2:",v1-v2)