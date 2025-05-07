import numpy as np

start = input("Drücke Enter, um das Spiel zu beginnen!")

print("\n")

if start == "":
    player1_score = 0
    player2_score = 0
    game_round = 1
    
    while player1_score != 3 or player2_score != 3:
        print(f"Runde: {game_round}" )
        print("\n")
        
        # player inputs
        player1_start = input("Spieler 1, Drücke Enter!")
        player1_value = np.random.randint(low=1, high=7)
        print(f"Spieler 1, dein Score ist: {player1_value}")
        
        print("\n")
        
        player2_start = input("Spieler 2, Drücke Enter!")
        player2_value = np.random.randint(low=1, high=7)
        print(f"Spieler 2, dein Score ist: {player2_value}")
        
        print("\n")
        
        if player1_value > player2_value:
            player1_score += 1
        elif player1_value < player2_value:
            player2_score += 1
            
        print(f"Gesamter Score: \n Spieler 1: {player1_score} \n Spieler 2: {player2_score}")
            
        print("\n")

