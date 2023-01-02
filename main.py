from art import logo, vs
from game_data import data
from random import randint, choice
from replit import clear

def next_choice():
  return choice(data)

def who_higher(first_person, second_person):
  if first_person["follower_count"] <= second_person["follower_count"]:
    return second_person
  else:
    return first_person
    

def person_info(person):
  return person["name"] + ", a " + person["description"] + " from " + person["country"]
#print()
first = next_choice()
game_over = False
count = 0

def answer(first_person, second_person):
  current_answer = ""
  while current_answer != "A" and current_answer != "B":
    current_answer = input("Who has more followers? Type A or B: ")

  if current_answer == "A":
    return first_person
  else:
    return second_person
  

while not game_over: 

  clear()
  print(logo)
  second = next_choice()
  if count > 0:
    print(f"You are right! Current score is: {count}")
  print(f"Compare A:{person_info(first)}")
  print(vs)
  print(f"Against B:{person_info(second)}")

  if answer(first,second) == who_higher(first,second):
    first = second
    count += 1
  else:
    game_over = True

clear()
print(logo)
print(f"Sorry. You are mistake. Score is {count}")