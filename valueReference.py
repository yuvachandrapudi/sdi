def m1(a):
    print("Address of A inside m1:", id(a))
    a.append(40)
    print("Address of A after modification inside m1:", id(a))
    print("Value of A inside m1:", a)

x=[10,20,30]
print("Address of X before calling m1:", id(x))
print("Value of X before calling m1:", x)
m1(x)