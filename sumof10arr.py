def sum(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum

for i in range(10):
    arg[i]=int(input("Enter numbers:"))
result=sum(arg)
print("Sum of array elements:",result)

#Design an algorithm to accept 20 integer elements for an array and print the maximum 3 and minimum 3 elements from the array. 
#Note: Sorting of array elements are not expected as part of this activity. 

def find_max_min(arr):
    max_elements = []
    min_elements = []
    for num in arr:
        if len(max_elements) < 3:
            max_elements.append(num)
            max_elements.sort(reverse=True)
        elif num > max_elements[-1]:
            max_elements[-1] = num
            max_elements.sort(reverse=True)

        if len(min_elements) < 3:
            min_elements.append(num)
            min_elements.sort()
        elif num < min_elements[-1]:
            min_elements[-1] = num
            min_elements.sort()

    return max_elements, min_elements

arr = [int(input("Enter numbers:")) for _ in range(20)]
max_elements, min_elements = find_max_min(arr)
print("Maximum 3 elements:", max_elements)
print("Minimum 3 elements:", min_elements)

#Design an algorithm to accept 10 integer elements for an array and then rearrange the elements in the array in reverse order. The reversed array must be displayed as output. 
def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

arr = [int(input("Enter numbers:")) for _ in range(10)]
reversed_arr = reverse_array(arr)
print("Reversed array:", reversed_arr)

