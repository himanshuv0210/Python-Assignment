list1=[10,30,20]
list2=[15,5,60]
list3=list()
print("Given List 1 : ",list1)
print("Given List 2 : ",list2)
for i in range(0,len(list1)):
    list3.append(list1[i])
for j in range(0,len(list2)):
    list3.append(list2[j])
print("Merge list : ",list3)
def sorting(arr):
    i=0
    j=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1):
             if arr[j]>arr[j+1]:
                 arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)
print('List after sorting')
sorting(list3)

    
