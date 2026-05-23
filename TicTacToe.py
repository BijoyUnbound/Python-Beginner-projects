import random, time

def show_board(board: list) -> None:
    print("-"*13)
    print("0  1  2  3\n")
    for k in range(1, 4):
        print(f"{k}  {"  ".join(board[k-1])}\n")
        
def is_win(board: list, player: str) -> bool:
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == player:
        return True   
    for k in range(3):
        if board[k][0] == board[k][1] == board[k][2] == player:
                return True
        elif board[0][k] == board[1][k] == board[2][k] == player:
                return True    
    return False
              
def is_draw(board: list) -> bool:
    for i in range(3):
        if "-" in board[i]:
            return False
    return True

print(a := "-:| Tic Tac Toe |:-")
print("-"*len(a))     
print()   

computer_choices = [f"{k}, {j}" for k in range(1, 4) for j in range(1, 4)]   
board = [["-" for x in range(1, 4)] for i in range(1, 4)]

players = ["X", "O"]
choose_player = input("Choose one(X or O): ").upper()
if choose_player not in players:
    raise ValueError("Only X or O are allowed!\nRestart to continue!!")
players.remove(choose_player)

print("\n-:| Board |:-")
show_board(board)
player = "X"
turns = 1

while True:
    if turns % 2 != 0:
        player = choose_player
        move = input(f"Player {player} enter row, collum: ")
        if move not in computer_choices:
            print("Unavailable spot!!!\n")
            continue
        computer_choices.remove(move)
            
    else:
        player = players[0]
        print(f"Player {player} Choosing...\n")
        time.sleep(1)
        move = random.choice(computer_choices)
        computer_choices.remove(move)
                
    row, col = move.split(", ")
    
    row = int(row)-1
    col = int(col)-1
        
    board[row][col] = player
    print("-:| Board |:-")
    show_board(board)
    turns += 1
    
    if is_win(board, player):
        print("-:| Board |:-")
        show_board(board)
        print(f"Player {player} Wins!")
        break
        
    elif is_draw(board):
        print("-:| Board |:-")
        show_board(board)
        print(f"It's a Draw between X and O")
        break