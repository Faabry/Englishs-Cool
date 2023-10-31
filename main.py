# Imports
import random
import PySimpleGUI as sg
from PIL import Image, ImageTk

# Função que exibe a imagem
def display_image(element):
    # Diretório da imagem
    img_path = f"img_teste/{element.lower()}.jpeg"
    image = Image.open(img_path)
    # Definir o tamanho da thumbnail para a imagem
    image.thumbnail((273, 350))
    # Inserir a imagem dentro da thumbnail
    image_data = ImageTk.PhotoImage(image)
    # Exibir o nome da imagem
    text = element.title()

    # Atualizar a imagem e o título a ser exibido dinamicamente
    window["-IMAGE-"].update(data=image_data)
    window["-TEXT-"].update(text)

# Função que randomicamente sorteia o elemento da lista desejado
def file_path(lista):
    result = random.choice(lista)
    return result.lower()


# Definindo o tema da interface
sg.theme('Lightblue')

# Lista dos elementos
animals = ["Elephant", "Snake", "Dog", "Cat", "Fish", "Bird",
           "Mouse", "Aligator", "pig", "turtle", "bat", "tiger", 
           "butterfly", "dog "]

places = ["Park", "Supermarket", "Mall", "Restaurant", "Movies",
          "Church", "School", "Work", "Party", "Library",
          "Gas Station", "Bus Stop", "House"]

food = ["Pasta", "Meat", "Ham", "Cheese", "Burger", "Pizza",
        "Ice Cream", "Chocolate", "Vegetables", "Bread",
        "Bacon", "French Fries", "Hot Dog", "sushi", "egg"]

fruits = ["Pear", "Apple", "Banana", "Orange", "Grape", "Lemon",
          "Passion Fruit", "Watermelon", "Melon", "Pineapple",
          "Papaya", "Coconut", "Kiwi", "Mango", "avocado"]

drinks = ["water", "soda", "coffee", "tea", "wine", "juice", 
          "hot chocolate", "milk", "beer"]

objects = ["car", "motorcycle", "cellphone","pen", "drums",
           "violin", "piano", "video game", "dental floss",
           "calculator", "chair"]

verbs = ["to have", "to like", "to sleep", "to want", "to eat",
         "to work", "to go", "to play", "to speak", "to study"]

# ----------------------------------------------------------------

# Layout da interface
layout = [
    [sg.Text("Learn", font=("Bookman 40 bold"), text_color="black"),
     sg.Text("Pics", font=("Bookman 40 bold"),text_color="red")],

    [sg.Text("Choose a category:", font=("Bookman Old Style", 25))],
    
    [sg.Button("Foods", key="-FOOD-", size=(12, 2),
               font=("Bookman Old Style", 12)),
     sg.Button("Places", key="-PLACES-", size=(12, 2),
               font=("Bookman Old Style", 12)),
     sg.Button("Animals", key="-ANIMALS-", size=(12, 2),
               font=("Bookman Old Style", 12)),
     sg.Button("Fruits", key="-FRUITS-", size=(12, 2),
               font=("Bookman Old Style", 12))],
    
    [sg.Button("Drinks", key="-DRINKS-", size=(12, 2),
               font=("Bookman Old Style", 12)),
     sg.Button("Objects", key="-OBJECTS-", size=(12, 2),
               font=("Bookman Old Style", 12)),
     sg.Button("Verbs", key="-VERBS-", size=(12, 2),
               font=("Bookman Old Style", 12)),
     sg.Button("Random", key="-RANDOM-", size=(12, 2),
               font=("Bookman Old Style", 12))],

    [sg.Image(key="-IMAGE-", size=(273, 274)),
     sg.Push(),
     sg.Text("Make a\nsentence\nwith...",
             font=("Bookman Old Style", 35),
             justification="center"), 
     sg.Push()],

    
    [sg.Text("", key="-TEXT-",
             font=("Bookman Old Style", 25),
             justification="right")],
    
    # sg.Button("🔊", font=("Arial", 15), size=(3, 1), key="-PLAY-", pad=(0, 0))],

    [sg.Button("Quit ❎", key="-QUIT-",
               font=("Bookman Old Style", 15),
               size=(21, 3)),
     sg.Push(),
     sg.Image("img_teste/logo1.png")]
]

window = sg.Window("English's Cool Game", layout, 
                   element_padding=(10, 10),
                   location=(250, 0),
                   size=(600, 800))

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "-QUIT-":
        break
    elif event == "-FOOD-":
        random_element = file_path(food)
        display_image(random_element)
    elif event == "-PLACES-":
        random_element = file_path(places)
        display_image(random_element)
    elif event == "-ANIMALS-":
        random_element = file_path(animals)
        display_image(random_element)
    elif event == "-FRUITS-":
        random_element = file_path(fruits)
        display_image(random_element)
    elif event == "-DRINKS-":
        random_element = file_path(drinks)
        display_image(random_element)
    elif event == "-VERBS-":
        random_element = file_path(verbs)
        display_image(random_element)
    elif event == "-OBJECTS-":
        random_element = file_path(objects)
        display_image(random_element)

window.close()



