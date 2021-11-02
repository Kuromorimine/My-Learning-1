# data = [3,2,4,8,10,2,6,9,8,3,7]
# sum = 0

# for i in range(len(data)):
#     sum = sum + data[i]
    
    
# print(sum)    #หาผลรวม
# print(sum/len(data)) #หาค่าเฉลี่ย

# data = [3,2,4,8,10,2,6,9,8,3,7]  

# for i in range(len(data)):    #แสดงตัวที่เป็นจำนวนคี่
#    if data[i]%2 == 1:
#        print(data[i])


# data = [3,2,4,8,10,2,6,9,8,3,7]  

# for i in range(len(data)):    #แสดงตัวที่เป็นจำนวนคู่
#    if data[i]%2 == 0:
#        print(data[i])       

# data = [3,2,4,8,10,2,6,9,8,3,7]  #แสดงตัวที่มีการซ้ำ
# k =[]
# data.sort()
# print(data)
# for i in range(len(data)-1):    
#    if data[i] == data[i+1]:
#       k.append(1)
#       print(data[i])
# print("มีตัวซ้ำ",len(k),"คู่")     

data = [3,2,4,8,10,2,6,9,8,8,3,7]  #แสดงตัวที่มีการซ้ำ โดยบอกจำนวนที่ซ้ำ
k =[]
data.sort()
print(data)
for i in range(len(data)-1):    
   if data[i] == data[i+1]:
      
      k.append(data[i])
      print(data[i],len(k),"ตัว")
      k.clear()

# data = [3,2,4,8,10,2,6,9,8,3,7] #หาตัวที่ซ้ำ
# y = 0
# for x in data:
#    if data.count(x)>1:
#       y+=1
#       data.remove(x)
# print(y)      

# data = [3,2,4,8,10,2,6,9,8,3,7]
# All = 0
# for i in data:
#    All = All + i
# print(All)         