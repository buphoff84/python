import random

dieSize = int(raw_input("Bitte Anzahl der Seiten eingeben: "))
noThrows = int(raw_input("Wie oft soll geworfen werden: "))

def rollDie(dieSize):
    print random.randint(1, dieSize)
    return

def main():
    i = 1;
    while i <= noThrows:
        print "Wurf " + str(i) + ": "
        rollDie(dieSize) 
        i += 1

if __name__ == '__main__':
    main()