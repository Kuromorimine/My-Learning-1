#Minesweeper
from openpyxl import Workbook 
import random
workbook = Workbook()
sheet = workbook.active
sheet.title
char = ["A","B","C","D","E","F","G","H","I","J","B","C","D","E","F","G","H","I","J","K","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for i in range(10):     #ใช้พื้นที่ ขนาด10x10ช่อง
    for j in range(10):
        sheet[char[i]+str(j+1)] = ""

for a in range(10):         #สุ่มที่Bomb
    for k in range(2):    #สุ่มเอาแถวแนวตั้ง2ลูก
        sheet[char[a]+str(random.randint(1,10))] = "Bomb"

workbook.save(filename="bombs1.xlsx")     
z = int(input("อยากลองกี่ครั้ง"))
gameover = 0
while gameover == 0:
    for y in range(z):         
        x=input("PlayerChoose"+str(y+1)+":") 
        if sheet[str(x)].value == "Bomb":
            print("Game Over")
            gameover=1
    print("Game Over")        
    gameover=1