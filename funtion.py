# def plus(x,y):
#     return x * y
# print(plus)    


#ยกกำลังโดยห้ามใช้เครื่องหมายยกกำลัง
# def power(x,y):
#     z = 1
#     for i in range(y):
#         z = z * x
#     return z
# print(power(2,3))  

# #ถอดรูดโดยใช้คูณ
# def sq(x):
#     return x ** 0.5
# print(sq(9))    

      

# #ให้ทำ + - * /
# a = int(input("ใส่เลขบวก"))
# b = int(input("ใส่เลขบวก"))
# def plus(x,y):
     
#     return x+y
# print(plus(a,b))    
# c = int(input("ใส่เลขลบ"))   
# d = int(input("ใส่เลขลบ")) 
# def sub(b,n)

#     return 

#เครื่องคิดเลข + - * / //
a = int(input("ใส่เลข"))  #inputพวกตัวเลข
b = input("ใส่เครื่องหมาย") 
c = int(input("ใส่เลข"))
def Cal(x,o,y):
    if o=="5":  #เครื่องหมายที่เราใช้จะถือว่าเป็นstring
        return x + y
    if o=="-":
        return x - y
    if o=="x":
        return x*y
    if o=="/":
        return x/y 
    if o=="sq":
        return x**0.5
print(Cal(a,b,c))  

# #สร้างFuntion Facto โดยใช้  loop

# def Fac(x):
#     sum = 1
#     for a in range(1,x+1):
#         sum = sum * a
#     return sum            
# print(Fac(5))

# สร้างFuntion Factoโดยใช้ if
# x = int(input("Facตัวที่เท่าไหร่")) 
# x = 1
# def Fac(x):
#     sum = 1
#     if x == sum:
#         return sum*x
#     if x != sum:
#             x = x-1
#         if x == sum:
#             print("x")
#         if x != sum:
#             x = x-1
# print(Fac(3))        

# # print(Fac(5))    
#สร้างFuntion fibonat โดยใช้  loop
# x = int(input("จะเอาถึงตัวที่เท่าไหร่"))
# def Fibo(x):
#     a = 0
#     b = 1
#     print(a)
#     print(b)
#     for k in range(x-2): 
#         c = a + b
#         print(c)
#         a = b #เปลี่ยนaให้กลายเป็นb
#         b = c #เปลี่ยนbให้กลายเป็นc
# print(Fibo(x))

#สร้างFuntion Fibonat โดยใช้ if