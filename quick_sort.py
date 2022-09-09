import copy
def quick_sort(arr,first,last):  
    i = copy.deepcopy(first)
    j = copy.deepcopy(last)
    pivot = i
    if first < last :
        while i < j :
            while arr[i] <= arr[pivot] and i < last :
                i += 1
            while arr[j] > arr[pivot] :
                j -= 1
            if i > j :
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        temp = arr[pivot]
        arr[pivot] = arr[j]
        arr[j] = temp
        
        quick_sort(arr,0,pivot-1)
        quick_sort(arr,pivot+1,last)
    # print(first,last)

a = int(input("Enter total number for a list : "))
l = []
for i in range(0,a) :
    temp = int(input("Enter {} number : ".format(i+1)))
    l.append(temp)
j = len(l) - 1
quick_sort(l,0,j)
print("Sorted list is : {}".format(l))

