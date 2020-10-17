
user_play = "y"

start_number = 0

while user_play == "y":

    user_number = input("How many numbers? ")
    
    for i in range(start_number, int(user_number) + start_number):

        print(i)

    start_number = start_number + int(user_number)

    user_play = input("Continue the chain: (y)es or (n)o? ")
