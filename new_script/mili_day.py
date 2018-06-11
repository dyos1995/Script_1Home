import platform
import os
if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

from tkinter import *
from tkinter import font
import tkinter.messagebox
import Pasing_mili
import naver_api

x_value = 400
y_value = 480

x_value_1 = 800
y_value_1 = 80

window = Tk()
window.geometry("1620x600+50+300")

army_case = 0 # 1번 육군 2번 해군 3번 공군 4번 해병대 5번 의경
Datalist = []

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
        d_year =int(d_year)
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
    font1 = font.Font(window, size=10, weight="bold", family="맑은 고딕")

    l1 = Label(window, text="입대 년도을  입력하세요.", font=font1)
    l1.place(x= x_value - 350, y = y_value - 330)

    e1 = Entry(window)
    e1.place(x= x_value - 200,  y=y_value - 330)

    l2 = Label(window, text="입  대  월을  입력하세요.", font=font1)
    l2.place(x=x_value - 350, y=y_value - 300)

    e2 = Entry(window)
    e2.place(x=x_value - 200, y=y_value - 300)

    l3 = Label(window, text="입  대  일을  입력하세요.", font=font1)
    l3.place(x=x_value - 350, y= y_value - 270)

    e3 = Entry(window)
    e3.place(x=x_value - 200, y=y_value - 270)


def enter_case1():
    font2 = font.Font(window, size=10, weight="bold", family="맑은 고딕")
    global e4
    b1 = Button(window, text='확인', command=Plus_day)
    b1.place(x=x_value - 150, y=y_value - 245)

    l4 = Label(window, text="입대일을 확인하세요.", font=font2)
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
    font3 = font.Font(window, size=11, weight="bold", family="한컴 윤고딕 240")
    result1 = Label(window, text="일병 예정일", font=font3)
    result1.place(x=x_value-300, y=y_value-160)

    result1_e = Entry(window)
    result1_e.place(x=x_value - 180, y=y_value - 160)
    result1_e['bg'] = "yellow"

    # 일병 진급일
    result2 = Label(window, text="상병  진급일", font=font3)
    result2.place(x=x_value-300, y=y_value - 130)

    result2_e = Entry(window)
    result2_e.place(x=x_value - 180, y=y_value - 130)
    result2_e['bg'] = "yellow"

    # 상병 진급일
    result3 = Label(window, text="병장  진급일", font=font3)
    result3.place(x=x_value - 300, y=y_value - 100)

    result3_e = Entry(window)
    result3_e.place(x=x_value - 180, y=y_value - 100)
    result3_e['bg'] = "yellow"

    # 병장 진급일
    result4 = Label(window, text="전역  예정일", font=font3)
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
    picture_mili() # 사진 넣기
    enter_result() # 결과 창
    next_button() # 다음으로 넘어가기

# =========================== 검색하기
def InitTopText_pasing():
    TempFont_1 = font.Font(window, size = 20, weight = 'bold', family = 'Consloas')
    MainText_1 = Label(window, font = TempFont_1, text = "[ 맞춤형 특기 검색 ]")
    MainText_1.pack()
    MainText_1.place(x=800, y = 10)

def RenderText_Rend():
    global RenderText

    RenderTextba = Scrollbar(window)
    RenderTextba.pack()
    RenderTextba.place(x = x_value_1, y = y_value_1)

    TempFont = font.Font(window, size = 10, family = 'Consolas')
    RenderText = Text(window, width = 49, height = 30, borderwidth = 12, relief = 'ridge', yscrollcommand=RenderTextba.set)
    RenderText.pack()
    RenderText.place(x=x_value_1, y=y_value_1+70)
    RenderTextba.configure(command=RenderText.yview)
    RenderTextba.pack(side=RIGHT, fill=BOTH)
    #RenderText.configure(state='disabled')


def spend_data():
    global Datalist
    print("입력")
    Datalist = Pasing_mili.Search_item(str(m1e.get()))

    if (len(Datalist) != 0):
        print("데이터 출력")
        RenderText.delete("1.0", END)
        for i in range(len(Datalist)):
            RenderText.insert(INSERT, "---------------------------")
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i+1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "군명 : ")
            RenderText.insert(INSERT, Datalist[i][1])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "전공명: ")
            RenderText.insert(INSERT, Datalist[i][2])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "군사특기명: ")
            RenderText.insert(INSERT, Datalist[i][0])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "---------------------------")
            RenderText.insert(INSERT,"\n\n")
        print("데이터 출력 완료")
        print("------------------")


