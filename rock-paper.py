print("""----------LETS PLAY ROCK PAPER SCISSORS!-------------
You only have to choose between rock, paper and scissors.""")

while (True):
    player1 = input("Player 1?  ")
    player2 = input("Player 2?  ")

    if (player1 == "rock" and player2 == "paper"):
        print("Player 1 wins!")
    
    elif (player1 == "rock" and player2 == "scissors"):
        print("Player 2 wins!")
        
    elif (player1 == "rock" and player2 == "rock"):
        print("Draw!")
    elif (player1 == "paper" and player2 == "rock"):
        print("Player 1 wins!")
        
    elif (player1 == "paper" and player2 == "scissors"):
        print("Player 2 wins!")
        
    elif (player1 == "paper" and player2 == "paper"):
        print("Draw!")
        
    elif (player1 == "scissors" and player2 == "paper"):
        print("Player 1 wins!")
        
    elif (player1 == "scissors" and player2 == "scissors"):
        print("Draw!")
        
    elif (player1 == "scissors" and player2 == "rock"):
        print("Player 2 wins!")
           
    