import random
import keyboard as kb
import time

class Sorting:
    def __init__(self):
        self.houses = ["Hufflepuff","Gryffindor","Ravenclaw","Slytherin"]
	
    def House_Selection(self):
        return self.houses[random.randint(0,len(self.houses)-1)]


if __name__=="__main__":
    Hat = Sorting()
    print(f"La casa que el sombrero me asigno fue: {Hat.House_Selection()}")
    while True:
        if kb.is_pressed("space"):
            print(f"La casa que el sombrero me asigno fue: {Hat.House_Selection()}")
            time.sleep(1)
        if kb.is_pressed("esc"):
            break
        
        