print("Input the three nums:")
a=float(input("Input a=:"))
b=float(input("Input b=:"))
c=float(input("Input c=:"))

delta=b**2-4*a*c
if delta>=0:
    x1=-b/(2*a)+delta**0.5/(2*a)
    x2=-b/(2*a)-delta**0.5/(2*a)
    print("the two real roots are:\nx1=%.3f\nx2=%.3f"%(x1,x2))

else:
    x1=complex(-b/(2*a),(-delta)**0.5/(2*a))
    x2=complex(-b/(2*a),-(-delta)**0.5/(2*a))
    print("The two false roots are:")
    print("%.2f+%.3fj"%(x1.real,x1.imag))
    print("%.2f-%.3fj" % (x2.real, -x2.imag))
