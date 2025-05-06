import numpy as np

start = input("Um Spiel anzufangen, druck mal Enter")

print("\n")

if start == "":
    player1_score = 0
    player2_score = 0
    game_round = 1
    
    while player1_score != 3 or player2_score != 3:
        print(f"Round {game_round}, FIGHT!")
        print("\n")
        
        # player inputs
        player1_start = input("Player 1, press enter")
        player1_value = np.random.randint(low=1, high=7)
        print(f"Plyer 1, your score is: {player1_value}")
        
        print("\n")
        
        player2_start = input("Player 2, press enter")
        player2_value = np.random.randint(low=1, high=7)
        print(f"Plyer 2, your score is: {player2_value}")
        
        print("\n")
        
        if player1_value > player2_value:
            player1_score += 1
        elif player1_value < player2_value:
            player2_score += 1
            
        print(f"Game score is: \n Player 1: {player1_score} \n Player 2: {player2_score}")
            
        print("\n")

