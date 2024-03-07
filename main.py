print("Velkommen til demo trekantsberegner, vælg det du kender:")
print("A: Du kender 3 sider")
print("B: Du kender 2 sider og 1 vinkel.")
print("C: Du kender 1 side og 2 vinkler.")
valg=(input("indsæt det du ville bruge:")).lower()

while True:
# Kører programmet hvis du vælger a eller A.
    if 'a' in valg:
        print("Du valgte A")
        side1 = float(input("Hvor lang er den første side?"))
        side2 = float(input("Hvor lang er den anden side?"))
        side3 = float(input("Hvor lang er den sidste side?"))

    # Kører programmet hvis du vælger b eller B.
    elif 'b' in valg:
        print("Du valgte B")
        b_vara = True
        while b_vara is True:
            side1 = float(input("Hvor lang er den første side?"))
            side2 = float(input("Hvor lang er den anden side?"))
            vinkel1 = float(input("Hvad er vinklen?"))
            if vinkel1<180:
                print("Din vinkel er valid.")
                b_vara = False
            else:
                print("Øv, din vinkel er ikke valid, prøv igen:")

    # Kører progemmet hvis du vægler c eller C.
    elif 'c' in valg:
        print("Du valgte C")
        c_vara = True
        while c_vara is True:
            side1 = float(input("Hvor lang er den første side?"))
            vinkel1= float(input("Hvad er den første vinkel?"))
            vinkel2 = float(input("Hvad er den anden vinkel?"))
            if vinkel1 + vinkel2<180:
                print("Din vinkeler er valid.")
                c_vara = False
            else:
                print("Øv, din vinkler er ikke valid, prøv igen:")

    else:
        print("Du har indtastet noget ugyldig, prøv igen")
    break