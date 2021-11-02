# from openpyxl import load_workbook
# workbook = load_workbook(filename = "Book.xlsx")
# workbook.sheetnames

# sheet = workbook.active

# sheet.title
# x= sheet["A1"].value
# print(x)

# from openpyxl import Workbook

# workbook = Workbook()
# sheet = workbook.active

# sheet["A1"] = "hello"


# workbook.save(filename="hello.xlsx")
# "A"+1

# from openpyxl import Workbook  #0-8แนวตั้ง

# workbook = Workbook()
# sheet = workbook.active

# for i in range(10):
#     sheet["A"+str(i+1)]=i+1

# workbook.save(filename="he1.xlsx")    

# from openpyxl import Workbook  #1-9แนวนอน

# workbook = Workbook()
# sheet = workbook.active
# list = ["A","B","C","D","E","F","G","H","I","J"]
# for i in range(10):
#     sheet[list[i]+"1"]=i+1  #ตัวแรกจะเป็นตัวอักษรแนวตั้ง ตัวที่สองคือตำแหน่งของแถว
# workbook.save(filename="he2.xlsx") #ให้saveในไฟล์ชื่อ "he2.xlsx" 

# from openpyxl import Workbook  #1-10แนวทะแยง

# workbook = Workbook()
# sheet = workbook.active
# list = ["A","B","C","D","E","F","G","H","I","J"]
# for i in range(10):
#     sheet[list[i]+str(i+1)]=i+1  
# workbook.save(filename="he3.xlsx") 

# from openpyxl import Workbook  #1-99part1แนวตั้ง

# workbook = Workbook()
# sheet = workbook.active
# list = ["A","B","C","D","E","F","G","H","I","J"]
# x=-1
# y=0
# for a in range(10):
#     x=x+1 
#     for i in range(10):
#         y=y+1
#         sheet[list[x]+str(i+1)]=y
      
# workbook.save(filename="he4.xlsx")   

# from openpyxl import Workbook  #1-99part2 0-10แบบแนวนอน

# workbook = Workbook()
# sheet = workbook.active
# list = ["A","B","C","D","E","F","G","H","I","J"]
# x=0
# y=0
# for a in range(10):
#     x=x+1
#     for i in range(10):
#         y=y+1
#         sheet[list[i]+str(x)]=y
      
# workbook.save(filename="he5.xlsx")   


# from openpyxl import load_workbook
# workbook = load_workbook(filename = "score.xlsx")
# workbook.sheetnames
# sheet = workbook.active
# sheet.title   
# list = ["A","B","C","D","E","F","G","H","I","J"]
# slist=[]  #listเปล่าสำหรับเก็บคะแนนรวมของแต่ละคน
# sum = 0 #คะแนนของแต่ละคน
# y = 4
# aver = 0 #คะแนนรวมของทุกคน
# pas = 0
# f = 0
# for a in range(20): #ในrangeคือจำนวนคน
#     y= y+1
#     for i in range(6):  #ในrangeคือจำนวนช่องคะแนนที่จะคิด
#         x =sheet[list[i+1]+str(y)].value
#         sum = sum+x
#     sheet["I"+str(y)] = sum #ใส่คะแนนรวมที่ตั้งIแถวy
#     if sum > 80:     #โซนตัดเกรด
#         sheet["J"+str(y)]="A"
#     if sum <=80 and sum >70:
#         sheet["J"+str(y)]="B"
#     if sum <=70 and sum >60:
#         sheet["J"+str(y)]="C"
#     if sum <=60 and sum >=50:
#         sheet["J"+str(y)]="D"  
#     if sum <50:
#         sheet["j"+str(y)]="F"
#     if sum >=50:
#         pas=pas+1
#     if sum <50:
#         f = f+1
#     aver = aver + sum   #ตัวแปรที่ใช้ในการเก็บคะแนนของนักเรียนทุกคนรวมกัน
#     slist.append(sum)     
#     sum = 0 #resetค่าsum
# slist.sort()
# sheet["M11"]=str(slist[0])#คะแนนน้อยสุด
# sheet["M12"]=str(slist[19])#คะแนนมากสุด
# sheet["M15"]=str(f) #จำนวนคนที่ไม่ผ่าน
# sheet["M14"]=str(pas)   #จำนวนคนที่ผ่าน
# aver = aver/20    #หาค่าเฉลี่ย
# sheet["M13"]=str(aver)    
# workbook.save(filename="score1.xlsx")