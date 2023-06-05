import math
def trisum(a,b,c):
    #identify whether it is a triangle?
    if(a+b+c-max(a,b,c)>max(a,b,c)):
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        return(area)
    else:
        return('error')

a=float(input('The first line:'))
b=float(input('The second line:'))
c=float(input('The third line:'))
s=trisum(a,b,c)
print(type(s))
print('The area is:%.3f'%(s))
