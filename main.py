from time import sleep
from  tkinter import Canvas , Button ,PhotoImage , Tk

from pandas import read_csv
BACKGROUND_COLOR = "#B1DDC6"

with open("./data/french_words.csv") as data:
    n = -1
    dicts = read_csv(data)
    words_fr_en= dicts.to_dict(orient="list")
def fun():
    global n

    n += 1
    canvas.itemconfig(language, text  = "French")
    canvas.itemconfig(words, text=f"{words_fr_en["French"][n]}")
    window.after(3000,fun_1 )

def fun_1():
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(words, text=f"{words_fr_en["English"][n]}")

window = Tk()
window.config(bg=BACKGROUND_COLOR)
window.title("Learning French")

card_back = PhotoImage(file="./images/card_back.png")
card_front= PhotoImage(file="./images/card_front.png")
wrong = PhotoImage(file="./images/wrong.png")
right = PhotoImage(file="./images/right.png")

canvas = Canvas(window,width= 800 , height=524, bg= BACKGROUND_COLOR)
canvas.create_image(400,262 ,image = card_front )

language =  canvas.create_text(400, 160, text =f"French", fill="black", font=("Helvetica", 50, "bold"))
words = canvas.create_text(400, 280, text =f"{words_fr_en["French"][0]}", fill="black", font=("Helvetica", 40, "bold"))
fun()
canvas.grid(row=0 , column= 0,columnspan=2)
button_right = Button(image = right , highlightthickness = 0 , command=fun )
button_right.grid(row=1 , column= 0)

button_wrong = Button(image = wrong , highlightthickness = 0 , command=fun )
button_wrong.grid(row=1 , column= 1)


window.mainloop()