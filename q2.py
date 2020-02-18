print("<<< Display the second largest number in a List >>>")
listn=[5,15,17,8,89,56,47,39,89,11,89]
print("list : ",listn)
max_element=max(listn)
for max_element in listn:
    listn.remove(max_element)
print("Second largest number : ",max(listn))
