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