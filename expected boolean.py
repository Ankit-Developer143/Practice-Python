def reverse(arg):
    if isinstance(arg,bool):
        if arg == True:
            return False
        else:
            return True
    else:
        return "Boolean Expected"
print(reverse(True))