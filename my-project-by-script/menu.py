from tkinter import *
from tkinter import font
import tkinter.messagebox
import military_count

window = Tk()
window.geometry("800x600+750+200")

x_value = 400
y_value = 480

def InitTopText():
    global TempFont
    global MainText

    TempFont = font.Font(window, size = 20, weight = 'bold', family = 'Consloas')
    MainText = Label(window, font = TempFont, text = "[ Military personnel help Service ]")
    #MainText.pack()
    MainText.place(x=200, y = 10)

def create_world():
    InitTopText() # 제목

def button_3():
    photo = PhotoImage(file = "국방부.gif")
    iLabel = Label(window, image = photo)
    iLabel.pack()

    b1 = Button(window, text = "밀   리   데   이", font ='helvetica 14 italic')
    b1.place(x=50, y = 150)
    b2 = Button(window, text = " 맞춤  특기  찾기 ",font ='helvetica 14 italic')
    b2.place(x=50, y = 250)
    b3 = Button(window, text = "    종      료   ",font ='helvetica 14 italic')
    b3.place(x=50, y = 350)

def main():
    InitTopText()
    button_3()
    #military_count.main()

    window.mainloop()

if __name__ == '__main__':
    main()
