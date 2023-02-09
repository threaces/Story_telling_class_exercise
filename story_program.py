# -*- coding: utf-8 -*-
"""Story_program.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jR34bv7Sd5jYtF0TbA75VI6HV2_P3jaD
"""

import random

class Room():

  def __init__(self, room_name):
    self.room_name = room_name
    self.backpack = Backpack()

  def welcome_message(self):
    message = f'Welocme in {self.room_name}'
    return message

  def get_access_to_room(self):

    with open('riddle.txt', 'r') as file:
      print(file.readlines())

    user_answer = input("Please provide answer on riddle ").lower()
    if user_answer == 'jutro':
      print("Congratulation. You broke a spell. You can go inside")
    else:
      print("Password is wrong. Try again")

  def room(self):

    list_of_items = ['Rozdzka', 'Latajaca Miotla', 'Peleryna Niewidka', 'Zaby w czekoladzie', 'Kamien filozoficzny', 'Miecz']
    list_of_user_items = []

    list_of_commends()

    while True:
      user_option = input(f"What do you want to do? ")
      user_option.title()

      if user_option == 'Take':
        user_item = input(f"Which item from the list do you want to take? {list_of_items} ").title()
        if user_item not in list_of_items:
          print("This item is not in the room")
        else:
          print("You took a item successfully")
          function = self.backpack.take_item()
          user_eq = list_of_items.remove(user_item)
          list_of_user_items.append(user_item)
          print(f"You have {function[0]} free slots in your backpack")
      elif user_option == 'Use':
        if len(list_of_user_items) == 1:
          print(f"You will use {list_of_user_items[0]}")
        elif len(list_of_user_items) > 1:
          random_item = random.choice(list_of_user_items)
          print(f"You will use {random_item}")
      elif user_option == 'Check':
        self.backpack.check_slots()
        print(f"{list_of_user_items}")
      elif user_option == 'Describe':
        room_description()
      elif user_option == 'Stop':
        break

class Backpack():

  def __init__(self):
    self.amount_slots = 3
    self.counter_slots = 0

  def take_item(self):
    if self.amount_slots < 0:
      print('You cant take more items. Please remove something from your backpack')
    else:
      self.counter_slots += 1
      self.amount_slots -= 1
   
    return (self.amount_slots, self.counter_slots)

  def check_slots(self):
    print(f"You have {self.amount_slots} free slots and {self.counter_slots} blocked slots")

def list_of_commends():
  print('Take - take a item\nUse - use item from your backpack\nCheck - check amount of free slots\nList - list of commands\nDescribe - Description of room\nStop - finish exploring a room')


def room_description():

  with open('room_description.txt', 'r') as file:
    text_value = file.readlines()
    
    for line in text_value:
      line = line.replace('\n', '')
      print(line)

def game():

  room1 = Room('Pokoj magiczny')
  print(room1.welcome_message())
  room1.get_access_to_room()
  room1.room()

game()