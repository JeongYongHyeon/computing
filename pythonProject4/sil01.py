import os # 디렉토리네 파일리스트를 불러오기위해 사용할 os 모듈을 import한다.
count = 0 # 동일한 이름이 카피될경우 증가할 count
while True: # 무한 루프
    filename = input('복사할 파일을 입력하세요: ') # 복사할 파일이름을 입력받음
    fp = open(filename+'.txt','r',encoding='utf-8') # 복사할 파일을 open하고 포인터객체로 저장
                                                    # encoding의 경우, 계속 파일을 읽어오지 못하는
                                                    # 에러가 떠서, 붙혀 주었습니다.(모든경우에 대해서 이러한 에러가 뜸)
    s = filename+'_copy.txt' # 복사할 파일이름에 _copy를 붙힌 문자열을 s에 저장
    in1 = fp.read() # read 모드로 지정한 포인터객체를 전부 읽어드리고 in1에 저장
    file_name_list = os.listdir() # 디렉토리내의 모든파일의 파일명을 리스트로써 저장

    if s in file_name_list: # 만약 복사한 파일명이 리스트에 있을경우
        count += 1 # 카운트를 하나 더해주고
        print(count) # 잘 동작하는지 확인하기위한 코드(없어도됨)
        fp0 = open(filename + '_copy' + '(' + str(count) + ')' + '.txt', 'w', encoding='utf-8')
        # 새로운 포인터객체를 쓰기모드로 열고 카운트한것을 추가해줌
        fp0.write(in1) # fp가 가르키는 포인터객체의 모든내용을 fp0 포인터객체가 가르키는 파일로 복사
        fp0.close() # 작업완료후에 닫아줘야함!
        fp.close() # 모든 객체포인터 닫아줘야한다!
    else: # 만약 복사한 파일명이 리스트에 없을 경우
        fp0 = open(s, 'w', encoding='utf-8') # fp0를 카운트추가 없이 그대로 파일명넣어주고 쓰기모드로 객체지정
        fp0.write(in1) # fp가 가르키는 포인터객체의 모든내용을 fp0 포인터객체가 가르키는 파일로 복사
        fp0.close() # 작업완료후에 닫아줘야함!
        fp.close() # 모든 객체포인터 닫아줘야한다!

    n = input() # n값 입력
    if n == ' ': # 스페이스바를 누를경우
        break # 반복문 탈출

