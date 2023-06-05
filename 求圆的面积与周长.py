def cir(r):
    PI=3.14
    s=PI*r*r
    l=2*PI*r
    return (s,l)

r=float(input("input the r:"))
(s,l)=cir(r)
print("the s is:%.3f,the l is:%.3f"%(s,l))
print(type(s))
print(type(l))
