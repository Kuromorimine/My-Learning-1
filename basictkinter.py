# from tkinter import *    #เอาtkinterมาใช้
# window =Tk()
# window.title("OsuGui")

# #ใส่ข้อความในหน้าจอOsuGui
# #text ใส่ข้อความ fgใส่สีของข้อความ fontใส่เพื่อระบุขนาดของตัวstr bgใส่สีพื้นหบังข้อความ
# CUR= Label(text = "Hello world",fg="red",font=20,bg="yellow").pack()#ใส่packเพื่อนำlabelไปใส่ในpop
# CUR2=Label(pop,text = "Welcome To Osu",fg="green",font=20,bg="pink").pack()#popหน้าtextเพราะในกรณีที่มีหลายหน้าจะได้ใส่ถูกที่


#กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
        #ขนาดของจอ(ที่คูณกัน)และตำแหน่งx,y(ที่บวกกัน)
# window.geometry("100x100+50+400")
# window.mainloop()

# from tkinter import *    #เอาtkinterมาใช้
# window =Tk()
# window.title("OsuGui")

# #ใช้placeเพื่อระบุตำแหน่งของข้อความในpop
# # CUR= Label(text = "Hello world",fg="red",font=20,bg="yellow").place(x=0,y=0)
# # CUR2=Label(pop,text = "Welcome To Osu",fg="green",font=20,bg="pink").place(x=100,y=100)

# window.geometry("100x100+50+400")
# window.mainloop()

# from tkinter import *    #เอาtkinterมาใช้
# window =Tk()
# window.title("OsuGui")

# #rowแนวนอน columnแนวตั้ง
# # CUR1=Label(window,text = "Hello world",fg="red",font=20,bg="yellow").grid(row=2,column=0)
# # CUR2=Label(window,text = "Welcome To Osu",fg="green",font=20,bg="pink").grid(row=2,column=1)


# #กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
#         #ขนาดของจอ(ที่คูณกัน)และตำแหน่งx,y(ที่บวกกัน)
# window.geometry("100x100+50+400")
# window.mainloop()

from tkinter import *   
window =Tk()
window.title("OsuGui")


CUR1=Label(window,text = "Hello world",fg="red",font=20,bg="yellow").pack()

#ใส่ปุ่ม
btn1 = Button(window,text="บันทึก",fg="yellow",bg="black").pack()



window.geometry("100x100+50+400")
window.mainloop()