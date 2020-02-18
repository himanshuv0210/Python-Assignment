print("<<< Put the even and odd numbers into different list >>>")
num=[1,2,3,4,5,6,7,8,9,10]
print("Original list : ",num)
even=list()
odd=list()
for i in range(0,len(num)):
    if(num[i]%2==0):
        even.append(num[i])
    else:
        odd.append(num[i])
print("Even list : ",even)
print("Odd list : ",odd)
