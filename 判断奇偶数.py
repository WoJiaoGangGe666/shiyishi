def idnum(s):
    if s%2==0:
        print('%d is integer'%s)
    else:
        print('%d is not integer'%s)


print('input q to quit.')
while 1:
    a=input('Input a num:')
    if a=='q':
        break
    idnum(int(a))
