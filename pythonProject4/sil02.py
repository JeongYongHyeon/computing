fp = open('readMe.txt','r',encoding='utf-8') # readMe를 쓰기모드로 열고 fp 포인터객체로 지정

word = 0 # 단어의 개수를 저장할 변수 초기화
character = 0 # 문자의 개수를 저장할 변수 초기화
sentence = 0 # 문장의 개수를 저장할 변수 초기화

for line in fp.readlines(): # fp포인터가 가르키는 파일을 맨앞줄부터 한줄씩 읽어들인다.
    character += len(line) # 한줄의 길이를 입력받아 character 변수에 저장
                           # 문자의 개수가된다.
    word_line = line.split() # line을 띄어쓰기로 구분한 리스트
    word += len(word_line) # 띄어쓰기를 기준으로 나뉘어진 리스트의 길이를
                           # 더해가면서 word 변수에 저장 - 단어의 개수가된다.

fp.close() # 열었던 파일포인터 객체 닫아줌
character -= 1 # 문자의 길이는 1를 빼주어야 정확히 나온다.

fp = open('readMe.txt','r',encoding='utf-8') # 다시 동일하게 읽어온다.
for line in fp.read(): # 이번에는 한글자씩 전부 읽어온다.
    if line == '.': # 한글자씩 읽다 '.' 을 만나게되면
        sentence += 1 # 문장으로 인식하고 count
        print(line) # 잘동작하는지 확인하기위한 코드(없애도된다.)

fp.close() # 열었던 파일 포인터객체를 닫아준다.
print('글자: %d개, 문자: %d개, 문장: %d개 '%(character,word,sentence)) # 출력