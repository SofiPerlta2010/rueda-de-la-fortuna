from tkinter import * 

import random 

root=Tk()

root.title("Rueda de la fortuna") 
root.geometry("500x500") 

list1 = ["Ana", "Luna", "Victor", "Gabi", "Vicky", "Xime", "Bella", "Vany", "Rebeca", "Majo", "Vale"] 
print(list1) 

def random_number(): 
  random_no = random.randint(0, 11) 
  print(random_no) 
  random_lucky_friend = list1[random_no] 
  print("tu amigo afortunado es: " + random_lucky_friend) 

btn1 = Button(root, text="¿Quién es tu amigo afortunado? ", command = random_number)  btn1.place (relx= 0.5,rely = 0.5, anchor = CENTER)

root.mainloop()