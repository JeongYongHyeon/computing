import os # os를 활용해 디렉토리네 파일명을 읽어오고 remove 함수를 활용하기위해 import
# os.remove()를 통해서 원래 있던 파일을 지움
# string.zfill() -> “1”.zfill(3)  “001” 처럼동작

while True: # 무한루프
    n = int(input('1.start condition 2.end condition: ')) # n으로 어떤 동작을 할지 입력받음
    if n == 1: # n이 1일 경우 파일전체 다른파일명으로 변경후 복사됨
        file_name_list = os.listdir() # 디렉토리네 파일명들의 리스트를 file_name_list에 저장
        search = input('search: ') # 찾을 파일명 입력
        match_list = [] # 찾을 파일명이 포함된 파일명들을 저장할 리스트 초기화
        for word in file_name_list: # file_name_list 를 인덱스0성분부터 반복하여 word에 넣어줌
            if search in word: # 찾을 파일명이 word에 있을경우
                match_list.append(word) # match_list에 word를 뒤로 붙혀가며 추가
        print('filterd file:',match_list) # 검색한 파일명 출력

        new_file_name = input('file name: ') # 새로변경할 파일명입력
        length = input('length(number) : ') # 뒤에 붙혀줄 숫자의 길이 지정
        for i in range(len(match_list)): # match_list의 길이만큼 반복
            back = str(i).zfill(int(length)) # 뒤에 붙혀줄 숫자.length길이로 번호(i)가 하나씩늘려가면서 바뀜
            fp = open(match_list[i], 'r',encoding='utf-8') # match_list의 i번째 인덱스의 파일명을 read모드로
                                                           # 열어주고 파일포인터 객체지정
            fp2 = open(new_file_name+'_'+back+'.txt','w',encoding='utf-8') # 새로 변경할 파일명에 뒤에붙혀줄 숫자를
                                                                           # 문자열로 더해서 쓰기모드로 열어주고
                                                                           # 파일 포인터 객체지정
            in1 = fp.read() # 원래의 읽어온 파일의 내용을 in1에 전부 저장
            fp2.write(in1) # 그대로 복사
            fp.close() # 읽기모드 포인터객체는 닫아준다.
            os.remove(match_list[i]) # 복사가 완료되면 원래있던 파일들은 전부 지워줌
            fp2.close() # 복사가 완료된 파일도(쓰기모드로 열었던) 포인터객체 닫아준다.

            # 이작업을 i인덱스가 하나씩 늘어나면서 반복
        file_name_list = os.listdir() # 현재 디렉토리네 파일명들을 다시 읽어옴
        renamed_list = [] # 다시 정의된 파일명들을 저장할 리스트
        for word in file_name_list: # 앞에서 했던 검색작업 반복
            if new_file_name in word:
                renamed_list.append(word)
        print('renamed file: ',renamed_list) # 새로 이름이 바뀐 복사파일들 파일명 출력

    elif n == 2: # n이 2일경우
        break # 반복문 탈출
