from tkinter import * # tkinter 모듈에서 모든클래스를 import
import random # random 모듈 import


score = 0 # 점수를 표기하는 score 변수 초기화
def move_Right(event): # 오른쪽방향키 입력시, 동작하는 함수
    global user # user 객체를 global 선언
    global userPosition # user의 위치를 저장할 변수 global 선언
    global score # 점수를 global 선언
    canvas.delete(user) # 움직임을 표현하기 위해 이전의 user객체를 지워줌
    global x1,y1,x2,y2 # user객체의 좌표
    x1 = x1 + 1 # x1좌표를 +1움직여줌
    x2 = x2 + 1 # x2좌표를 +1움직여줌  = 같은모양이 되면서, 움직이는것처럼 표현됨
    #print(x1)
    user = canvas.create_oval(x1,y1,x2,y2,fill='blue') # 움직인 후의 user 객체를 oval class를 이용해 그려줌(원)
    #print(yb_list)
    userPosition = canvas.coords(user) # 유저객체의 위치를 돌려받는 coords를 활용,각 좌표가 4개의 배열로나옴[x1,y1,x2,y2]
    print(userPosition) # 움직여진 user객체의 좌표 확인
    for i in range(len(yb_list)): # 생성된 공의 개수만큼 반복하면서 (yb_list에는 생성된 공의 객체들이 저장되어있음)
        if (userPosition[2] == ybPosition_list[i][0]) \
                and ((userPosition[1]+userPosition[3])/2 > ybPosition_list[i][1]) and\
                ((userPosition[1]+userPosition[3])/2 < ybPosition_list[i][3]):
            canvas.delete(yb_list[i]) # user객체의 가장오른쪽 x좌표가 생성된 공의 가장왼쪽 x좌표와 같을때
                                      # and user객체의 y좌표 두점의 중앙이 생성된공의 y제일 아래 좌표보다 클때
                                      # and user객체의 y좌표 두점의 중앙이 생성된공의 y제일 위쪽 좌표보다 작을때
                                      # 해당 index의 생성된 공 객체가 지워진다.
            score += 1 # 점수를 1 더해줌
    l1 = Label(window, width=40, text='score: ' + str(score))
    l1.grid(row=0, column=0, columnspan=5) # 더해진점수를 다시 label에 표시
    if score == len(yb_list): # 생성된 공 전부 제거시 clear 출력 기능추가
        l1 = Label(window, width=40, text='clear!')
        l1.grid(row=0, column=0, columnspan=5)




def move_Left(event): # 왼쪽 방향키 입력시 동작하는 함수
    global user # user 객체를 global 선언
    global score # 점수를 global 선언
    canvas.delete(user)  # 움직임을 표현하기 위해 이전의 user객체를 지워줌
    global x1,y1,x2,y2 # user객체의 좌표
    x1 = x1 - 1 # x1좌표를 -1해주고 다시 대입 -> 왼쪽으로 이동시켜줌
    x2 = x2 - 1 # x2좌표를 -1해주고 다시 대입 -> 왼쪽으로 이동시켜줌
    #print(x1)
    user = canvas.create_oval(x1,y1,x2,y2,fill='blue') # 움직인 후의 user 객체를 oval class를 이용해 그려줌(원)
    userPosition = canvas.coords(user) # 유저객체의 위치를 돌려받는 coords를 활용,각 좌표가 4개의 배열로나옴[x1,y1,x2,y2]
    print(userPosition) # 움직여진 user객체의 좌표 확인

    for i in range(len(yb_list)): # 생성된 공의 개수만큼 반복하면서 (yb_list에는 생성된 공의 객체들이 저장되어있음)
        if (userPosition[0] == ybPosition_list[i][2]) \
                and ((userPosition[1]+userPosition[3])/2 > ybPosition_list[i][1])\
                and ((userPosition[1]+userPosition[3])/2 < ybPosition_list[i][3]):
            canvas.delete(yb_list[i])  # user객체의 가장왼쪽 x좌표가 생성된 공의 가장 오른쪽 x좌표와 같을때
                                      # and user객체의 y좌표 두점의 중앙이 생성된공의 y제일 아래 좌표보다 클때
                                      # and user객체의 y좌표 두점의 중앙이 생성된공의 y제일 위쪽 좌표보다 작을때
                                      # 해당 index의 생성된 공 객체가 지워진다.
            score += 1 # 점수를 1 더해줌
    l1 = Label(window, width=40, text='score: ' + str(score))
    l1.grid(row=0, column=0, columnspan=5)  # 더해진점수를 다시 label에 표시
    if score == len(yb_list): # 생성된 공 전부 제거시 clear 출력 기능추가
        l1 = Label(window, width=40, text='clear!')
        l1.grid(row=0, column=0, columnspan=5)


