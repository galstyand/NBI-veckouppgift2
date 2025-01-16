number1 = int(input("Ange första numret: "))
number2 = int(input("Ange första andra: "))
number3 = int(input("Ange första tredje: "))

#1
summa = number1+number2+number3
print("Summan blir: " + str(summa))

#2
max = number1
if number2 > max:
    max = number2
if number3 > max:
    max = number3
print("Sötrsta numret är: " + str(max))

#3 och 4
if number3 == number2 == number1:
    print("Alla är lika!")
    print("Melersta tal: " + str(number1))
elif number3 == number2 or number3 == number1 or number2 == number1:
    print("Två lika!")
    print("Finns inget mellersta tal! ")
else:
    print("Inga lika!")
    if (number2 < number1 < number3) or (number3 < number1 < number2):
        print("Melersta siffran är: " + str(number1))
    elif (number1 < number2 < number3) or (number3 < number2 < number1):
        print("Melersta siffran är: " + str(number2))
    else:
        print("Melersta siffran är: " + str(number3))

