a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
a,b,c=c,a,b
print("After swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

# This program takes three integers as input and swaps their values in a circular manner.
count=0
arr=[80,50,26]
for i in arr:
    if arr[i]>35:
        count+=1
print("Number of students cleared exam:",count)

# This program counts how many students scored more than 35 marks.
non_neg=0
neg=0

arr=[0]*5
for i in range(len(arr)):
    arr[i]=int(input("Enter numbers:"))
    if arr[i]>0:
        non_neg+=1
    else:
        neg+=1
print("Number of non-negative numbers:",non_neg)
print("Number of negative numbers:",neg)

# This program counts the number of non-negative and negative integers from user input.

num=int(input("Enter a number:"))
if num%2==0:
    print("Even number")
else:
    print("Odd number")

# This program checks if a number is even or odd.

arr=[12,47,55]
sum=0
for i in arr:   
    sum+=i
print("Sum of array elements:",sum)


data=["India","USA","UK","java"]