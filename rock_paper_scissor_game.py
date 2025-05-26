import random

u_choice = int(input("Type 0 for Rock, 1 for Paper, and 2 for Scissor: "))
sys_choice = random.randint(0, 2)
choices = ["Rock", "Paper", "Scissor"]
if u_choice == 0 and sys_choice == 1:
    print(f"You chose {choices[u_choice]}, Computer chose {choices[sys_choice]}")
    print("You Loose!")

elif u_choice == 1 and sys_choice == 2:
    print(f"You chose {choices[u_choice]}, Computer chose {choices[sys_choice]}")
    print("You Loose!")

elif u_choice == 2 and sys_choice == 0:
    print(f"You chose {choices[u_choice]}, Computer chose {choices[sys_choice]}")
    print("You Loose!")

elif u_choice == sys_choice:
    print(f"You chose {choices[u_choice]}, Computer chose {choices[sys_choice]}")
    print("It's a Draw!")

else:
    print(f"You chose {choices[u_choice]}, Computer chose {choices[sys_choice]}")
    print("You WIN!!")