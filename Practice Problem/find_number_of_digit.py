def find_number_of_digit(n):
   if n == 0:
       return 0
   return 1 + find_number_of_digit(n//10)
print(find_number_of_digit(14545))
