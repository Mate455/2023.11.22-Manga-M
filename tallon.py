# 2. Írj programot, beolvassa a felhasználó nevét, majd köszön neki

# Változok 
nev,szovegKiir = "", ""

nev = input("Hogyan Hivnak: ")

szovegKiir = f"Hello {nev}!"
print(szovegKiir)


#3.Írj programot, ami beolvas egy számot, majd kiírja a kétszeresét!
 
 #Változok 
 alapSzam, ketszeres, szovegKiir = 0 , 0, ""

 alapszam =int(input("Kérem a számot: "))
 ketszerese =2* alapSzam
 szovegKiir =f"A szam:{alapszam} \
 kétszeres: {ketszeres}"

 print(szovegKiir)


 """
#4.Írj programot, ami beolvas két számot, majd kiírja:
a. az összegüket;
b. különbségüket;
c. szorzatukat;
d. hányadosukat, ha lehet!

"""
#Változok 
elso, masodik ,osszeg ,kulonbseg ,szorzat ,hanyados ,szovegKir = 0, 0, 0, 0,

elso = int (input("Kérem a elsö számot :"))
elso = int (input("Kérem a második számot :"))


osszeg = elso + masodik
kulonbseg = elso - masodik
szorzat = elso * masodik
hanyados = elso / masodik
szovegKir =f"A számok:{elso},{masodik} "
szovegKir =f"A osszege:{osszeg} "
szovegKir =f"A külöbsége:{kulonbseg} "
szovegKir =f"A szorzata:{szorzat} "
szovegKir =f"A hanyadosa:{hanyados:} "

print(szovegKir)


#  5. Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!

#Változok 
elso,masodik, nagyobb, szovegKiir = 0, 0, 0,  ""

elso = int(input("Kérem az elsö számot: ")) 
masodik = int(input("Kérem a második számot: ")) 

if elso < masodik:
    nagyobb = masodik 
else: 
    nagyobb =elso
    
    szovegKiir = f"A nagyobb szám"



    # 6. Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet!

#Változó
elso,masodik,harmadik, legkisebb,  szovegKiir = 0, 0, 0, 0, ""

elso = int(input("Kérem az elsö számot: ")) 
masodik = int(input("Kérem a második számot: ")) 
harmadik = int(input("Kérem a harmadik számot: ")) 

# Sehédváltozó

if elso <= masodik:
    kisebb = elso
else: 
    kisebb = masodik

if kisebb <= harmadik:
        legkisebb = kisebb
else:
    legkisebb=harmadik

    szovegKiir = f"legkisebb szám" 
    print(szovegKiir)