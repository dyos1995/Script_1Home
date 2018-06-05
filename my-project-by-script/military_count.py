from tkinter import *
from tkinter import font
import menu
import tkinter.messagebox


x_value = 400
y_value = 480

window = Tk()
window.geometry("800x600+750+200")

army_case = 0 # 1번 육군 2번 해군 3번 공군 4번 해병대 5번 의경

def InitTopText():
    TempFont = font.Font(window, size = 20, weight = 'bold', family = 'Consloas')
    MainText = Label(window, font = TempFont, text = "[ 군 전역일 계산 ]")
    MainText.pack()
    MainText.place(x=300, y = 10)


def Plus_day():
    d_year = e1.get()
    d_month =e2.get()
    d_day = e3.get()

    one_star = 0
    two_star = 0
    three_star = 0
    four_star = 0

    one_star_year = 0
    two_star_year = 0
    three_star_year = 0
    four_star_year = 0


    e4.delete(0, 100)

    if(e1.get() == '' or e2.get() == '' or e3.get() == ''):

        e4.insert(0, "오류 재입력")

    else:
        d_year = int(d_year)
        d_month = int(d_month)
        d_day = int(d_day)

        if (d_year < 100):
            d_year += 2000

        if (d_day < 1 or d_day > 31):
            e4.insert(0, "날짜 오류 재입력")
        elif (d_month < 1 or d_month > 12):
            e4.insert(0, "달 오류 재입력")
        else:
            plus_day = str(d_year) + '.' + str(d_month) + '.' + str(d_day)
            e4.insert(0, plus_day)

            one_star_year = int(d_year)

            if(army_case == 1): # 육군
                one_star = int(d_month) + 3
                if(one_star > 12):
                    one_star_year = int(d_year) + 1
                    one_star = one_star % 12

                two_star = one_star + 7
                two_star_year = one_star_year
                if (two_star > 12):
                    two_star_year = one_star_year + 1
                    two_star = two_star % 12

                three_star = two_star + 7
                three_star_year = two_star_year
                if (three_star > 12):
                    three_star_year = two_star_year + 1
                    three_star = three_star % 12

                four_star = three_star + 4
                four_star_year = three_star_year
                if (four_star > 12):
                    four_star_year = three_star_year + 1
                    four_star = four_star % 12

            elif (army_case == 2):  # 해군
                one_star = int(d_month) + 6
                if (one_star > 12):
                    one_star_year = int(d_year) + 1
                    one_star = one_star % 12

                two_star = one_star + 6
                two_star_year = one_star_year
                if (two_star > 12):
                    two_star_year = one_star_year + 1
                    two_star = two_star % 12

                three_star = two_star + 7
                three_star_year = two_star_year
                if (three_star > 12):
                    three_star_year = two_star_year + 1
                    three_star = three_star % 12

                four_star = three_star + 4
                four_star_year = three_star_year
                if (four_star > 12):
                    four_star_year = three_star_year + 1
                    four_star = four_star % 12

            elif (army_case == 3):  # 공군
                one_star = int(d_month) + 3
                if (one_star > 12):
                    one_star_year = int(d_year) + 1
                    one_star = one_star % 12

                two_star = one_star + 7
                two_star_year = one_star_year
                if (two_star > 12):
                    two_star_year = one_star_year + 1
                    two_star = two_star % 12

                three_star = two_star + 7
                three_star_year = two_star_year
                if (three_star > 12):
                    three_star_year = two_star_year + 1
                    three_star = three_star % 12

                four_star = three_star + 7
                four_star_year = three_star_year
                if (four_star > 12):
                    four_star_year = three_star_year + 1
                    four_star = four_star % 12




            result1_e.delete(0,100)
            result2_e.delete(0, 100)
            result3_e.delete(0, 100)
            result4_e.delete(0, 100)


            #일병 계산
            plus_1_day = str(one_star_year) + '.' + str(one_star) + '.' + '01'
            result1_e.insert(0, plus_1_day)

            #상병 계산
            plus_2_day = str(two_star_year) + '.' + str(two_star) + '.' + '01'
            result2_e.insert(0, plus_2_day)

            #병장 계산
            plus_3_day = str(three_star_year) + '.' + str(three_star) + '.' + '01'
            result3_e.insert(0, plus_3_day)

            #전역일
            day_l = int(d_day - 1)
            plus_4_day = str(four_star_year) + '.' + str(four_star) + '.' + str(day_l)
            result4_e.insert(0, plus_4_day)


def Clear():
    e1.delete(0,100)
    e2.delete(0,100)
    e3.delete(0,100)
    e4.delete(0,100)


