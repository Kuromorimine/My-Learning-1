#1 2 4 8 ... 1024 512 256 128 ... 1
x = 1
for i in range(0,10):
    print(x)
    x = x*2
for a in range(0,11):
    print(int(x))
    x = x/2 