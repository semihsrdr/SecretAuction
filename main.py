def clear():  # Prints 50 blank lines
    print("\n" * 50)


def select_winner(data):
    winner=""
    winner_offer=0
    for key,value in data.items():
        if value>winner_offer:
            winner=key
            winner_offer=value
    print()
    print("The winner is "+winner.capitalize()+" by "+str(winner_offer)+"$.")
    print()
    print("You can see all offers on the below")
    print("-------------------------------------------------------------------")
    for key,value in data.items():
        print(key,":",str(value)+"$")
        print()

people = {}
print("Welcome to the Secret Auction Program.")
while True:
    name = input("What's your name?: ")
    offer = int(input("What's your offer?: "))
    people.update({name: offer})
    clear()
    another_else=input("Is there any another person to give offer(yes, no): ")
    if another_else.lower()=="no":
        select_winner(people)

        break

