from Math import *
from Dateandtime import *

# Tells you the time date and the day.
todaysDateTime

# Det er loop for hele program endtil brugeren siger nej til sprøgsmålet.
while True:
    print("Velkommen til trekantsberegner, vælg det du kender:")
    print("A: Du kender 3 sider.")
    print("B: Du kender 2 sider og 1 vinkel.")
    print("C: Du kender 1 side og 2 vinkler.")
    valg = (input("Indsæt det du ville bruge:")). lower()

# Kører programmet hvis du vælger a eller A.
    if 'a' in valg:
        print("Du valgte A")
        sidesCheck = True
        while sidesCheck is True:
            try:
                sidea = float(input("Hvor lang er den første side?"))
                print("Din første side er:", sidea)
                sideb = float(input("Hvor lang er den anden side?"))
                print("Din anden side er:", sideb)
                sidec = float(input("Hvor lang er den sidste side?"))
                print("Din anden side er:", sidec)

                print("Side a er:", sidea)
                print("Side b er:", sideb)
                print("Side c er:", sidec)
                vinkelA = cosinusrelation_vinkel_vil(sidea, sideb, sidec)
                print("Vinkel A er:", vinkelA)
                vinkelB = sinusrelation_vinkel_vil(sidea, sidec, vinkelA)
                print("Vnkel B er:", vinkelB)
                vinkelC = vinkelsum(vinkelA, vinkelB)
                print("Vinkel C er:", vinkelC)

                if vinkelA + vinkelB + vinkelC < 180:
                    print("")
                else:
                    print("Din trekant er ugyldig")

                break

            except ValueError:
                print('')
                print("Du har indtastet noget ugyldig, prøv igen:")


# Kører programmet hvis du vælger b eller B.
    elif 'b' in valg:
        print("Du valgte B")
        # Loop for til at tjekke om hvis brugeren kommer til at skriv et str.
        sidesCheck = True
        while sidesCheck is True:
            b_vara = True
            while b_vara is True:
                try:
                    side1 = float(input("Hvor lang er den første side?"))
                    print("Din første side er:", side1)
                    side2 = float(input("Hvor lang er den anden side?"))
                    print("Din anden side er:", side2)
                    vinkel1 = float(input("Hvad er vinklen?"))
                    print("Din første vinkel er:", vinkel1)
                    # Tjekker om din trekant kan laves.
                    if vinkel1 < 180:
                        print("Din vinkel er valid.")
                        b_vara = False
                        sidesCheck = False
                    else:
                        print("Din vinkel er ugyldig, prøv igen:")

                    print("Side A er:", side1)
                    print("side B er:", side2)
                    print("Side c er:", pythagoras_hypotenuse(side1, side2))

                except ValueError:
                    print('')
                    print("Du har tastest noget ugyldig, prøv igen:")

    # Kører progemmet hvis du vægler c eller C.
    elif 'c' in valg:
        print("Du valgte C")
        sidesCheck = True
        while sidesCheck is True:
            try:
                c_vara = True
                while c_vara is True:
                    side1 = float(input("Hvor lang er den første side?"))
                    print("Din anden side er:", side1)
                    vinkel1 = float(input("Hvad er den første vinkel?"))
                    print("Din første vinkel er:", vinkel1)
                    vinkel2 = float(input("Hvad er den anden vinkel?"))
                    print("Din anden vinkel er:", vinkel2)

                    if vinkel1 + vinkel2 < 180:
                        print("Din vinkeler er gyldig.")
                        c_vara = False
                        sidesCheck = False
                    else:
                        print("Din vinkler er ugyldig, prøv igen:")

            except ValueError:
                print('')
                print("Du har indtastet noget ugyldigt, prøv igen:")

    else:
        print("Du har indtastet noget ugyldig, prøv igen")

    print('')
    print("Skal du bruge programmet igen?")
    choice = input("Skriv ja eller nej:")
    if 'nej' in choice:
        print("Tak fordi du brugte denne trekantsberegner :)")
        break
