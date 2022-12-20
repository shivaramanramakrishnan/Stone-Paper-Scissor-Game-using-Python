stone = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

choice = int(input("What do you choose? Type 0 for Stone, 1 for Paper or 2 for Scissors.\n"))
game = [stone, paper, scissors]

print(game[choice])
comp = random.randint(0,2)
print("\nComputer chose:\n")
print(game[comp])

if choice == comp:
  print("You draw")
elif choice==0 and comp==1:
  print("You lose")
elif choice==0 and comp==2:
  print("You win")
elif choice==1 and comp==0:
  print("You win")
elif choice==1 and comp==2:
  print("You lose")
elif choice==2 and comp==0:
  print("You lose")
elif choice==2 and comp==1:
  print("You win")


