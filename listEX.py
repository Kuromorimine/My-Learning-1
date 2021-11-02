# a = ["apple","banana","cherry"]
#        0          1       2

# print(a)
# print(a[1])
# print(len(a))#หาจำนวนสมาชิก

# a.append("orange")  #เพิ่มสมาชิกในaโดยที่มันจะอยู่บนสุด
# print(a)

# a.insert(0,"potato")  #เพิ่มสมาชิกโดยระบุตำแหน่ง
# print(a)
# a.remove(a[0])        #เอาสมาชิกออกโดยที่ระบุตำแหน่ง
# print(a)
# a.remove("banana")   #เอาสมาชิกออกโดยระบุชื่อ
# print(a)

# a = ["apple","banana","cherry"]
# for b in range(len(a)):
#     print(b)
#     print(a[b])

# for c in a:  #ถ้าcอยู่ในa  ให้printออกมา
#     print(c)    


# list=[0,1,2,3,4] ##ใช้inlistttttt
# for i in list:
#     print(i)


#โจทย์ สุ่มMonsterในlist
# import random
# a = random.randint(0,4)
# print(a)
# b = ["Diablos","Deviljho","Rajang","Rathalos","Mizutsune"]
# print(b[a])


# #โจทย์ สุ่มMonsterในlistแบบออกยาก
# import random
# b = ["Diablos","Deviljho","Deviljho","Deviljho","Deviljho","Deviljho","Deviljho","Deviljho","Deviljho","Rajang","Rathalos","Mizutsune"]
# a = random.randint(0,(len(b)-1))
# print(b[a])

#โจทย์ สุ่มMonsterในlistแบบออกยาก
# import random
# b = ["Diablos","Deviljho","Rajang","Rathalos","Mizutsune"]
# a = random.randint(0,100)
# l = input("Press enter to random")
# print(a)
# if l == "enter":
#     if a >0 and a <=50: #เกลืออออ
#         print(b[0])
#     if a >50 and a <=60: 
#         print(b[1])    
#     if a >60 and a <=75: 
#         print(b[2])
#     if a >75 and a <=99: 
#         print(b[3])
#     if a >99 and a <=100: #โครตพ่อโครตแม่rare
#         print(b[4])


# import msvcrt


# list= []
# k= msvcrt.getch()
# print(k)