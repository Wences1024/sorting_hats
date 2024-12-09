import random
import keyboard as kb
import time

class Sorting:
    def __init__(self):
        #Create the list with the name of the houses
        self.houses = ["Hufflepuff","Gryffindor","Ravenclaw","Slytherin"]
	
    def House_Selection(self):
        #Return randomly any string of the list
        return self.houses[random.randint(0,len(self.houses)-1)]


if __name__=="__main__":
    #Create the object
    Hat = Sorting()
    #Print the line for the first time
    print(f"The house you belong to is: {Hat.House_Selection()}")
    #Now you get into the loop
    while True:
        #Check if the "space" bar is pressed
        if kb.is_pressed("space"):
            #Display the house
            print(f"La casa que el sombrero me asigno fue: {Hat.House_Selection()}")
            #Wait until you release the space bar
            time.sleep(1)
            #Check if escape button is pressed to end the loop and the program
        if kb.is_pressed("esc"):
            break
        
        