def enter_mili_date():
    global m1e
    m1 = Label(window, text = "전공 / 자격증을 입력하세요")
    m1.place(x = x_value_1, y = y_value_1)

    m1e = Entry(window)
    m1e.place(x = x_value_1+5, y = y_value_1+20)

    m1b = Button(window, text = "완료",command = spend_data)
    m1b.place(x = x_value_1+150, y = y_value_1+15)

def create_world_2():
    Pasing_mili.readytPasing()
    InitTopText_pasing() # 상단 맞춤형 특기 찾기
    enter_mili_date() # 전공 / 과명 적기
    RenderText_Rend() # 목록 출력

# =========================== 병과 검색하기
def InitTopText_pasing_2():
    TempFont_2 = font.Font(window, size = 20, weight = 'bold', family = 'Consloas')
    MainText_2 = Label(window, font = TempFont_2, text = "[ 병무청 위치 ]")
    MainText_2.pack()
    MainText_2.place(x=1200, y = 10)

def spend_data_1():
    naver_data = naver_api.Search_txt(str(m2e.get()))
    RenderText_2.delete("1.0", END)
    for i in range (len(naver_data)):
        RenderText_2.insert(INSERT, "--------------")
        RenderText_2.insert(INSERT,"\n")
        RenderText_2.insert(INSERT,"기관명 : ")
        RenderText_2.insert(INSERT,naver_data[i][0])
        RenderText_2.insert(INSERT,"\n")
        RenderText_2.insert(INSERT,"전화번호 : ")
        RenderText_2.insert(INSERT,naver_data[i][1])
        RenderText_2.insert(INSERT,"\n")
        RenderText_2.insert(INSERT,"주소 : ")
        RenderText_2.insert(INSERT,naver_data[i][2])
        RenderText_2.insert(INSERT,"\n")
        RenderText_2.insert(INSERT,"상세주소 : ")
        RenderText_2.insert(INSERT,naver_data[i][3])
        RenderText_2.insert(INSERT, "\n")
        RenderText_2.insert(INSERT, "--------------")
        RenderText_2.insert(INSERT,"\n\n")


def enter_mili_date_3():
    global m2e
    m2 = Label(window, text = "지역명을 작성해주세요")
    m2.place(x = x_value_1 + 400, y = y_value_1)

    m2e = Entry(window)
    m2e.place(x = x_value_1+405, y = y_value_1+20)

    m2b = Button(window, text = "완료",command = spend_data_1)
    m2b.place(x = x_value_1+550, y = y_value_1+15)


def RenderText_Rend_2():
    global RenderText_2

    RenderTextba_2 = Scrollbar(window)
    RenderTextba_2.pack()
    RenderTextba_2.place(x = x_value_1 + 400, y = y_value_1)

    TempFont = font.Font(window, size = 10, family = 'Consolas')
    RenderText_2 = Text(window, width = 49, height = 10, borderwidth = 12, relief = 'ridge', yscrollcommand=RenderTextba_2.set)
    RenderText_2.pack()
    RenderText_2.place(x=x_value_1 + 400, y=y_value_1+50)
    RenderTextba_2.configure(command=RenderText.yview)
    RenderTextba_2.pack(side=RIGHT, fill=BOTH)

def picture_image():
    photo_1 = PhotoImage(file="강한육군.gif")  # 디폴트 이미지 파일
    imageLabel_2 = Label(window, image=photo_1)
    imageLabel_2.configure(image=photo_1)
    imageLabel_2.image = photo_1
    imageLabel_2.place(x=1190, y=300)

def create_world_3():
    InitTopText_pasing_2() # 상단 맞춤형 특기 찾기
    enter_mili_date_3() # 병과 입력
    RenderText_Rend_2() # text
    picture_image()

def main():
    create_world()
    create_world_2()
    create_world_3()

    window.mainloop()


if __name__ == '__main__':
    main()


