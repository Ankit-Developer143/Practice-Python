"""[print(i*"*") for i in range(10,1,-1)]

**********
*********
********
*******
******
*****
****
***
** """ 

for i in range(1,10):
    for j in range(10,i,-1):
        print(" ",end=' ')
    for k in range(1,i):
            print(" # ", end=' ')
    print("  ")

"""              #
               #   #
             #   #   #
           #   #   #   #
         #   #   #   #   #
       #   #   #   #   #   #
     #   #   #   #   #   #   #
   #   #   #   #   #   #   #   # """
    


