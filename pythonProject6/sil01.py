import random # 원하는 분포의 데이터를 생성해주기 위한 random 모듈 import
import matplotlib.pyplot as plt # 그래프를 ploting해주기위한 모듈 import

class clsAvgFilter: # 평균필터를 수행하는 클래스
    k = 1 # 들어오는 데이터를 1부터 순서대로 하나씩 늘려나가기 위한 파라미터, 평균필터 계산에도 이용
    prevAvg = 0 # 초기 이전의 평균값 = 0; 평균필터 계산에 적용

    def __init__(self, k = 1, prevAvg = 0): # 생성자, 처음 class가 호출되면, k=1이고, 이전의 평균값은 0임
        self.k = k # k의 값을 생성된 객체에 저장하기 위함
        self.prevAvg = prevAvg # 이전의 평균값을 생성된 객체에 저장하기 위함

    def AvgFilter(self, xn): # 실제 평균필터 계산하는 메서드
        alpha = (self.k - 1) / self.k # 알파는 k-1/k
        avg = alpha * self.prevAvg + (1 - alpha) * xn # 반환되는 평균값은 alpha * 이전의 평균값 + (1-alpha) * 현재들어오는데이터

        self.k += 1 # k가 하나씩 더해나감 (들어오는 데이터의 개수만큼)
        self.prevAvg = avg # 이전의 평균값 변수에 현재 계산된 평균값을 저장해줌으로써, 다음 계산에 사용

        return avg
        # 계산된 avg값을 리턴

class clsMovAvgFilter: # 이동평균필터 계산하는 클래스
    def __init__(self, numOfData, prevAvg = 0): # 생성자 초기 이동평균필터 객체가 생성되면,
                                                # 계산에 사용할 데이터개수를 지정해주어야함, 이전의 평균값은 디폴트 0
        self.xBuf = []  # buffer
        #self.oBuf = [0.0, 0.0]
        self.firstRun = 1 # firstrun은 처음 객체 생성될때 1로 초기화 -> (이전평균값 없이 첫동작일때 1)
        self.index = 0 # index는 처음 객체 생성될때 0으로 초기화
        self.numOfData = numOfData # 초기 객체 생성시 지정한 numofdata를 생성한 객체에 저장
        self.prevAvg = prevAvg # 이전의 평균값, 생성한 객체에 저장
        if self.prevAvg != 0:               # (이전의 평균값이 0이 아닌경우)초기에 이전의 평균값을 주는 경우 버퍼에 채움
            for i in range(self.numOfData): # 계산에 사용할 데이터 개수, 초기 지정한 범위만큼 반복
                self.xBuf.append(self.prevAvg) # 버퍼에 이전의 평균값을 추가
            self.index = 0 # 이전의 평균값이 0이 아닌경우 -> 인덱스 0저장
            self.firstRun = 0 # 이전의 평균값이 0이 아닌경우 -> firstrun 0저장 -> (이전평균값이 있을때 0)

    def MovAvgFilter(self, xn): # 이동평균필터 수행하는 메서드
        if self.firstRun == 1:          # (이전의 평균값이 0인 경우)초기에 평균값을 주지 않고 측정값이 바로 들어 오는 경우 모든 버퍼를 채운다.
            for i in range(self.numOfData): # 계산에 사용할 데이터 개수, 초기 지정한 범위만큼 반복
                self.xBuf.append(xn) # 버퍼에 입력 데이터값 집어넣음
            avg = xn # 리턴할 평균값은 들어오는 데이터값이 그대로 나오게됨
            self.firstRun = 0 # 전부 수행하고 난후, firstrun = 0 초기화
            self.index = 1 # index = 1 저장
        else:
            # calculate moving average, 이동 평균을 계산한다.
            avg = self.prevAvg + (xn - self.xBuf[self.index]) / self.numOfData # 이동평균필터 실제 계산부분
            # 평균값 = 이전의 평균값 + (들어오는 현재 데이터값 - 이전평균의 가장오래된 데이터(버퍼에 저장된 index변수 번째 데이터)/계산에 사용할 데이터 개수)
            # index 변수 = 0 -> 이전평균의 가장 오래된 데이터가됨
            # store new one
            self.xBuf[self.index] = xn # 버퍼의 index변수 번째 인덱스에 현재 들어온 데이터 저장
            # index adjustment
            self.index += 1 # index변수 하나씩 증가
            self.index %= self.numOfData    # index adjustment with round robin style

        self.prevAvg = avg # 이전평균값에 구해진 avg저장

        return avg
        # 구해진 avg값 리턴

