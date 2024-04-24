import random
game=["__","__","__",
      "__","__","__",
      "__","__","__"]
current_player="x"
running_game=True
winner=None
def printgame(game):
    print(game[0] + "|" +game[1] + "|" + game[2] )
    print("_________")
    print(game[3] + "|" + game[4] + "|" + game[5])
    print("_________")
    print(game[6] + "|" + game[7] + "|" + game[8])
def player(game):
    inp=int(input("enter the value :"))
    if game[inp-1]=="__":
        game[inp-1]=current_player
    else:
        print("oops already player filled")

def horizontal(game):
    global winner
    if game[0]==game[1]==game[2] and game[0]!="__":
        winner=game[0]
        return True
    if game[3]==game[4]==game[5] and game[3]!="__":
        winner=game[0]
        return True
    if game[6]==game[7]==game[8] and game[6]!="__":
        winner=game[0]
        return True
def vertical(game):
    global winner
    if game[0] == game[3] == game[6] and game[0] != "__":
        winner = game[0]
        return True
    if game[1] == game[4] == game[7] and game[1] != "__":
        winner = game[0]
        return True
    if game[2] == game[5] == game[8] and game[2] != "__":
        winner = game[0]
        return True
def diag(game):
    global winner
    if game[0] == game[4] == game[8] and game[0] != "__":
        winner = game[0]
        return True
    if game[2] == game[4] == game[6] and game[2] != "__":
        winner = game[0]
        return True
def check_tie(game):
    global running_game
    if "__" not in game:
        printgame(game)
        print("it is tie")
        running_game=False
def winning(game):
    global running_game
    if horizontal(game):
        printgame(game)
        print(f"the winner is {winner}")
        running_game=False
    elif vertical(game):
        printgame(game)
        print(f"the winner is {winner}")
        running_game=False
    elif horizontal(game):
        printgame(game)
        print(f"the winner is {winner}")
        running_game=False
def switchplayyer(game):
    global current_player
    if current_player=="x":
        current_player="0"
    else:
        current_player="x"
def computer(game):
    while current_player=="0":
        position=random.randint(0,8)
        if game[position]=="__":
            game[position]="0"
        switchplayyer(game)
while running_game:
    printgame(game)
    player(game)
    horizontal(game)
    vertical(game)
    diag(game)
    check_tie(game)
    switchplayyer(game)
    computer(game)
    winning(game)


