a = input("Enter Your Number: ")
my_list =[a]
while True:
    b = input("Do You Want to Enter more input press y/n: ")
    if b == 'y':
        more_input = input("Enter another Number : ")
        my_list.append(more_input)
    elif b == 'n':
        break
my_list.sort(reverse = True)
print(my_list)

#['5', '4']

        
    
