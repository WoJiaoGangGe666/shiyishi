def idzhishu(a):
    if a==2:
        print('It is not zhishu')

    elif a>2:
        for i in range(2,a):
            if a%i==0:
                print('It is a zhishu:%d=%d*%d'%(a,i,a/i))
                break
        else:
            print('It is not a zhishu.')

    else:
        print('Input error.')


s=int(input('Input a integer >1:'))
idzhishu(s)
