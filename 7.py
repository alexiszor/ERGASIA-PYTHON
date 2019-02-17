import random

#to tetragono opou paizetai to paixnidi
a = ["","",""]#pano grammi
a2 = ["","",""]#mesaia grammi
a3 = ["","",""]#kato grammi

#to tetragono opou dinontai oi odhgies
z = ["0","1","2"]#pano grammi
z2 = ["3","4","5"]#mesaia grammi
z3 = ["6","7","8"]#kato grammi

abc = ["0","1","2","3","4","5","6","7","8"]#lista apo opou epilegei o ypologistis

c = 0#c einai i metabliti tou paikti
d = 0#d einai i metabliti tou ypologisti

print("To play first in the game select 1 else,press 2")
p = int(input(""))
print("select Symbol ,press 1 for o or 2 for x")
symbol = int(input(""))
if symbol == 1:
             c = "o"
             d = "x"
             print("The computer  plays automatically.")
             print("Select where you want to play with help from the table with numbers below(For example,to put (o) in 0 position ,press 0)")
             print("! BE CAREFUL  DON'T SELECT A POSITION THAS HAS BEEN SELECTED BEFORE")
elif symbol == 2:
             c = "x"
             d = "o"
             print("The computer plays automatically.")
             print("Select where you want to play with help from the table with numbers below(For example,to put (x) in 0 position ,press 0)")
             print("!! BE CAREFUL  DON'T SELECT A POSITION THAS HAS BEEN SELECTED BEFORE")
             
#emfanisi tou tetragonou odhgion
print(z)#emfanisi pano grammis
print(z2)#emfanisi mesaias grammis
print(z3)#emfanisi kato grammis

#emfanisi tou tetragonou pou pazetai to paixnidi
print(a)#emfanisi pano grammis
print(a2)#emfanisi mesaias grammis
print(a3)#emfanisi kato grammis
print()

A1 = -1#metablites poy xrismopoioyntai oste na mhn epilegei kouti pou exei epilexthei
A2 = -1
A3 = -1
A4 = -1
A5 = -1
A6 = -1
A7 = -1
A8 = -1

r = 0#metabliti pou ginetai 1 ean kapoios nikise i menei miden an to paixnidi irthe isopalia

error = 0#metabliti oste na min emfanisontai minimata an exei ginei lathos

sum = 0#metabliti pou elegxei pios exei seira