def move_Up(event): # 위쪽 방향키 입력시 동작하는 함수
    global user # 모든 방향키에 대해 같음
    global score # "
    canvas.delete(user) # "
    global x1,y1,x2,y2 # "
    y1 = y1 - 1 # y1에 -1해준값을 다시 y1에 넣어주어, 위로 움직이는것 표현
    y2 = y2 - 1 # "
    #print(y1)
    user = canvas.create_oval(x1,y1,x2,y2,fill='blue') # 위로 움직여진 좌표로 다시 user를 그려줌
    userPosition = canvas.coords(user)  # 유저객체의 위치를 돌려받는 coords를 활용,각 좌표가 4개의 배열로나옴[x1,y1,x2,y2]
    print(userPosition) # 움직여진 user객체의 좌표 확인

    for i in range(len(yb_list)): # 생성된 공의 개수만큼 반복하면서 (yb_list에는 생성된 공의 객체들이 저장되어있음)
        if (userPosition[1] == ybPosition_list[i][3]) \
                and ((userPosition[0]+userPosition[2])/2 > ybPosition_list[i][0])\
                and ((userPosition[0]+userPosition[2])/2 < ybPosition_list[i][2]):
            canvas.delete(yb_list[i]) # user객체의 가장위쪽 y좌표가 생성된 공의 가장 아래쪽 y좌표와 같을때
                                      # and user객체의 x좌표 두점의 중앙이 생성된공의 x좌표 가장 왼쪽보다 클때
                                      # and user객체의 x좌표 두점의 중앙이 생성된공 x좌표의 가장 오른쪽보다 작을때
                                      # 해당 index의 생성된 공 객체가 지워진다.
            score += 1 # 점수를 1더해줌
    l1 = Label(window, width=40, text='score: ' + str(score)) # 더해준 score표시
    l1.grid(row=0, column=0, columnspan=5)
    if score == len(yb_list): # clear 출력화면 추가
        l1 = Label(window, width=40, text='clear!')
        l1.grid(row=0, column=0, columnspan=5)


def move_Down(event): # 아래 방향키를 눌렀을때 동작하는 함수
    global user # 위와같음
    global score
    canvas.delete(user)
    global x1,y1,x2,y2
    y1 = y1 + 1 # 아래로 가는것을 표현하기 위해 좌표를 다시 설정해줌
    y2 = y2 + 1
    #print(y1)
    user = canvas.create_oval(x1,y1,x2,y2,fill='blue') # 새로 대입된 좌표를 이용해 user 객체 다시 그려줌
    userPosition = canvas.coords(user)
    print(userPosition)

    for i in range(len(yb_list)):  # 생성된 공의 개수만큼 반복하면서 (yb_list에는 생성된 공의 객체들이 저장되어있음)
        if (userPosition[3] == ybPosition_list[i][1]) \
                and ((userPosition[0]+userPosition[2])/2 > ybPosition_list[i][0])\
                and ((userPosition[0]+userPosition[2])/2 < ybPosition_list[i][2]):
            canvas.delete(yb_list[i]) # user객체의 가장아래쪽 y좌표가 생성된 공의 가장 위쪽 y좌표와 같을때
                                      # and user객체의 x좌표 두점의 중앙이 생성된공의 x좌표 가장 왼쪽보다 클때
                                      # and user객체의 x좌표 두점의 중앙이 생성된공 x좌표의 가장 오른쪽보다 작을때
                                      # 해당 index의 생성된 공 객체가 지워진다.
            score += 1 # 위와같음음
    l1 =Label(window, width=40, text='score: ' + str(score))
    l1.grid(row=0, column=0, columnspan=5)
    if score == len(yb_list):
        l1 = Label(window, width=40, text='clear!')
        l1.grid(row=0, column=0, columnspan=5)




