def filter_list(lst):
    
    for i in lst[:]:
        if isinstance(i,int) == False:
            lst.remove(i)
    return lst


print(filter_list([1, 2,"a"]))

# op:- [1, 2]
