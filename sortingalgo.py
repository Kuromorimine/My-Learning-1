# list=[14,33,27,35,10]  #ทำsorting algorithmโดยห้ามใช้sort pactice #จากน้อยไปมาก

# for a in range(4):
#     for i in range(4):
#         if list[i]>list[i+1]:  #เช็คว่าตัวนี้มากกว่าตัวถถัดไปใช่ไหม
#             list.insert(i,list[i+1])#แทรกเข้าแล้วลบออก
#             del list[i+2]
#             print(list)   #ตรงนี้d-bugได้

# # print(list)

# list=[33,10,27,35,14,15]  #ทำsorting algorithmโดยห้ามใช้sort pactice

# for a in range(len(list)-1):
#     for i in range(len(list)-1):
#         if list[i]>list[i+1]:
#             list.insert(i,list[i+1])#แทรกเข้าแล้วลบออก
#             del list[i+2]
#             print(list)   #ตรงนี้d-bugได้

# print(list)


# # sorting algorithm quiz #จากน้อยไปมาก
# import random
# list=[]
# c=0
# for b in range(10): 
#     x=random.randint(0,100)
#     list.append(x)
# print(list)
# for a in range(len(list)-1):
#     for i in range(len(list)-1):
#         if list[i]>list[i+1]:
#             list.insert(i,list[i+1])
#             del list[i+2]
#             c=c+1
#             # print(list) #d-bugตรงนี้
# print(list)
# print("ครั้งนี้ใช้การจัดทั้งหมด :",c)

import random #จากมากไปน้อย
list=[]
c=0
for b in range(10): 
    x=random.randint(0,100)
    list.append(x)
print(list)
for a in range(len(list)-1):
    for i in range(len(list)-1):
        if list[i]<list[i+1]:
            list.insert(i,list[i+1])
            del list[i+2]
            c= c+1
            # print(list) #d-bugตรงนี้
print(list)
