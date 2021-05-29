import random # random 모듈을 import한다.

class R_S_P_user(): # R_S_P_user 클래스를 선언한다.

    choiceRSP = [] # field, 최종 리턴값이 된다.

    def __init__(self,prob): # 생성자

        #self.RSP = None
        self.prob = prob # 초기 주먹,가위,보 의 확률을 설정
        self.prob_list = [] # 입력된 확률값을 split 으로 나눠 prob_list 리스트에 저장
        self.RSP_list = [] # 입력된 확률에 100을 곱한값을 각각 리스트에 추가시켜 구현하기 위한 리스트

    def choice(self): # 가위바위보 선택


        self.prob_list = self.prob.split() # 입력된 확률값을 split으로 나눠 저장
        rock_number = int(float(self.prob_list[0])*100) # 주먹의 개수, 확률값에 100을 곱해 int형으로 변환시킨값을 대입
        scissors_number = int(float(self.prob_list[1])*100) # 가위의 개수, 확률값에 100을 곱해 int형으로 변환시킨값을 대입
        paper_number = int(float(self.prob_list[2])*100) # 보의 개수, 확률값에 100을 곱해 int형으로 변환시킨값을 대입
        for i1 in range(rock_number): # 주먹의 개수만큼 반복
            self.RSP_list.append('Rock') # 실제 주먹,가위,보 뽑을 리스트에 주먹의 개수만큼 'Rock'을 추가
        for i2 in range(scissors_number): # 가위의 개수만큼 반복
            self.RSP_list.append('Scissors') # 실제 주먹,가위,보 뽑을 리스트에 주먹의 개수만큼 'Scissors'을 추가
        for i3 in range(paper_number): # 보의 개수만큼 반복
            self.RSP_list.append('Paper') # 실제 주먹,가위,보 뽑을 리스트에 주먹의 개수만큼 'Paper'을 추가
        #print(self.RSP_list) # 잘 추가 되었는지 확인
        self.choiceRSP = random.choice(self.RSP_list) # RSP_list에서 랜덤으로 주먹,가위,보 중 하나가 선택됨

    def get_RSP(self): # 여기서 가위 바위 보 가져옴 멤버변수 직접적 접근 허용 x, 함수로 접근하도록
        return self.choiceRSP

while True: # 무한반복문
    n = int(input('1.게임시작 2.유저생성 3.종료: ')) # n의 값에 따라 게임시작, 유저생성, 종료
    if n == 1: # n은 1일때 가위바위보 시작
        print('가위 바위 보 게임을 시작합니다.')
        user1.choice() # class를 이용하여, R_S_P_user 클래스의 choice함수를 이용하여 가위 바위 보 선택
        user2.choice() # class를 이용하여, R_S_P_user 클래스의 choice함수를 이용하여 가위 바위 보 선택
        print('유저 1: ',user1.get_RSP()) # 가위 바위 보 중 선택된것 출력
        print('유저 2: ',user2.get_RSP()) # 가위 바위 보 중 선택된것 출력
        print('--------------------------')
        if user1.get_RSP() == user2.get_RSP(): # 가위 바위 보 승리를 판단하기 위한 if 문들
            print('유저1: draw 유저2: draw')
        elif (user1.get_RSP() == 'Rock') & (user2.get_RSP() == 'Scissors'):
            print('유저1: win 유저2: lose')
        elif (user1.get_RSP() == 'Rock') & (user2.get_RSP() == 'Paper'):
            print('유저1: lose 유저2: win')
        elif (user1.get_RSP() == 'Scissors') & (user2.get_RSP() == 'Rock'):
            print('유저1: lose 유저2: win')
        elif (user1.get_RSP() == 'Scissors') & (user2.get_RSP() == 'Paper'):
            print('유저1: win 유저2: lose')
        elif (user1.get_RSP() == 'Paper') & (user2.get_RSP() == 'Rock'):
            print('유저1: win 유저2: lose')
        elif (user1.get_RSP() == 'Paper') & (user2.get_RSP() == 'Scissors'):
            print('유저1: lose 유저2: win')

    if n == 2: # n이 2이면, 확률을 입력받아 R_S_P_user의 instance를 생성, user1,user2 객체 생성

        prob1 = input('유저 1의 확률을 입력해주세요: ') # user1의 확률을 입력받음
        prob2 = input('유저 2의 확률을 입력해주세요: ') # user2의 확률을 입력받음
        user1 = R_S_P_user(prob1) # R_S_P_user의 instance를 생성, user1,user2 객체 생성
        user2 = R_S_P_user(prob2)

    if n == 3: # n이 3이면 반복문 종료
        break


