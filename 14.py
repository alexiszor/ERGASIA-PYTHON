a = -1
b = -2
print("Select numbers greater or equal to zero ( second should be greater than first)")
while a > b or (a < 0 or b < 0):
    a = float(input(""))#zitoyntai oi arithmoi a,b
    b = float(input(""))

print("[",a,",",b,"]")#emfanisi diasthmatos
if a == int(a):
    a = int(a)
else:
    a = int(a) + 1
b = int(b)
print("select integer > 0 or equal to zero")
d = -1
while d < 0:
    d = int(input(""))#ziteitai o akeraios d
pr = []#lista pou tha apothikeyontai oi protoi arithmoi

for i in range(a,b+1):#eyresi proton aritmon sto [a,b]
    sum = 0
    F = 2
    while i > 1:
        
        if  i % F == 0:
                i = i / F
                sum = sum + 1
        else:
                F = F + 1
        if (i < 1 or i == 1) and sum == 1:
            pr.append(int(i*F))

#z metabliti pou menei 0 ean den yparxoun p kai q,allios ginetai 1
z = 0

for i in pr:#eyresi twn p,q
    
    for j in pr:
            
            
        if i - j == d or i - j == -d:
                p = i
                q = j        
                z = 1
        if z == 1:
                break
        
    if z == 1:
        break
if z == 1:
    print(p,q)
    print(d,"=","|",p,"-",q,"|")
else:
    print("there are no numbers")

