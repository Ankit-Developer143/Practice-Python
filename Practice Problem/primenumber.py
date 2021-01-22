num = int(input("Enter Your Number "))
flag = True
for i in range(2,num):
    if(num%i == 0):
        flag = False
if(flag == True):
    print("This is prime number")
    
else:
    print("This is not prime number")



# Enter Your Number 13
# This is prime number


for i in range(1,100):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)


""" 2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97 """