print("Velkommen til demo trekantsberegner, vælg det du kender:")
print("A: Du kender 3 sider")
print("B: Du kender 2 sider og 1 vinkel.")
print("C: Du kender 1 side og 2 vinkler.")
valg=(input("indsæt det du ville bruge:")).lower()

# Kører programet hvis du vælger A eller a
if 'a' in valg:
    print("Du valgte A")
    side1 = float(input("Hvor lang er den første side?"))
    side2 = float(input("Hvor lang er den anden side?"))
    side3 = float(input("Hvor lang er den sidste side?"))

elif 'b' in valg:
    print("Du valgte B")
    while True:
        side1 = float(input("Hvor lang er den første side?"))
        side2 = float(input("Hvor lang er den anden side?"))
        vinkel1 = float(input("Hvad er vinklen?"))
        if vinkel1<180:
            print("Din vinkel er valid.")
            break
        else:
            print("Øv, din vinkel er ikke valid, prøv igen:")

elif 'c' in valg:
    print("Du valgte C")
    while True:
        side1 = float(input("Hvor lang er den første side?"))
        vinkel1= float(input("Hvad er den første vinkel?"))
        vinkel2 = float(input("Hvad er den anden vinkel?"))
        if vinkel1 + vinkel2<180:
            print("Din vinkeler er valid.")
            break
        else:
            print("Øv, din vinkler er ikke valid, prøv igen:")

else:
    while True:
        print("Du har indtastet noget ugyldig, prøv igen")
        break