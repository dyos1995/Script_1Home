from tkinter import *
from tkinter import font
import tkinter.messagebox
import military_count

window = Tk()
window.geometry("800x600+750+200")

x_value = 400
y_value = 480

def InitTopText():
    TempFont = font.Font(window, size = 20, weight = 'bold', family = 'Consloas')
    MainText = Label(window, font = TempFont, text = "[ Military personnel help Service ]")
   # MainText.pack()
    MainText.place(x=200, y = 10)



def create_world():
    InitTopText() # 제목


def main():

    military_count.main()

    window.mainloop()

if __name__ == '__main__':
    main()

