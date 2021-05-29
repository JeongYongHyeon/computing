from PIL import Image, ImageTk, ImageFilter # PIL 패키지로부터 Image,ImageTk,ImageFilter 모듈 import
import tkinter as tk # tkinter 모듈 tk라는 이름으로 import
from tkinter import filedialog as fd # tkinter 모듈로부터 filedialog 를 fd라는 이름으로 import


im = None # im 변수 선언 및 초기화
tk_img = None# tk_img 변수 선언 및 초기화

class Interface: # 부모 class
    def __init__(self): # 생성자 (pass로 넘김, 사용x)
        pass

    def open(self): # 파일 열기 (pass 후 자식 class에 넘김)
        pass

    def quit(self): # 종료
        self.window.quit() # 생성한 객체의 윈도우를 종료

    def image_rotate(self): # img processing rotate (pass 후 자식 class에 넘김)
        pass

    def image_blur(self): # img processing blur (pass 후 자식 class에 넘김)
        pass

    def image_edgeEnhance(self): # img processing edge enhance (pass 후 자식 class에 넘김)
        pass

    def interface(self): # interface 생성
        #global window
        self.window = tk.Tk() # window 객체 변수에 Tk 매서드로 생성한 전체창 저장
        self.canvas = tk.Canvas(self.window,width=512,height=512) # 그림을 그릴수 있는 창 사진크기에 맟춰 생성
        self.canvas.pack() # canvas 화면에 보일 수 있게함
        menubar = tk.Menu(self.window) # 생성한 window객체에 menu 추가하여 menubar에 저장
        filemenu = tk.Menu(menubar) # 파일 메뉴
        ipmenu = tk.Menu(menubar) # image processing 메뉴

        filemenu.add_command(label='열기', command= self.open) # 파일메뉴에 '열기' 눌렀을시, open 메서드가 실행
        filemenu.add_command(label='종료', command= self.quit) # 파일메뉴에 '종료' 눌렀을시, quit 메서드가 실행
        ipmenu.add_command(label='영상회전', command= self.image_rotate) # 파일메뉴에 '영상회전' 눌렀을시,image_rotate 메서드가 실행
        ipmenu.add_command(label='영상흐리개', command= self.image_blur) # 파일메뉴에 '영상흐리개' 눌렀을시,image_blur 메서드가 실행
        ipmenu.add_command(label='edgeEnhance',command = self.image_edgeEnhance) # 'image_edgeEnhance'눌렀을시,image_edgeEnhance 메서드 실행

        menubar.add_cascade(label='파일', menu=filemenu) # '파일' 눌렀을시, filemenu 메뉴창 실행
        menubar.add_cascade(label='영상처리', menu=ipmenu) # '영상처리' 눌렀을시, ipmenu 메뉴창 실행
        self.window.config(menu=menubar) # 메뉴를 구성함
        self.window.mainloop() # 윈도우객체 생성후 유지되게만듬


class ImgProcessing(Interface): # 영상처리 자식 클래스(Interface 부모 클래스로 상속)
    def open(self):  # open 메서드에 내용추가
        #global im, tk_img
        self.fname = fd.askopenfilename() # 내pc에서 파일 찾고 열 수 있도록함
        self.im = Image.open(self.fname) # 찾은 파일을 열어서 im 객체에 저장
        self.im2 = self.im.resize((512, 512)) # im의 사이즈를 512,512로 재구성
        self.tk_img = ImageTk.PhotoImage(self.im2) # Tk와 연동되도록 ImageTk 의 PhotoImage 메서드를 이용하여, im2를 tk_img에 저장
        self.canvas.create_image(256, 256, image=self.tk_img) # 이미지를 tk canvas에 생성
        self.window.update() # 수정된것 window 객체에 update 시켜줌

    def quit(self):
        self.window.quit()

    def image_rotate(self): # image rotate 메서드에 내용추가
        #global im, tk_img
        self.out = self.im.rotate(45) # im 객체의 이미지를 45도 rotate 시키고 out 객체에 저장
        self.tk_img = ImageTk.PhotoImage(self.out) # rotate된 사진 tk_img 객체에 Tk image로 저장
        self.canvas.create_image(256, 256, image=self.tk_img) # 이미지를 tk canvas에 생성
        self.window.update() # 수정된것 window 객체에 update

    def image_blur(self): # image blur 메서드에 내용추가
        #global im, tk_img
        self.out = self.im.filter(ImageFilter.BLUR) # im이미지 blur처리하여 out 객체에 저장
        self.tk_img = ImageTk.PhotoImage(self.out) # blur된 사진 tk_img 객체에 Tk image로 저장
        self.canvas.create_image(256, 256, image=self.tk_img) # 이미지를 tk canvas에 생성
        self.window.update() # 수정된것 window 객체에 update

    def image_edgeEnhance(self): # image edge enhance 메서드에 내용추가
        self.out = self.im.filter(ImageFilter.EDGE_ENHANCE) # im 이미지 edge enhance 처리하여 out 객체에 저장
        self.tk_img = ImageTk.PhotoImage(self.out) # edge enhance된 사진 tk_img객체에 Tk image 로 저장
        self.canvas.create_image(256,256,image=self.tk_img) # 이미지를 tk canvas에 생성
        self.window.update() # 수정된것 window 객체에 update



a = ImgProcessing() # a 객체생성
a.interface() # interface 메서드 실행
