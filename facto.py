# m = 0
# sum = 1
# for k in range(5):
#         m = m + 1
#         sum = sum * m
#         print(sum)

# i = 0
# sum = 1
# while i<=5:
#     i = i + 1
#     sum = sum * i
#     print(sum)

# i = 0
# sum = 1
# while i<=5:
#     i = i + 1
#     sum = sum * i
# print(sum) #ถ้าอยากทำให้ออกแค่ตัวสุดท้ายให้เอาprintอยู่นอกloop

x = int(input("จะเอาFacที่เท่าไหร่ :"))
m = 0
sum = 1
for k in range(x):
        m = m + 1
        sum = sum * m

print(sum)
