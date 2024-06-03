import random
import os

over = False
move_xy = 0
last = ""
rematch = True
scores = {"x": 0, "o": 0, "draw": 0}
move = random.choice(["X","O"])
valid_move = False
end = ["END", "CLOSE", "QUIT", "EXIT"]

#function for printing out the zone
def print_zone(zone, scores):
    os.system("cls")
    print(f"\n|---------|\n|Scores:  |\n|X: {scores['x']}     |\n|O: {scores['o']}     |\n|Draw: {scores['draw']}  |\n|---------|\n|---------|")
    print("|1 2 3 /  |")
    for n in range(3):
        for n2 in range(3):
            print(f"|{zone[n][n2]['cell']}", end="")
        print(f"| {n+1} |\n|---------|")
    print("")

while rematch == True:
    rematch = False
    zone = [[{"null": True, "cell": " "}, {"null": True, "cell": " "}, {"null": True, "cell": " "},], 
        [{"null": True, "cell": " "}, {"null": True, "cell": " "}, {"null": True, "cell": " "},], 
        [{"null": True, "cell": " "}, {"null": True, "cell": " "}, {"null": True, "cell": " "},] ]
    x = 0
    y = 0
    draw = 9

    #1 round
    while over != True:
        last = move
        print_zone(zone, scores)

        #placing the move
        choosing = True
        valid_move = False
        while choosing:
            while not valid_move:
                move_xy = input(f"Where do you want to place '{move}' : ")  #getting an answer
                if move_xy.upper() in end:                                  #quitting if wanted
                    exit()
                try:                                                        
                    move_xy = int(move_xy)                                  #checking valid move
                    if len(str(move_xy)) == 2:
                        valid_move = True
                    else:                                                   #invalid move
                        print_zone(zone, scores)
                        print("Invalod syntax. Correct from for placing your move is 'xy'\nx being the row, y being the column")
                except:
                    print_zone(zone, scores)
                    print("Invalod syntax. Correct from for placing your move is 'xy'\nx being the row, y being the column")
            x = int(str(move_xy)[0])-1                                  #placing the move into the zone if the choosen cell is available
            y = int(str(move_xy)[1])-1
            if zone[x][y]["null"] == True:                              #finalizing move
                zone[x][y]["cell"] = move
                zone[x][y]["null"] = False
                choosing = False
            else:                                                       #cell not available
                print_zone(zone, scores)
                print("That cell is already occupied, please choose again")   
                valid_move = False

        #scanning the surroundings
        for v in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            vektor_x = v[0]
            vektor_y = v[1]
            try:
                if zone[x+vektor_x][y+vektor_y]["cell"] == move:
                    break
            except:
                pass

        #checking for win condition
        try:
            if zone[x + (2 * vektor_x)][y + (2 * vektor_y)]["cell"] == move: 
                over = True
                print_zone(zone, scores)
                print(f"{move} won the round.")
        except:
            pass
        try:
            if zone[x - vektor_x][y - vektor_y]["cell"] == move:
                over = True
                print_zone(zone, scores)
                print(f"{move} won the round.")
        except:
            pass
    
        #scores
        if over and draw != 0:
            if move == "X":
                scores["x"] += 1
            else:
                scores["o"] += 1

        #draw
        if not over:
            for n in range(3):
                for n2 in range(3):
                    if zone[n][n2]['null'] == False:
                        draw -= 1
                    elif zone[n][n2]['null'] == True:
                        draw += 1
            if draw == 0:
                over = True
                print_zone(zone, scores)
                print("The round is draw.")
                scores["draw"] += 1

        #next move
        if last == "X":
            move = "O"
        else:
            move = "X"

    #starting next round
    while not rematch:
        answer = input("Do you want to play another round?\n   yes -> Y\n   no -> N\n")
        if answer.upper() == "Y":
            rematch = True
            over = False
        elif answer.upper() == "N" or answer.upper() in end:
            exit()
