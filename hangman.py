import random
def hangman(word):
    wrong=0
    stages=["",
            "_____      ",
            "|          ",
            "|    |     ",
            "|    0     ",
            "|   /|\    ",
            "|   / \    ",
            "|          ",
            ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("Welcome to the hangman")

    while wrong<len(stages)-1:
        ans=input("guess a letter:")
        if ans in rletters:
            lot=rletters.index(ans)
            board[lot]=ans
            rletters[lot]= "@"
        else:
            wrong+=1
        print("\n".join(stages[0:wrong+1])+"\n"+" ".join(board))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose!正解は{}".format(word))
x=["egg","cat","school","game","kitchen","rugby","shower","bed","window"]
tw=x[random.randint(0,8)]
hangman(tw)
