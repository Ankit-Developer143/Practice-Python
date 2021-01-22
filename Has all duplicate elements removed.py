def unique_sort(lst):
    lst = set(lst)
    lst = list(lst)
    lst.sort()
    return lst
print(unique_sort([1, 2, 4, 3,2]))

#op:-[1, 2, 3, 4]