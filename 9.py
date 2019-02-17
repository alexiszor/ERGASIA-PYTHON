def abc(list):
    a = 0
    maxlist = []
    if len(list)==0:
        max = 0
    if len(list)==1:
        max = list[0]
        maxlist.append(list[0])
    if len(list) != 1:
        
        for i in range(0,len(list)):
            a = list[i]
        
            for j in range(i+1,len(list)):
                a = a + list[j]
                if i == 0 and j == 1:
                    max = a - 1
                
                if a > max:
                    max = a
                    maxlist.clear()
                    for k in range(i,j+1):
                        maxlist.append(list[k])
                   
    return (max,maxlist)
    

    
list = []
print("Choose lenngth of list")
length = int(input(""))
l = len(list)
num = 1
while l < length:
    print(num,"th","number")
    a = int(input(""))
    list.append(a)
    l = len(list)
    num = num + 1

print(abc(list))
            