class ClsLowPassFilter: # 저역통과필터 수행하는 클래스 생성
    alpha = 0.97 # alpha의 값을 0.97 상수로둔다.
    def __init__(self, alpha=0.97 ,prevAvg = 0): # 생성자, 객체 생성되면,  alpha 0.97을 생성된 객체에 저장하고,
                                                 # 이전의평균값 디폴트는 0으로 두고, 입력을 받는다.
        self.prevAvg = prevAvg # 이전의 평균값을 생성된 객체에 저장
        self.alpha = alpha # alpha값을 생성된 객체에 저장


    def LowPassFilter(self,xn): # lowpass filter 수행하는 메서드

        est = self.alpha * self.prevAvg + (1-self.alpha) * xn # 추정값 = alpha * 이전평균값 + (1-alpha)
        self.prevAvg = est # 이전평균값에 구한 추정값 저장
        return est # 구한 추정값 return

n_list = [] # 랜덤분포로 생성한 데이터 저장할 리스트
i_list = [] # 생성된 샘플 수를 저장할 리스트
avg_list = [] # 평균필터로 계산된 데이터 저장할 리스트
Mavg_list = [] # 이동평균필터로 계산된 데이터 저장할 리스트
LowPass_list = [] # 저역통과 필터로 계산된 데이터 저장할 리스트

avg1 = clsAvgFilter() # 평균필터 객체생성
Mavg1 = clsMovAvgFilter(10) # 이동평균필터 객체생성
Lowpass1 = ClsLowPassFilter() # 저역통과필터 객체생성
n = input('랜덤분포를 선택하세요: ') # 3가지 랜덤분포중 하나를 선택하기 위한 입력
if n == 'gaussian': # 가우시안분포 선택시

    for i in range(100): # n_samples 의 가우시안 랜덤분포 데이터 생성
        xn = random.gauss(10,10) # xn은 mean: 0 std: 5 의 가우시안랜덤분포 데이터
        avg = avg1.AvgFilter(xn) # 생성된 입력데이터마다 평균필터수행
        Mavg = Mavg1.MovAvgFilter(xn) # 생성된 입력데이터마다 이동평균필터수행
        Lowpass = Lowpass1.LowPassFilter(xn) # 생성된 입력데이터마다 저역통과필터수행
        n_list.append(xn) # 생성된 데이터 추가해가며 저장
        i_list.append(i) # sample 의 개수만큼 1부터 추가해가며 저장 (1~nsamples)
        avg_list.append(avg) # 평균필터 결과 추가해가며 저장
        Mavg_list.append(Mavg) # 이동평균필터 결과 추가해가며 저장
        LowPass_list.append(Lowpass) # 저역통과 필터 결과 추가해가며 저장

    print(LowPass_list)
    print(n_list)

    fig = plt.figure() # subplot을 하기위한 객체 생성
    ax1 = fig.add_subplot(2,1,1) # 첫번째 plot 설정
    ax2 = fig.add_subplot(2,1,2) # 두번째 plot 설정

    # 첫번째 plot
    ax1.plot(i_list,n_list,label='Data')    # X축: 1~nsamples, y축: 생성된데이터
    ax1.plot(i_list,avg_list,label='Average filter')   # X축: 1~nsamples, y축: 평균필터결과
    ax1.plot(i_list,Mavg_list,label='Moving average filter')  # X축: 1~nsamples, y축: 이동평균필터결과
    ax1.plot(i_list,LowPass_list,label='Lowpass filter')  # X축: 1~nsamples, y축: 저역통과필터결과

    ax1.legend(prop={'size':4}) # 각데이터 label 표시

    # 두번째 plot
    # 히스토그램 표시하기위한 ploting

    ax2.hist(n_list, bins=200, density=True, histtype='step', label=r'random.normal(0, $1^2$)', color='C0')
    ax2.hist(avg_list, bins=200, density=True, histtype='step', label=r'random.normal(0, $1^2$)', color='C1')
    ax2.hist(Mavg_list, bins=200, density=True, histtype='step', label=r'random.normal(0, $1^2$)', color='C2')
    plt.show()

