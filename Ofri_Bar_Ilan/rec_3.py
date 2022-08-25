def merge_sorted_lists(l1, l2):
    if len(l1) == 0 and len(l2) == 0:
        return []

    if len(l1) == 0 and len(l2) > 0:
        return l2

    if len(l2) == 0 and len(l1) > 0:
        return l1

#     l1 and l2 is not empty
    new_l = []
    if l1[0] < l2[0]:
        new_l.append(l1[0])
        merge_lists = merge_sorted_lists(l1[1:], l2)
        return new_l + merge_lists

    if l2[0] < l1[0]:
        new_l.append(l2[0])
        rec = merge_sorted_lists(l1, l2[1:])
        sorted_lists = new_l + rec
        return sorted_lists


print(merge_sorted_lists([], []))  # []

print(merge_sorted_lists([], [1]))  # [1]
print(merge_sorted_lists([3], []))  # [3]
print(merge_sorted_lists([3, 5, 7], []))  # [3, 5, 7]

print(merge_sorted_lists([3], [4]))  # [3, 4]
print(merge_sorted_lists([4], [3]))  # [3, 4]
print(merge_sorted_lists([3,4,5], [6]))  # [3, 4, 5, 6] |||  [3] + m([4, 5], [6]) => [4] + m([5], [6]) => [5] + m([], [6]) => [6]
print(merge_sorted_lists([3,5], [4]))  # [3, 4, 5]

print(merge_sorted_lists([3,5,10], [4,6,7, 8, 9]))  # [3, 4, 5, 6, 7, 8]
