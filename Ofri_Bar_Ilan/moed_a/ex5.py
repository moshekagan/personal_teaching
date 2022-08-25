list1 = list()
list1.append([1, 2, 3])
list2 = list1
list2.extend([1, 2, 3])

print(list1)
print(list2)
print(list1 == list2 and list1 is list2)