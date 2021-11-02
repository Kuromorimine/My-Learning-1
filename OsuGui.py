# from tkinter import *
# import time
# import msvcrt
# window = Tk()
# window.title("OsuGui")
# window.geometry("200x60")
# window.attributes('-topmost', True)#ทำให้มันอยู่บนสุด
# window.update()


   
# for k in range(5,0,-1):#ให้ทำงานทุกๆ0.05วินาที
#     list=[]
#     CUR=Label(window,text=str(len(list)),fg="red",bg="white",font=20).pack()
#     for i in range(1,-1,-1): #ให้ทำงานทุกๆ0.01วินาที
#         k =msvcrt.getch()
#         list.append(str(k))
#         time.sleep(1)


# window.mainloop()


# from tkinter import *
# import time ,msvcrt
# from tkinterkeybind import key_pressed

# # x = input("ตัวที่1")
# window = Tk()
# window.title("KeyPerSecond")
# window.geometry("200x60")
# window.attributes('-topmost', True)
# window.update()

# z= TRUE

# while z: #สั่งให้มันทำงานไปเรื่อยๆ
#     for i in range(1,-1,-1):
#         list =[]
#         x = input("b only")
#         def check_freq(x):
#             freq={}
#             for c in set(x):
#                 freq[c]=x.count(c)
#             return freq

#         for a in range(1,-1,-1): #ตรวจสอบkeyที่กดโดยใช้"Mary had a little lamb".count("a")>>4
#             def key_press():    
#                 window.bind(x,key_pressed)
                
#                 list.append(" ")
#             time.sleep(10)
#         CUR=Label(window,text=str(len(list)),fg="red",bg="black",font=20).pack()

#         time.sleep(10000)
#     window.mainloop()



from tkinter import Tk, Label
root=Tk()
def key_pressed(event):
    w=Label(root,text="b:"+event.char)
    w.place(x=70,y=90)
    root.bind("b",key_pressed)

root.mainloop()