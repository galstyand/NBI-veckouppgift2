answer = input("Vill du ange temperaturen i Celsius(C) eller Farenheit(F)? ")
if answer == "C" or answer == "c":
    tempC = input("Skriv in en temperatur i grader Celsius: ")
    tempF = 1.8 * float(tempC) + 32
    print(str(tempF))
elif answer == "F" or answer == "f":
    tempF = input("Skriv in en temperatur i grader Farenheit: ")
    tempC = (float(tempF) - 32) / 1.8
    print(str(tempC))
else:
    print("Fel inmattning. Försök igen!")
    exit()

if float(tempC) < 10:
    print("Ta på sig vinterkläder!")
elif float(tempC) > 20:
    print("Packa badkläder!")