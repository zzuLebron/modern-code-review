def is_win(game):
    for row in game:
        if row[0] == row[1] == row[2] != ' ':
            return True
    for col in range(3):
        if game[0][col] == game[1][col] == game[2][col] != ' ':
            return True
    if game[0][0] == game[1][1] == game[2][2] != ' ':
        return True
    if game[0][2] == game[1][1] == game[2][0] != ' ':
        return True
    return False

def print_board(game):
    print("-------------")
    for row in game:
        print("|", " | ".join(row), "|")
        print("-------------")

def main():
    while True:
        game = [[' ' for _ in range(3)] for _ in range(3)]  
        player1 = 'X'
        player2 = 'O'
        turn = False  
        print("X = Player 1")
        print("O = Player 2")
        print_board(game)
        
        for n in range(9):
            current_player = player2 if turn else player1
            print(f"Player {current_player}: Which cell to mark? i:[1..3], j:[1..3]: ")
            try:
                i, j = map(int, input().split())
                i -= 1
                j -= 1
                if i < 0 or i >= 3 or j < 0 or j >= 3 or game[i][j] != ' ':
                    print("Invalid move! Try again.")
                    continue
                game[i][j] = current_player
            except ValueError:
                print("Invalid input! Please enter two numbers separated by a space.")
                continue
            
            print_board(game)
            
            if is_win(game):
                print(f"Player {current_player} wins!")
                break  
            
            turn = not turn  
        
        if not is_win(game):
            print("It's a tie!")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
    