def enter_case():
    global e1, e2, e3
    l1 = Label(window, text="입대년도을  입력하세요.", font='helvetica 10 italic')
    l1.place(x= x_value - 350, y = y_value - 330)

    e1 = Entry(window)
    e1.place(x= x_value - 200,  y=y_value - 330)

    l2 = Label(window, text="입  대  월을  입력하세요.", font='helvetica 10 italic')
    l2.place(x=x_value - 350, y=y_value - 300)

    e2 = Entry(window)
    e2.place(x=x_value - 200, y=y_value - 300)

    l3 = Label(window, text="입  대  일을  입력하세요.", font='helvetica 10 italic')
    l3.place(x=x_value - 350, y= y_value - 270)

    e3 = Entry(window)
    e3.place(x=x_value - 200, y=y_value - 270)


def enter_case1():
    global e4
    b1 = Button(window, text='확인', command=Plus_day)
    b1.place(x=x_value - 150, y=y_value - 245)

    l4 = Label(window, text="입대일을 확인하세요.", font='helvetica 11 italic')
    l4.place(x=x_value - 350, y=y_value - 210)

    e4 = Entry(window)
    e4.place(x=x_value - 180, y= y_value - 210)
    e4['bg'] = "pink"


def picture_mili():
    global imageLabel
    global inputBox
    global stay_army

    photo = PhotoImage(file="국방부.gif")  # 디폴트 이미지 파일
    imageLabel = Label(window, image=photo)
    imageLabel.configure(image = photo)
    imageLabel.image = photo
    imageLabel.place(x= 400, y = 100)

    select_army = Label(window, text = "소속 - 육군 / 해군 / 공군 / 해병대" )
    select_army.place(x = 80, y = 85)

    inputBox = Entry(window)
    inputBox.place(x = 80, y = 110)

    button = Button(window, text = '클릭', command = change_image)
    button.place(x = 230, y = 106)

    stay_army = Entry(window)
    stay_army.place(x = 600, y = 70)


def enter_case2():
    global e5
    b1 = Button(window, text='초기화', command=Clear)
    b1.place(x=x_value - 100, y=y_value - 245)


def enter_result():
    # 전역 예정일
    global result1_e
    global result2_e
    global result3_e
    global result4_e

    result1 = Label(window, text="일병 예정일", font='helvetica 11 italic')
    result1.place(x=x_value-300, y=y_value-160)

    result1_e = Entry(window)
    result1_e.place(x=x_value - 180, y=y_value - 160)
    result1_e['bg'] = "yellow"

    # 일병 진급일
    result2 = Label(window, text="상병 진급일", font='helvetica 11 italic')
    result2.place(x=x_value-300, y=y_value - 130)

    result2_e = Entry(window)
    result2_e.place(x=x_value - 180, y=y_value - 130)
    result2_e['bg'] = "yellow"

    # 상병 진급일
    result3 = Label(window, text="병장 진급일", font='helvetica 11 italic')
    result3.place(x=x_value - 300, y=y_value - 100)

    result3_e = Entry(window)
    result3_e.place(x=x_value - 180, y=y_value - 100)
    result3_e['bg'] = "yellow"

    # 병장 진급일
    result4 = Label(window, text="전역 예정일", font='helvetica 11 italic')
    result4.place(x=x_value - 300, y=y_value - 70)

    result4_e = Entry(window)
    result4_e.place(x=x_value- 180, y=y_value- 70)
    result4_e['bg'] = "yellow"

def change_image():
    global army_case
    path = inputBox.get()
    if(inputBox.get() == ''):
        inputBox.insert(0, "작성 오류")

    if(inputBox.get() == "공군"):
        army_case = 3
        stay_army.delete(0,10)
        stay_army.insert(0,"24개월")

    elif(inputBox.get() == "해군"):
        army_case = 2
        stay_army.delete(0,10)
        stay_army.insert(0, "23개월")

    else:
        army_case = 1
        stay_army.delete(0,10)
        stay_army.insert(0, "21개월")


    path += '.gif'
    imag = PhotoImage(file = path)
    imageLabel.configure(image=imag)
    imageLabel.image = imag


def next_button():
    next_button = Button(window, text='이전화면')
    next_button.place(x = 310, y = 450)


def create_world():
    global e1, e2, e3, e4
    InitTopText() # 제목
    enter_case()  # 년 월 일 입력
    enter_case1() # 버튼 - 확인 / 출력
    enter_case2() # 버튼 - 초기화
    #picture_mili() # 사진 넣기
    enter_result() # 결과 창
    next_button() # 다음으로 넘어가기



def main():
    create_world()
    window.mainloop()


if __name__ == '__main__':
    main()