elif n == 'random': # random.random() 분포 선택시

    # 생성되는 데이터를 제외하고는 과정같음
    for i in range(100):
        xn = random.random()  # -1부터 1까지의 uniform분포 데이터 생성
        avg = avg1.AvgFilter(xn)
        Mavg = Mavg1.MovAvgFilter(xn)
        Lowpass = Lowpass1.LowPassFilter(xn)  # 생성된 입력데이터마다 저역통과필터수행
        n_list.append(xn)
        i_list.append(i)
        avg_list.append(avg)
        Mavg_list.append(Mavg)
        LowPass_list.append(Lowpass)  # 저역통과 필터 결과 추가해가며 저장

    fig = plt.figure()  # subplot을 하기위한 객체 생성
    ax1 = fig.add_subplot(2, 1, 1)  # 첫번째 plot 설정
    ax2 = fig.add_subplot(2, 1, 2)  # 두번째 plot 설정

    # 첫번째 plot
    ax1.plot(i_list, n_list, label='Data')  # X축: 1~nsamples, y축: 생성된데이터
    ax1.plot(i_list, avg_list, label='Average filter')  # X축: 1~nsamples, y축: 평균필터결과
    ax1.plot(i_list, Mavg_list, label='Moving average filter')  # X축: 1~nsamples, y축: 이동평균필터결과
    ax1.plot(i_list, LowPass_list, label='Lowpass filter')  # X축: 1~nsamples, y축: 저역통과필터결과

    ax1.legend(prop={'size': 4})  # 각데이터 label 표시

    # 두번째 plot
    # 히스토그램 표시하기위한 ploting

    ax2.hist(n_list, bins=200, density=True, histtype='step', label=r'random.normal(0, $1^2$)', color='C0')
    ax2.hist(avg_list, bins=200, density=True, histtype='step', label=r'random.normal(0, $1^2$)', color='C1')
    ax2.hist(Mavg_list, bins=200, density=True, histtype='step', label=r'random.normal(0, $1^2$)', color='C2')
    ax2.hist(LowPass_list, bins=200, density=True, histtype='step', label=r'random.normal(0, $1^2$)', color='C2')
    plt.show()



elif n == 'uniform': # uniform 분포 선택시

    # 생성되는 데이터를 제외하고는 과정같음
    for i in range(100):
        xn = random.uniform(-1,1) # -1부터 1까지의 uniform분포 데이터 생성
        avg = avg1.AvgFilter(xn)
        Mavg = Mavg1.MovAvgFilter(xn)
        Lowpass = Lowpass1.LowPassFilter(xn)  # 생성된 입력데이터마다 저역통과필터수행
        n_list.append(xn)
        i_list.append(i)
        avg_list.append(avg)
        Mavg_list.append(Mavg)
        LowPass_list.append(Lowpass)  # 저역통과 필터 결과 추가해가며 저장

    fig = plt.figure()  # subplot을 하기위한 객체 생성
    ax1 = fig.add_subplot(2, 1, 1)  # 첫번째 plot 설정
    ax2 = fig.add_subplot(2, 1, 2)  # 두번째 plot 설정

    # 첫번째 plot
    ax1.plot(i_list, n_list, label='Data')  # X축: 1~nsamples, y축: 생성된데이터
    ax1.plot(i_list, avg_list, label='Average filter')  # X축: 1~nsamples, y축: 평균필터결과
    ax1.plot(i_list, Mavg_list, label='Moving average filter')  # X축: 1~nsamples, y축: 이동평균필터결과
    ax1.plot(i_list, LowPass_list, label='Lowpass filter')  # X축: 1~nsamples, y축: 저역통과필터결과

    ax1.legend(prop={'size': 4})  # 각데이터 label 표시

    # 두번째 plot
    # 히스토그램 표시하기위한 ploting

    ax2.hist(n_list, bins=200, density=True, histtype='step', label=r'random.normal(0, $1^2$)', color='C0')
    ax2.hist(avg_list, bins=200, density=True, histtype='step', label=r'random.normal(0, $1^2$)', color='C1')
    ax2.hist(Mavg_list, bins=200, density=True, histtype='step', label=r'random.normal(0, $1^2$)', color='C2')
    ax2.hist(LowPass_list, bins=200, density=True, histtype='step', label=r'random.normal(0, $1^2$)', color='C2')
    plt.show()




