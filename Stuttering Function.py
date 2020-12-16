def stutter(word):
    return ( word[0:2]+"... ")*2+(word)+"?"
print(stutter("enthusiastic"))

#op:-en... en... enthusiastic?

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
    
'''op
1 2 3 4 
5 6
7 8 9'''



