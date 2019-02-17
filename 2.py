b = 0
num = []

print("give number")
F = 2
b = int(input(""))
while b > 1 and b < 1000001:
        if  b % F == 0:
                F = int(F)                
                num.append(F)
                b = b / F
        else:
                F = F + 1

 		
for i in range(len(num)):print(num[i],"*", end=" ")if (i!=len(num) - 1)else print(num[i])
        
