import random

while True:
    print("Würfel mit Enter!")
    input()
    
    wuerfel1 = random.randint(1,6)
    wuerfel2 = random.randint(1,6)
    
    print(wuerfel1)
    print(wuerfel2)
    
    if wuerfel1 == 6 and wuerfel2 == 6:
        print("Du hast gewonnen")
        break
    else:
        print("Es wird noch einmal gewürfelt")
        print()