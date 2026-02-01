


import random
lottery=random.randint(10,99)
print(lottery)
guess=eval(input("enter two numbers: "))

lottery_digit1=lottery//10
lottery_digit2=lottery%10


guess_digit1=guess//10
guess_digit2=guess%10

if lottery==guess:
    print("WE HAVE A WINNER!!!!!!!")
elif(lottery_digit1==guess_digit2 and lottery_digit2==guess_digit1 ):
    print("ALMOST!!! YOU HAVE HALF PRICE!!YAAY")
elif(lottery_digit1==guess_digit1 
         or lottery_digit1==guess_digit2
         or lottery_digit2==guess_digit1 
         or lottery_digit2==guess_digit2):
    print("ONE DIGIT MATCH!!WIN 10 CAD")
else:
    print("TRY NEXT TIME")



