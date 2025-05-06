import random

while True:
    print("Würfel mit Enter!")
    input( )
    
    wuerfel1 = random.randint(1,6)
    wuerfel2 = random.randint(1,6)
    
    print(wuerfel1)
    print(wuerfel2)
    
    if wuerfel1 + wuerfel2 == 12:
        print("Du hast gewonnen")
        break
    else:
        print("Du verlierst")