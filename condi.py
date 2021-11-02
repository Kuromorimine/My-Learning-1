# a = 9  #น้อยกว่า มากกว่า เท่ากับ ไม่เท่ากับ
# b = 5  #  <      >     ==     !=


# if a > b:
#     print("a มากกว่า b")
# else:
#     print("a น้อยกว่า b")    

# a = 5
# b = 6

# if a > b:
#     print("a มากกว่า b")

# if a < b:
#     print("a น้อยกว่า b")

# if a == b:
#     print("a เท่ากับ b")    

# if a != b:
#     print("a ไม่เท่ากับ b")

# import random
# a = random.randint(1,10) #1-10
# print("a= ",a)
# b = input("ใส่มาสิ :")
# print("b = ",b)

# if a > b:
#     print("a มากกว่า b")

# import random
# a = 8
# print("a= ",a)
# b = int(input("ใส่มาสิ :"))
# print("b = ",b)

# if a > b:
#     print("a มากกว่า b")

#ทำเกมทายตัวเลข
#random 1-10
#in put เพื่อทายตัวเลข
#1 >
#2 <
#3 =
# import random
# a = random.randint(1,10) #1-10

# b = int(input("คิดว่าเท่าไร่ ใส่มา :"))

# if a > b:
#     print("a มากกว่า b")

# if a < b:
#     print("a น้อยกว่า b")

#     if a == b:
#     print("ยินดีด้วยทายถูก")

# import random     #คราวนี้อยากให้ถ้าทายถูกให้หยุด
# a = random.randint(1,10) #1-10
# for x in range(3):
#     b = int(input("คิดว่าเท่าไร่ ใส่มา :"))

#     if a == b:
#         print("ยินดีด้วย")
#         break
#     if a < b:
#         print("มากไปนะ")
#     if a > b:
#         print("น้อยไปนะ")     

# import random     #ทายผิดครบ3ครั้งแล้วให้ขึ้นว่าGame Over
# a = random.randint(1,10) #1-10
# c = 1
# print(a)
# for x in range(3):
#     b = int(input("คิดว่าเท่าไร่ ใส่มา :"))

#     if a == b:
#         print("ยินดีด้วย")
#         break
#     if a < b:
#         print("มากไปนะ")
#     if a > b:
#         print("น้อยไปนะ")    
#     c = c + 1
# if c == 4:
#     print("Game Over")


# import random  #คราวนี้อยากให้ถ้าทายถูกให้หยุด โดยใช้while
# a = random.randint(1,10) #1-10
# print(a)
# z = 1
# while z <=3:
#     b = int(input("คิดว่าเท่าไร่ ใส่มา :"))

#     if a == b:
#         print("ยินดีด้วย")
#         z = z + 11
#     if a < b:
#         print("มากไปนะ")
#     if a > b:
#         print("น้อยไปนะ")   
#     z = z + 1    


# import random  #คราวนี้อยากให้ถ้าทายถูกให้หยุด โดยใช้while
# a = random.randint(1,10) #1-10  #ถ้าทายผิด3ครั้ง ให้ขึ้นGame Over
# print(a)
# z = 1
# while z <=3:
#     b = int(input("คิดว่าเท่าไร่ ใส่มา :"))

#     if a == b:
#         print("ยินดีด้วย")
#         z = z + 10
#     if a < b:
#         print("มากไปนะ")
#     if a > b:
#         print("น้อยไปนะ")   
#     z = z + 1 
    
# if z == 4:
#     print("GameOver")

# import random  #เอาจริงๆจะใช้elifก็ได้นะ
# a = random.randint(1,10) 
# print(a)
# z = 1
# while z <=3:
#     b = int(input("คิดว่าเท่าไร่ ใส่มา :"))

#     if a == b:
#         print("ยินดีด้วย")
#         z = z + 10
#     elif a < b:
#         print("มากไปนะ")
#     elif a > b:
#         print("น้อยไปนะ")   
#     z = z + 1 
    
# if z == 4:
#     print("GameOver")

# import random  #เอาจริงๆจะใช้elifก็ได้นะ
# a = random.randint(1,10) 
# print(a)
# z = 1
# while z <=3:
#     b = int(input("คิดว่าเท่าไร่ ใส่มา :"))

#     if a == b:
#         print("ยินดีด้วย")
#         z = z + 10
#     elif a < b:
#         print("มากไปนะ")
#     elif a > b:
#         print("น้อยไปนะ")   
#     z = z + 1 
    
# if z == 4:
#     print("GameOver")    

import random  #เอาจริงๆจะใช้elifก็ได้นะ
a = random.randint(1,10) 
print(a)
z = 1
while z <=3:
    b = int(input("คิดว่าเท่าไร่ ใส่มา :"))

    if a == b:
        print("ยินดีด้วย")
    
        z += 3
    elif a < b:
        print("มากไปนะ")
    elif a > b:
        print("น้อยไปนะ")   
    z = z + 1 
    
if z == 4:
    print("GameOver")        