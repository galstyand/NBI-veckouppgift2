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
