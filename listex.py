list1 = [1,6,3,2,1,4,5,3]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)