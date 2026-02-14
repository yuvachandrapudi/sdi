def fun(a,b):
    try:
        a=int(a)
        b=int(b)
        result=a/b
        sum=a+b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")    
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
    return result,sum

a=input("Enter a:")
b=input("Enter b:")
result,sum=fun(a,b)
print("Sum:", sum)
