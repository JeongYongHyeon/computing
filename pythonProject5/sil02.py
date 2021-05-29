from turtle import* # 사용할 turtle모듈을 import* 로 전부 사용할 수 있게됨
import random # random 모듈 import
class Ball: # Ball class 선언
    def __init__(self,color,size,speed): # 생성자 (색, 사이즈, 속도) 입력받음

        speed_list = [-speed,speed] # x,y의 증가 방향을 +,- 로 random하게 선택할 수 있게 함
        speed1 = random.choice(speed_list) # 랜덤선택
        speed2 = random.choice(speed_list) # 랜덤선택

        self.xspeed = speed1 # x의 증가
        self.yspeed = speed2 # y의 증가
        self.c = random.uniform(-3,3)
        self.wall = 300
        self.a = self.xspeed
        self.b = self.c * self.yspeed




        self.size = size # parameter로 받은 size를 생성한 객체에 저장
        self.color = color # parameter로 받은 color를 생성한 객체에 저장

        self.turtle = Turtle() # Turtle()함수를 self.turtle 객체에 저장
        self.turtle.shape('circle') # 객체의 모양 설정
        self.turtle.color(color,color) # 객체의 turtle.color를 이용하여 색설정
        self.turtle.resizemode('user') # resizemode는 user로 정의
        self.turtle.shapesize(size, size, 10) # 입력받은 parameter로 size를 설정




    def move(self): # 실제 움직이는 메서드


        self.x += self.a # x의 좌표가 xspeed만큼 더해져 나간다.
        self.y += self.b # y의 좌표가 yspeed만큼 더해져 나간다.
        self.turtle.goto(self.x,self.y) # 바뀌어 가는 x,y좌표로 움직여감

        if (self.x > self.wall) & (self.y > 0):  # x가 오른쪽 벽에 닿았을때 y가 0보다 클경우

            self.tmp = self.a
            self.a = -self.b
            self.b = self.tmp
            print(self.tmp,self.a,self.b)

        elif (self.x > 300) & (self.y < 0):  # x가 오른쪽 벽에 닿았을때 y가 0보다 작을경우
            self.tmp = self.a
            self.a = -self.b
            self.b = self.tmp

        elif (self.x < -300) & (self.y > 0):  # x가 왼쪽 벽에 닿았을때 y가 0보다 클경우
            self.tmp = self.a
            self.a = -self.b
            self.b = self.tmp
        elif (self.x < -300) & (self.y < 0):  # x가 왼쪽 벽에 닿았을때 y가 0보다 작을경우
            self.tmp = self.a
            self.a = -self.b
            self.b = self.tmp
        elif (self.y > 300) & (self.x > 0):  # y가 위쪽 벽에 닿았을때 x가 0보다 큰경우
            self.tmp = self.a
            self.a = self.b
            self.b = -self.tmp
        elif (self.y > 300) & (self.x < 0):  # y가 위쪽 벽에 닿았을때 x가 0보다 작을경우
            self.tmp = self.a
            self.a = self.b
            self.b = -self.tmp
        elif (self.y < -300) & (self.x > 0):  # y가 아래쪽 벽에 닿았을때 x가 0보다 큰경우
            self.tmp = self.a
            self.a = self.b
            self.b = -self.tmp
        elif (self.y < -300) & (self.x < 0):  # y가 아래쪽 벽에 닿았을때 x가 0보다 작을경우
            self.tmp = self.a
            self.a = self.b
            self.b = self.tmp


ball = Ball('red',1,1) # Ball클래스의 color를 'red'로 size를 1로 speed를 1로 갖는 ball인스턴스를 생성

ball.turtle.penup() # ball객체의 turtle함수를 이용하여 펜을올림
ball.wall = 300 # 벽을 그림 (크기 300)
ball.turtle.goto(-ball.wall, -ball.wall) # x=-300,y=-300 으로 이동
ball.turtle.pendown() # 펜을 놓고 그림 그릴 준비함
for i in range(4): # 4번 반복
    ball.turtle.fd(ball.wall * 2)  # 600만큼 앞으로가고
    ball.turtle.left(90) # 90도 왼쪽회전을 반복하여 벽을그림
ball.turtle.penup() # 펜을 다시 올림

ball.x = random.randint(-ball.wall,ball.wall) # x의 좌표 벽안에서 랜덤설정
ball.y = random.randint(-ball.wall,ball.wall) # y의 좌표 벽안에서 랜덤설정

ball.turtle.pendown()
 # 경로를 보여주기 위해 다시 펜을 내림

while True: # 무한반복문
    ball.move() # ball객체의 move메서드를 불러옴
    #print(ball.x,ball.y) # 좌표를 실시간으로 확인