while sum < 9:
    
    if p == 1:#diadikasia ean o paiktis exei epilexei na paixei protos
        
    
        if sum % 2 == 0:#seira paixth
            
            b = int(input(""))#elegxos oste na min synexistei to paixnidi an epilexei kouti pou exei epilegei apo prin o paiktis
            if b == A1 or b == A2 or b == A3 or b == A4 or b == A5 or b == A6 or b == A6 or b == A7 or b == A8:
                sum = 9
                print("error")
                error = 1
            
 
            if b < 9 and b > 5:#topothetisi symbolon stin kato grammi
                b=b-6
                a3[b] = c
                b=b+6
            elif b > 2 and b < 6:#topothetisi symbolon stin mesaia grammi
                b=b-3
                a2[b] = c
                b=b+3
            else:#topothetisi symbolon stin pano grammi
                a[b] = c
            print(a)
            print(a2)
            print(a3)
            print()
            sum = sum + 1
            #apothikeysi ton theseon pou exoun epilexthei
            if sum == 1:
                A1 = b
            elif sum == 3:
                A3 = b
            elif sum == 5:
                A5 = b
            elif sum == 7:
                A7 = b
            
        else:#seira ypologisth
            b = random.choice(abc)
            b = int(b)
            while b == A1 or b == A2 or b == A3 or b == A4 or b == A5 or b == A6 or b == A6 or b == A7 or b == A8:#elegxos oste na min epilexei o ypologistis kouti pou exei epilexthei
                b = random.choice(abc)
                b = int(b)

            if b < 9 and b > 5:#topothetisi symbolon stin kato grammi
                b=b-6
                a3[b] = d
                b=b+6
            elif b > 2 and b < 6:#topothetisi symbolon stin mesaia grammi
                b=b-3
                a2[b] = d
                b=b+3
            else:#topothetisi symbolon stin pano grammi
                a[b] = d
            print(a)
            print(a2)
            print(a3)
            print()
            sum = sum + 1
            #apothikeysi ton theseon pou exoun epilexthei
            if sum == 2:
                A2 = b
            elif sum == 4:
                A4 = b
            elif sum == 6:
                A6 = b
            elif sum == 8:
                A8 = b
    elif p == 2 :#diadikasia ean o ypologistis paizei protos

        if sum % 2 == 0:#seira ypologisti
            
            b = random.choice(abc)
            b = int(b)
            while b == A1 or b == A2 or b == A3 or b == A4 or b == A5 or b == A6 or b == A6 or b == A7 or b == A8:#elegxos oste na min epilexei o ypologistis kouti pou exei epilexthei
                b = random.choice(abc)
                b = int(b)
                
                

            if b < 9 and b > 5:#topothetisi symbolon stin kato grammi
                b=b-6
                a3[b] = d
                b=b+6
            elif b > 2 and b < 6:#topothetisi symbolon stin mesaia grammi
                b=b-3
                a2[b] = d
                b=b+3
            else:#topothetisi symbolon stin pano grammi
                a[b] = d
            print(a)
            print(a2)
            print(a3)
            print()
            sum = sum + 1
            #apothikeysi ton theseon pou exoun epilexthei
            if sum == 1:
                A1 = b
            elif sum == 3:
                A3 = b
            elif sum == 5:
                A5 = b
            elif sum == 7:
                A7 = b

        else:#seira paixth
            b = int(input(""))#elegxos oste na min synexistei to paixnidi an epilexei kouti pou exei epilegei apo prin o paiktis
            if b == A1 or b == A2 or b == A3 or b == A4 or b == A5 or b == A6 or b == A6 or b == A7 or b == A8:
                sum = 9
                print("error")
                error = 1

            if b < 9 and b > 5:#topothetisi symbolon stin kato grammi
                b=b-6
                a3[b] = c
                b=b+6
            elif b > 2:#topothetisi symbolon stin mesaia grammi
                b=b-3
                a2[b] = c
                b=b+3
            else:#topothetisi symbolon stin pano grammi
                a[b] = c
            print(a)
            print(a2)
            print(a3)
            print()
            sum = sum + 1
            #apothikeysi ton theseon pou exoun epilexthei
            if sum == 2:
                A2 = b
            elif sum == 4:
                A4 = b
            elif sum == 6:
                A6 = b
            elif sum == 8:
                A8 = b

     #elexgoi gia niki tou paikti   
    if ((a[0] == c and a[1] == c and a[2] == c) or (a2[0] == c and a2[1] == c and a2[2] == c) or (a3[0] == c and a3[1] == c and a3[2] == c)) and error == 0:
        sum = 9
        print("player 1  wins")
        r = 1
    elif ((a[0] == c and a2[0] == c and a3[0] == c) or (a[1] == c and a2[1] == c and a3[1] == c) or (a[2] == c and a2[2] == c and a3[2] == c)) and error == 0 :
        sum = 9
        print("player 1  wins")
        r = 1
    elif ((a[0] == c and a2[1] == c and a3[2] == c) or (a[2] == c and a2[1] == c and a3[0] == c)) and error == 0 :
        sum = 9
        print("player 1  wins")
        r = 1

    #elegxoi gia niki tou ypologisth
    if ((a[0] == d and a[1] == d and a[2] == d) or (a2[0] == d and a2[1] == d and a2[2] == d) or (a3[0] == d and a3[1] == d and a3[2] == d)) and error == 0 :
        sum = 9
        print("compputer  wins")
        r = 1
    elif ((a[0] == d and a2[0] == d and a3[0] == d) or (a[1] == d and a2[1] == d and a3[1] == d) or (a[2] == d and a2[2] == d and a3[2] == d)) and error == 0:
        sum = 9
        print("computer  wins")
        r = 1
    elif ((a[0] == d and a2[1] == d and a3[2] == d) or (a[2] == d and a2[1] == d and a3[0] == d)) and error == 0 :
        sum = 9
        print("computer  wins")
        r = 1

    #elegxos isopalias
    if sum == 9 and r == 0 and error == 0 :
        print("Draw")
   
