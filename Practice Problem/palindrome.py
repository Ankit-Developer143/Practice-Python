#A palindrome is a word, number, or any string of characters which reads the same backward as it reads forward.

number = int(input()); 

reverse = 0
temp = number

while number > 0: 

    digit = number % 10

    reverse = reverse * 10 + digit 

    number = number // 10

if temp==reverse:

    print("it is a palindrome!")

else:

    print("it is not a palindrome!")

#     1001
# it is a palindrome!