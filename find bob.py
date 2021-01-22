def find_bob(names):
    try:

        ele = "Bob"
        val = names.index(ele)
        return val
    except:
        return -1
print(find_bob(["Jimmy", "Layla"]))
#op:- -1