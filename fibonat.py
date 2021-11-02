#0 1 1 2 3 5 8 13 21 34

a = 0
b = 1
print(a)
print(b)
for x in range(10): 
    c = a + b
    print(c)
    a = b #เปลี่ยนaให้กลายเป็นb
    b = c #เปลี่ยนbให้กลายเป็นc