yb_list = [] # 생성된공의 객체를 저장하는 변수
ybPosition_list = [] # 생성된공의 좌표값을 저장하는 변수 (2차원)
def create_ball_click(): # create 버튼클릭시 공을 10개씩 랜덤하게 생성
    global yb # 생성된 공 하나를 가르킴 (yb는 계속변하는 하나의값으로 yb_list에 추가시킴)
    global ybPosition # 생성된공의 좌표를 가르킴
    global score
    for i in range(0,10): # 10번 반복
        x1 = random.randint(0, 300) # 랜덤위치를 저장
        y1 = random.randint(0, 200) # 랜덤위치를 저장
        yb = canvas.create_oval(x1, y1, x1 + 10, y1 + 10, fill='yellow') # 크기가 일정한 노란색공을 생성
        ybPosition = canvas.coords(yb) # yb의 좌표를 저장
        ybPosition_list.append(ybPosition) # yb의 좌표를 리스트에 추가 (2차원)
        yb_list.append(yb) # yb객체를 리스트에 추가
        print(yb_list) # 생성된 객체 확인
        print(ybPosition_list) # 생성된 객체의 좌표확인
    score = 0 # clear 후, create 생성시 score를 다시 0으로 초기화시키기위함



def delete_ball(): # 생성된 공을 전부 삭제
    global score # 점수를 초기화 시키기위해 선언
    for i in range(len(yb_list)): # 생성된 공의 객체의 길이 만큼 반복
        canvas.delete(yb_list[i]) # canvas.delete 를 활용하여 객체를 전부 지워줌
    score = 0 # score 0으로 초기화
    l1 = Label(window, width=40, text='score: ' + str(score)) # 0으로 바뀐 score 다시 label
    l1.grid(row=0, column=0, columnspan=5)

def process1(): # create 버튼을 생성할때 실행되지 않고 process1를 거쳐서 버튼을 눌렀을때 실행되도록 하기위함
    create_ball_click()

def process2(): # delete 버튼을 생성할때 실행되지 않고 process2를 거쳐서 버튼을 눌렀을때 실행되도록 하기위함
    delete_ball()

window = Tk() # 전체를 감싸는 window

l1 = Label(window,width=40,text = 'score: '+ str(score))  # 초기에 프로그램 실행시 score 표시 (0으로 초기화되어있음)
l1.grid(row = 0, column = 0, columnspan=5) # grid 격자모양으로 0,0 위치에

canvas = Canvas(window,width = 300, height = 200) # 그림을 그릴 canvas 객체를 Canvas 클래스로 생성
canvas.grid(row = 3,column = 2) # grid 격자모양으로 3,2위치에

b1 = Button(window,text='Create',command = process1) # create 버튼 객체 생성
b2 = Button(window,text='Delete',command =process2) # delete 버튼 객체 생성

b1.grid(row = 1, column = 2)  # 격자위치 1,2
b2.grid(row = 2, column = 2) # 격자위치 2,2

x1 = 10 # 초기에 유저 객체의 위치설정 및 생성
y1 = 10
x2 = 3*x1
y2 = 3*y1
print(x2,y2)
user = canvas.create_oval(x1,y1,x2,y2, fill='blue')


canvas.focus_set() # 키보드 입력을 받기위해 필요한 메서드
canvas.bind('<Right>',move_Right) # 오른쪽 방향키 입력시 move_Right 함수 실행
canvas.bind('<Left>',move_Left) # 왼쪽 방향키 입력시 move_Left 함수 실행
canvas.bind('<Up>',move_Up) # 위쪽 방향키 입력시 move_Up 함수 실행
canvas.bind('<Down>',move_Down) # 아래쪽 방향키 입력시 move_Down 함수 실행


window.mainloop() # 윈도우창 출력 시키기위해 필요