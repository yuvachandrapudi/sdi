# #Design an algorithm to accept 10 integer elements for an array and print the sum of all the elements
# arr = []
# sum=0
# for i in range(10):
#     arr.append(int(input()))
#     sum+=arr[i]
# print(sum)

# # Design an algorithm to accept 20 integer elements for an array and print the maximum 3 and minimum 3 elements from the array. 
# # Note: Sorting of array elements are not expected as part of this activity.
# arr = []
# for i in range(20):
#     arr.append(int(input()))

# max1 = max2 = max3 = float('-inf')
# min1 = min2 = min3 = float('inf')

# for num in arr:
#     if num > max1:
#         max3 = max2
#         max2 = max1
#         max1 = num
#     elif num > max2:
#         max3 = max2
#         max2 = num
#     elif num > max3:
#         max3 = num

#     if num < min1:
#         min3 = min2
#         min2 = min1
#         min1 = num
#     elif num < min2:
#         min3 = min2
#         min2 = num
#     elif num < min3:
#         min3 = num

# print(max1, max2, max3)
# print(min1, min2, min3)

# #Design an algorithm to accept 10 integer elements for an array and then rearrange the elements in the array in reverse order. The reversed array must be displayed as output.
# arr = []
# for i in range(10):
#     arr.append(int(input()))
# arr.reverse()
# print(arr)

# Activity 4: 
# Design an algorithm which accepts a set of N (consider N to be 30) student’s examination marks (in the range of 0 to 100). Then make a count of the number of students that obtain each possible mark (i.e.; 
# count of how many students scored 0, count of how many students scored 1, …. till count of how many students scored 100) 
# marks = []
# print("enter marks of 30 students")
# for i in range(30):
#     marks.append((int(input())))

# count = [0] * 101
# for m in marks:
#     count[m] += 1

# for i in range(101):
#     print("no of students scored ",i, count[i])

# Activity 5: 
# Modify the algorithm written in Activity 4 in order to get count of students in a specific range of marks as defined below. 
# Range of marks: 
# 0 to 10% 
# 11% to 20% 
# ; 
# ; 
# ; 
# 91% to 100%

# marks = []
# for i in range(30):
#     marks.append(int(input()))

# ranges = [0] * 10

# for m in marks:
#     if m == 100:
#         ranges[9] += 1
#     else:
#         ranges[m // 10] += 1

# for i in range(10):
#     print("students between  ",i*10,"and",(i+1)*10,ranges[i])


# Activity 6: 
# Design an algorithm to calculate the factorial of a number N. The value of N is provided as an input by the user. 
# n = int(input("Enter number:"))
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)

# Activity 7: 
# # Design an algorithm which accepts 10 integer values, calculates the average and prints it.

# arr = []
# sum=0
# for i in range(10):
#     arr.append(int(input()))
#     sum+=arr[i]
# print("Average:",sum / 10)

# Activity 8: 
# A train running at the speed of x km/hr crosses a pole in y seconds. Design an algorithm to accept x and y as inputs from the user and then calculate the length of the train. 
# Note: values of x and y must be positive and non-zero. 

# x = float(input("Enter speed in km/hr:"))
# y = float(input("enter time in sec:"))
# length = (x * 1000 / 3600) * y
# print(length)

# Activity 9: 
# A train X m long passes a man, running at 5 km/hr in the same direction in which the train is going, in Y seconds. Design an algorithm to accept the values of X and Y as input from the user and then calculate the speed of the train. 
#Note: values of X and Y must be positive and non-zero.

# X = float(input("length of train in m:"))
# Y = float(input("time in seconds:"))
# relative_speed = X / Y
# train_speed = relative_speed * 3.6 + 5
# print("Train speed:",train_speed)

# Activity 10: 
# # Two goods train each 500 m long, are running in opposite directions on parallel tracks. Their speeds are X km/hr and Y km/hr respectively. Design an algorithm to accept the values of speed X and Y from the user and find the time taken by the slower train to pass the driver of the faster one. 
# # Note: values of X and Y must be positive and non-zero 

# X = float(input("Speed of 1st train in km/hr:"))
# Y = float(input("Speed of 2nd train in km/ph:"))
# slower = min(X, Y)
# time = 500 / (slower * 1000 / 3600)
# print(time)
