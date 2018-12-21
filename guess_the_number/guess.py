import random

guess = random.randint(0,100)

correct = False
noties = 1
while correct == False: 
    inputNo = int(raw_input("Bitte die Zahl erraten: "))
    if inputNo == guess:
        print("Korrekt geraten! Gesamtzahl der Versuche: " + str(noties))
        correct = True
    elif inputNo < guess:
        print("zu erratende Zahl ist groesser")
    elif inputNo > guess:
        print("zu erratende Zahl ist kleiner")

    noties += 1