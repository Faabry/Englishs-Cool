import random
import os
from PIL import Image
from time import sleep

def file_path(lista):
     result = random.choice(lista)
     return result.lower()


animals = ["Elefant", "Snake", "Dog", "Cat", "Fish", "Bird",
         "Mouse", "Aligator"]

places = ["Park", "Supermarket", "Mall", "Restaurant", "Movies"
          "church", "school", "work", "party", "library", "gas station", "bus stop", "house"]

food = ["Pasta", "Meat", "Ham", "Cheese", "Burguer", "pizza", 
        "Ice Cream", "Chocolate", "Vegetables", "bread", "bacon", "french fries", "hot dog"]

fruits = ["pear", "apple", "banana", "orange", "grape", "lemon",
          "passion fruit", "watermelon", "melon", "pineapple", "papaya", "coconut", "kiwi", "mango"]


random_element = ""

os.system("cls")

print("-" * 20)
choice = int(input("Choose the option\n" +
               "1- Food\n" +
               "2- Places\n" +
               "3- Animals\n" +
               "4- Fruits\n>>> "))
print("-" * 20)

if choice == 1:
    random_element = file_path(food)
elif choice == 2:
    random_element = file_path(places)
elif choice == 3:
    random_element = file_path(animals)
elif choice == 4:
    random_element = file_path(fruits)
else:
    print("Choose another valid option")

print("MAKE")
sleep(1)
print("A")
sleep(1)
print("SENTENCE")
sleep(1)
print("WITH ...")


img = Image.open(f"images/{random_element}.jpeg")
img.show()
