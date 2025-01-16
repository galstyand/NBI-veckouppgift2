print("Matchen är över, nu ska vi räkna ut resultatet!")
tottenham = input("Hur många mål gjorde Tottenham? ")
liverpool = input("Hur många mål gjorde Liverpool? ")
difference = int(tottenham) - int(liverpool)
if difference > 0:
    print("Tottenham vann med " + str(difference) + " mål")
elif difference < 0:
    print("Liverpool vann med " + str(abs(difference)) + " mål")
else:
    print("Oavgjort")

#testfall för att testa koden
#1. Tottenham 1, Liverpool 0. Resultat: Tottenham vann med 1 mål
#2. Tottenham 0, Liverpool 1. Resultat: Liverpool vann med 1 mål
#1. Tottenham 1, Liverpool 1. Resultat: Oavgjort

