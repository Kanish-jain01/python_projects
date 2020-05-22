def Start(play):
    print("\nYou can quit the game by entering 'Q'\n")
    c=0
    re=0
    while(c<4):
        print("\nThis is the turn of Player",play)
        print("\nPlease enter where you want to navigate\n")
        print("\nYou can navigate in 4 directions now\n")
        print("\nUp, down, left and right\n")
        visited=[]
        nav=input()
        nav=nav.upper()

        if(nav=="U"and nav not in visited):
            visited.append("U")
            re=navup(play)
        elif(nav=="L" and nav not in visited):
            visited.append("L")
            re=navup(play)
        elif(nav=="D" and nav not in visited):
            visited.append("D")
            re=navup(play)
        elif(nav=="R" and nav not in visited):
            visited.append("R")
            re=navup(play)
        elif(nav=="Q"):
                break        
        else:
            print("\nYou have visited this riddle\n")
            c=c-1
        c+=1
    return re

def navup(play):
    print("\nNow where do you want to go \n")
    print("\nYou can quit the game by entering 'Q'\n")
    print("\nYou can navigate in 3 directions now\n")
    print("\nUp, left and right\n")
    answers=["answer1","answer2","answer3"]                #declaring variables    
    points=0
    count=0
    visited=[]                       
    while(count<3):
        print("\nWhere do you want to navigate next?\n")
        navig=input()
        navig=navig.upper()
        if(navig=="U" and navig not in visited):
            print("\nThis is riddle 1\n")
            visited.append("U")
            answer=input()
            if(answer==answers[0]):
                points+=1
                print("\nCorrect Answer\n")
            else:
                print("\nIncorrect Answer\n")
        elif(navig=="L" and navig not in visited):
            print("\nThis is riddle 2\n")
            visited.append("L")
            answer=input()
            if(answer==answers[1]):
                points+=1
                print("\nCorrect Answer\n")
            else:
                print("\nIncorrect Answer\n")
        elif(navig=="R" and navig not in visited):
            print("\nThis is riddle 3\n")
            visited.append("R")
            answer=input()
            if(answer==answers[2]):
                points+=1
                print("\nCorrect Answer\n")
            else:
                print("\nIncorrect Answer\n")
        elif(navig=="Q"):
            print("\nThis is the end of game of player",play)
            return 0
        else:
            print("\nYou have visited this riddle\n")
            count=count-1
        count=count+1    
    print("\nYou have visited all the riddles\n")
    point(points)
    return 0

def point(points):
    print("\nPlayer ",play," has secured ",points," points\n")
        
# this is the main part
print("Welcome to text based adventure")
print("\nInstructions\n")
print("\n1.You are in center of a room and can move two rooms further \n2. Then solve riddles in the room and return to center\n3. The fastest to solve wins")
print("\nThe navigation keys are:\nU for up\nd for down\nl for left\nr for right\n")
print("\nNumber of players:")
players=int(input())
play=1
ret=0
while(players>0):
    ret=Start(play)
    players=players-1
    play+=1



