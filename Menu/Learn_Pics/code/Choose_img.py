import random

class Random_Img:
    def __init__(self, element_list: list):
        self.element_list = element_list

    
    def sort_img(self, category):
        result = random.choice(self.element_list[category])
        return result