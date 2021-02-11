import random

rock = '''
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

#logic for user's choice
choice1 = int(input("What do you choose? Tyep 0 for Rock, 1 for Paper and 2 for Scissors\n"))

if choice1 == 0:
  print(rock)
elif choice1 == 1:
  print(paper)
elif choice1 == 2:
  print(scissors)
else: 
  print("Wrong choice")

#logic for cmputer's choice
choice2 = random.randint(0,1)

print(f"Computer choose {choice2}")

if choice2 == 0:
  print(rock)
elif choice2 == 1:
  print(paper)
elif choice2 == 2:
  print(scissors)
else: 
  print("Wrong choice")

#logic for game
if choice1 == choice2:
  print("Draw!!, try again!")

elif choice1 == 0 and choice2 == 2:
  print("You win!!")
elif choice1 == 2 and choice2 == 1:
  print("You Win!!")
elif choice1 == 1 and choice2 == 0:
  print("You Win")
else:
  print("Computer Winssssss")

# elif choice1 == 0:
#   if choice2 == 1:
#     print("You win!!")
#   else:
#     print("Computer win!!")

# elif choice1 ==  1:
#   if choice2 == 2:
#     print("You win!!")
#   else:
#     print("Computer win!!")


 

