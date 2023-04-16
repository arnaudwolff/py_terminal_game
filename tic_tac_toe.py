import numpy as np

greetings = """ 
Greetings! 
Today you will play a game of Tic Tac Toe. 
The game is played between two players on a three-by-three grid.
Players take turns, and at each turn, the player has to mark one space in the grid with X or O.
The player who succeeds in placing three Xs or Os in a horizontal, vertical, or diagonal row is the winner.
"""

print(greetings)

player_names = "We will start by getting your names."

print(player_names)
print("\n")

player_1 = input("What is Player 1's name? ")
player_2 = input("What is Player 2's name? ")

print("\n")
print("Hi " + player_1 + " and " + player_2 + "! We hope you are ready to enjoy the game!")

print("""
This is how we will proceed.

Since we play on a three-by-three grid, the nine locations will be defined in the following way:
- The upper row will have three locations: UL (upper-left), UM (upper-middle) and UR (upper-right).
- The middle row will have three locations: ML (middle-left), MM (middle-middle) and MR (middle-right).
- The lower row will have three locations: LL (lower-left), LM (lower-middle) and LR (lower-right).

The first player to play will pick a mark (either X or O) and a location (e.g., UL) on the grid.
Then, the second player will be attributed the other mark (e.g., X if player 1 chose O), and will choose an empty location on the grid (e.g., MR).
The game will continue until a player wins, or there are no empty locations left on the grid.
""")

marks = ["X", "O"]
locations = ["UL", "UM", "UR", "ML", "MM", "MR", "LL", "LM", "LR"]
available_locations = [i for i in locations]
grid = [["","",""], ["","",""], ["","",""]]
grid_array = np.array(grid)


first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")

first_player = input("So, who plays first? " + player_1 + " or " + player_2 + "? ")

while (first_player != player_1) and (first_player != player_2):
    print("""
    I am sorry, the name that you have entered does not match either of the players' names.
    Please enter an appropriate name (be careful about capitalization).
    """) 
    first_player = input("Who plays first? " + player_1 + " or " + player_2 + "? ")

print("\n")

if first_player == player_1:
    mark_p1 = input(player_1 + ", what mark have you chosen? ")
    while mark_p1 not in marks:
        print("""
    I am sorry, this is not an appropriate mark.
    Please choose between X and O).
    """) 
        mark_p1 = input(player_1 + ", what mark have you chosen? ")
    first_turn_p1 = input(player_1 + ", where's your first mark on the grid? ")
    while first_turn_p1 not in available_locations:
        print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
        first_turn_p1 = input(player_1 + ", where's your first mark on the grid? ")
    available_locations.remove(first_turn_p1)
    if first_turn_p1 == "UL":
        grid_array[0][0] = mark_p1
    elif first_turn_p1 == "UM":
        grid_array[0][1] = mark_p1
    elif first_turn_p1 == "UR":
        grid_array[0][2] = mark_p1 
    elif first_turn_p1 == "ML":
        grid_array[1][0] = mark_p1  
    elif first_turn_p1 == "MM":
        grid_array[1][1] = mark_p1
    elif first_turn_p1 == "MR":
        grid_array[1][2] = mark_p1
    elif first_turn_p1 == "LL":
        grid_array[2][0] = mark_p1  
    elif first_turn_p1 == "LM":
        grid_array[2][1] = mark_p1
    elif first_turn_p1 == "LR":
        grid_array[2][2] = mark_p1  
        
    print("\n")
    print(grid_array)
    print("\n")

    first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
    second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
    third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
    fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
    fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
    sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
    seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
    eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")

    second_player = player_2
    remaining_mark = []
    for i in marks:
        if i != mark_p1:
            remaining_mark.append(i)
    mark_p2 = remaining_mark[0]   
    print(second_player + ", now it's your turn! You have been attributed the " + mark_p2 + " mark.")
    second_turn_p2 = input("What remaining location on the grid do you choose? ")
    while second_turn_p2 not in available_locations:
        print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
        second_turn_p2 = input("What remaining location on the grid do you choose? ")
    available_locations.remove(second_turn_p2)
    if second_turn_p2 == "UL":
        grid_array[0][0] = mark_p2
    elif second_turn_p2 == "UM":
        grid_array[0][1] = mark_p2
    elif second_turn_p2 == "UR":
        grid_array[0][2] = mark_p2 
    elif second_turn_p2 == "ML":
        grid_array[1][0] = mark_p2  
    elif second_turn_p2 == "MM":
        grid_array[1][1] = mark_p2
    elif second_turn_p2 == "MR":
        grid_array[1][2] = mark_p2
    elif second_turn_p2 == "LL":
        grid_array[2][0] = mark_p2  
    elif second_turn_p2 == "LM":
        grid_array[2][1] = mark_p2
    elif second_turn_p2 == "LR":
        grid_array[2][2] = mark_p2

    print("\n")
    print(grid_array)
    print("\n")

    first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
    second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
    third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
    fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
    fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
    sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
    seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
    eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")
    third_player = player_1
    print(third_player + ", your turn again.")
    third_turn_p1 = input("What remaining location on the grid do you choose? ")
    while third_turn_p1 not in available_locations:
        print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
        third_turn_p1 = input("What remaining location on the grid do you choose? ")
    available_locations.remove(third_turn_p1)
    if third_turn_p1 == "UL":
        grid_array[0][0] = mark_p1
    elif third_turn_p1 == "UM":
        grid_array[0][1] = mark_p1
    elif third_turn_p1 == "UR":
        grid_array[0][2] = mark_p1 
    elif third_turn_p1 == "ML":
        grid_array[1][0] = mark_p1  
    elif third_turn_p1 == "MM":
        grid_array[1][1] = mark_p1
    elif third_turn_p1 == "MR":
        grid_array[1][2] = mark_p1
    elif third_turn_p1 == "LL":
        grid_array[2][0] = mark_p1  
    elif third_turn_p1 == "LM":
        grid_array[2][1] = mark_p1
    elif third_turn_p1 == "LR":
        grid_array[2][2] = mark_p1  
    
    
    print("\n")
    print(grid_array)
    print("\n")

    first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
    second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
    third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
    fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
    fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
    sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
    seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
    eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")

    fourth_player = player_2
    print(fourth_player + ", your turn.")
    fourth_turn_p2 = input("What remaining location on the grid do you choose? ")
    while fourth_turn_p2 not in available_locations:
        print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
        fourth_turn_p2 = input("What remaining location on the grid do you choose? ")
    available_locations.remove(fourth_turn_p2)
    if fourth_turn_p2 == "UL":
        grid_array[0][0] = mark_p2
    elif fourth_turn_p2 == "UM":
        grid_array[0][1] = mark_p2
    elif fourth_turn_p2 == "UR":
        grid_array[0][2] = mark_p2 
    elif fourth_turn_p2 == "ML":
        grid_array[1][0] = mark_p2  
    elif fourth_turn_p2 == "MM":
        grid_array[1][1] = mark_p2
    elif fourth_turn_p2 == "MR":
        grid_array[1][2] = mark_p2
    elif fourth_turn_p2 == "LL":
        grid_array[2][0] = mark_p2  
    elif fourth_turn_p2 == "LM":
        grid_array[2][1] = mark_p2
    elif fourth_turn_p2 == "LR":
        grid_array[2][2] = mark_p2

    print("\n")
    print(grid_array)
    print("\n")

    first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
    second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
    third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
    fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
    fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
    sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
    seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
    eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")
    
    fifth_player = player_1
    print(fifth_player + ", your turn.")
    fifth_turn_p1 = input("What remaining location on the grid do you choose? ")
    while fifth_turn_p1 not in available_locations:
        print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
        fifth_turn_p1 = input("What remaining location on the grid do you choose? ")
    available_locations.remove(fifth_turn_p1)
    if fifth_turn_p1 == "UL":
        grid_array[0][0] = mark_p1
    elif fifth_turn_p1 == "UM":
        grid_array[0][1] = mark_p1
    elif fifth_turn_p1 == "UR":
        grid_array[0][2] = mark_p1 
    elif fifth_turn_p1 == "ML":
        grid_array[1][0] = mark_p1  
    elif fifth_turn_p1 == "MM":
        grid_array[1][1] = mark_p1
    elif fifth_turn_p1 == "MR":
        grid_array[1][2] = mark_p1
    elif fifth_turn_p1 == "LL":
        grid_array[2][0] = mark_p1  
    elif fifth_turn_p1 == "LM":
        grid_array[2][1] = mark_p1
    elif fifth_turn_p1 == "LR":
        grid_array[2][2] = mark_p1 

    print("\n")
    print(grid_array)
    print("\n")

    first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
    second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
    third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
    fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
    fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
    sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
    seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
    eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")


    last_player = fifth_player

    if ((first_win == True) or (second_win == True) or (third_win == True) or (fourth_win == True) or ((fifth_win == True)) or (sixth_win == True) or (seventh_win == True) or (eighth_win == True)):
        print("Congratulations " + last_player + "! You won the game!" )
    else: 
        sixth_player = player_2
        print(sixth_player + ", your turn.")
        sixth_turn_p2 = input("What remaining location on the grid do you choose? ")
        while sixth_turn_p2 not in available_locations:
            print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
            sixth_turn_p2 = input("What remaining location on the grid do you choose? ")
        available_locations.remove(sixth_turn_p2) 
        if sixth_turn_p2 == "UL":
            grid_array[0][0] = mark_p2
        elif sixth_turn_p2 == "UM":
            grid_array[0][1] = mark_p2
        elif sixth_turn_p2 == "UR":
            grid_array[0][2] = mark_p2 
        elif sixth_turn_p2 == "ML":
            grid_array[1][0] = mark_p2  
        elif sixth_turn_p2 == "MM":
            grid_array[1][1] = mark_p2
        elif sixth_turn_p2 == "MR":
            grid_array[1][2] = mark_p2
        elif sixth_turn_p2 == "LL":
            grid_array[2][0] = mark_p2  
        elif sixth_turn_p2 == "LM":
            grid_array[2][1] = mark_p2
        elif sixth_turn_p2 == "LR":
            grid_array[2][2] = mark_p2

        print("\n")
        print(grid_array)
        print("\n")

        first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
        second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
        third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
        fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
        fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
        sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
        seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
        eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")


        last_player = sixth_player

        if ((first_win == True) or (second_win == True) or (third_win == True) or (fourth_win == True) or ((fifth_win == True)) or (sixth_win == True) or (seventh_win == True) or (eighth_win == True)):
            print("Congratulations " + last_player + "! You won the game!" )
        else:
            seventh_player = player_1
            print(seventh_player + ", your turn.")
            seventh_turn_p1 = input("What remaining location on the grid do you choose? ")
            while seventh_turn_p1 not in available_locations:
                print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
                seventh_turn_p1 = input("What remaining location on the grid do you choose? ")
            available_locations.remove(seventh_turn_p1)
            if seventh_turn_p1 == "UL":
                grid_array[0][0] = mark_p1
            elif seventh_turn_p1 == "UM":
                grid_array[0][1] = mark_p1
            elif seventh_turn_p1 == "UR":
                grid_array[0][2] = mark_p1 
            elif seventh_turn_p1 == "ML":
                grid_array[1][0] = mark_p1  
            elif seventh_turn_p1 == "MM":
                grid_array[1][1] = mark_p1
            elif seventh_turn_p1 == "MR":
                grid_array[1][2] = mark_p1
            elif seventh_turn_p1 == "LL":
                grid_array[2][0] = mark_p1  
            elif seventh_turn_p1 == "LM":
                grid_array[2][1] = mark_p1
            elif seventh_turn_p1 == "LR":
                grid_array[2][2] = mark_p1 

            print("\n")
            print(grid_array)
            print("\n")

            first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
            second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
            third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
            fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
            fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
            sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
            seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
            eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")


            last_player = seventh_player

            if ((first_win == True) or (second_win == True) or (third_win == True) or (fourth_win == True) or ((fifth_win == True)) or (sixth_win == True) or (seventh_win == True) or (eighth_win == True)):
                print("Congratulations " + last_player + "! You won the game!" )
            else:
                eighth_player = player_2
                print(eighth_player + ", your turn.")
                eighth_turn_p2 = input("What remaining location on the grid do you choose? ")
                while eighth_turn_p2 not in available_locations:
                    print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
                    eighth_turn_p2 = input("What remaining location on the grid do you choose? ")
                available_locations.remove(eighth_turn_p2)
                if eighth_turn_p2 == "UL":
                    grid_array[0][0] = mark_p2
                elif eighth_turn_p2 == "UM":
                    grid_array[0][1] = mark_p2
                elif eighth_turn_p2 == "UR":
                    grid_array[0][2] = mark_p2 
                elif eighth_turn_p2 == "ML":
                    grid_array[1][0] = mark_p2  
                elif eighth_turn_p2 == "MM":
                    grid_array[1][1] = mark_p2
                elif eighth_turn_p2 == "MR":
                    grid_array[1][2] = mark_p2
                elif eighth_turn_p2 == "LL":
                    grid_array[2][0] = mark_p2  
                elif eighth_turn_p2 == "LM":
                    grid_array[2][1] = mark_p2
                elif eighth_turn_p2 == "LR":
                    grid_array[2][2] = mark_p2

                print("\n")
                print(grid_array)
                print("\n")

                first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
                second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
                third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
                fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
                fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
                sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
                seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
                eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")


                last_player = eighth_player

                if ((first_win == True) or (second_win == True) or (third_win == True) or (fourth_win == True) or ((fifth_win == True)) or (sixth_win == True) or (seventh_win == True) or (eighth_win == True)):
                    print("Congratulations " + last_player + "! You won the game!" )
                else: 
                    ninth_player = player_1
                    print(ninth_player + ", your turn.")
                    ninth_turn_p1 = input("What remaining location on the grid do you choose? ")
                    while ninth_turn_p1 not in available_locations:
                        print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
                        ninth_turn_p1 = input("What remaining location on the grid do you choose? ")
                    available_locations.remove(ninth_turn_p1)
                    if ninth_turn_p1 == "UL":
                        grid_array[0][0] = mark_p1
                    elif ninth_turn_p1 == "UM":
                        grid_array[0][1] = mark_p1
                    elif ninth_turn_p1 == "UR":
                        grid_array[0][2] = mark_p1 
                    elif ninth_turn_p1 == "ML":
                        grid_array[1][0] = mark_p1  
                    elif ninth_turn_p1 == "MM":
                        grid_array[1][1] = mark_p1
                    elif ninth_turn_p1 == "MR":
                        grid_array[1][2] = mark_p1
                    elif ninth_turn_p1 == "LL":
                        grid_array[2][0] = mark_p1  
                    elif ninth_turn_p1 == "LM":
                        grid_array[2][1] = mark_p1
                    elif ninth_turn_p1 == "LR":
                        grid_array[2][2] = mark_p1

                    print("\n")
                    print(grid_array)
                    print("\n")

                    first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
                    second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
                    third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
                    fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
                    fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
                    sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
                    seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
                    eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")

                    last_player = ninth_player

                    if ((first_win == True) or (second_win == True) or (third_win == True) or (fourth_win == True) or ((fifth_win == True)) or (sixth_win == True) or (seventh_win == True) or (eighth_win == True)):
                        print("Congratulations " + last_player + "! You won the game!" )
                    else:
                        print("The game has ended without any player winning. We still hope you had fun playing the game!")    

elif first_player == player_2:
    mark_p2 = input(player_2 + ", what mark have you chosen? ")
    while mark_p2 not in marks:
        print("""
    I am sorry, this is not an appropriate mark.
    Please choose between X and O).
    """) 
        mark_p2 = input(player_2 + ", what mark have you chosen? ")
    first_turn_p2 = input(player_2 + ", where's your first mark on the grid? ")
    while first_turn_p2 not in available_locations:
        print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".")
        first_turn_p2 = input(player_2 + ", where's your first mark on the grid? ")
    available_locations.remove(first_turn_p2)
    if first_turn_p2 == "UL":
        grid_array[0][0] = mark_p2
    elif first_turn_p2 == "UM":
        grid_array[0][1] = mark_p2
    elif first_turn_p2 == "UR":
        grid_array[0][2] = mark_p2
    elif first_turn_p2 == "ML":
        grid_array[1][0] = mark_p2  
    elif first_turn_p2 == "MM":
        grid_array[1][1] = mark_p2
    elif first_turn_p2 == "MR":
        grid_array[1][2] = mark_p2
    elif first_turn_p2 == "LL":
        grid_array[2][0] = mark_p2 
    elif first_turn_p2 == "LM":
        grid_array[2][1] = mark_p2
    elif first_turn_p2 == "LR":
        grid_array[2][2] = mark_p2

    print("\n")
    print(grid_array)
    print("\n") 

    first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
    second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
    third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
    fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
    fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
    sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
    seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
    eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")
    
    second_player = player_1
    remaining_mark = []
    for i in marks:
        if i != mark_p2:
            remaining_mark.append(i)
    mark_p1 = remaining_mark[0]        
    print(second_player + ", now it's your turn! You have been attributed the " + mark_p1 + " mark.")
    second_turn_p1 = input("What remaining location on the grid do you choose? ")
    while second_turn_p1 not in available_locations:
        print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
        second_turn_p1 = input("What remaining location on the grid do you choose? ")
    available_locations.remove(second_turn_p1)
    if second_turn_p1 == "UL":
        grid_array[0][0] = mark_p1
    elif second_turn_p1 == "UM":
        grid_array[0][1] = mark_p1
    elif second_turn_p1 == "UR":
        grid_array[0][2] = mark_p1
    elif second_turn_p1 == "ML":
        grid_array[1][0] = mark_p1  
    elif second_turn_p1 == "MM":
        grid_array[1][1] = mark_p1
    elif second_turn_p1 == "MR":
        grid_array[1][2] = mark_p1
    elif second_turn_p1 == "LL":
        grid_array[2][0] = mark_p1 
    elif second_turn_p1 == "LM":
        grid_array[2][1] = mark_p1
    elif second_turn_p1 == "LR":
        grid_array[2][2] = mark_p1  
    
    print("\n")
    print(grid_array)
    print("\n")

    first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
    second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
    third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
    fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
    fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
    sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
    seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
    eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")


    third_player = player_2
    print(third_player + ", your turn again.")
    third_turn_p2 = input("What remaining location on the grid do you choose? ")
    while third_turn_p2 not in available_locations:
        print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
        third_turn_p2 = input("What remaining location on the grid do you choose? ")
    available_locations.remove(third_turn_p2)
    if third_turn_p2 == "UL":
        grid_array[0][0] = mark_p2
    elif third_turn_p2 == "UM":
        grid_array[0][1] = mark_p2
    elif third_turn_p2 == "UR":
        grid_array[0][2] = mark_p2
    elif third_turn_p2 == "ML":
        grid_array[1][0] = mark_p2  
    elif third_turn_p2 == "MM":
        grid_array[1][1] = mark_p2
    elif third_turn_p2 == "MR":
        grid_array[1][2] = mark_p2
    elif third_turn_p2 == "LL":
        grid_array[2][0] = mark_p2 
    elif third_turn_p2 == "LM":
        grid_array[2][1] = mark_p2
    elif third_turn_p2 == "LR":
        grid_array[2][2] = mark_p2

    print("\n")
    print(grid_array)
    print("\n")

    first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
    second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
    third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
    fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
    fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
    sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
    seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
    eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")

    fourth_player = player_1
    print(fourth_player + ", your turn.")
    fourth_turn_p1 = input("What remaining location on the grid do you choose? ")
    while fourth_turn_p1 not in available_locations:
        print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
        fourth_turn_p1 = input("What remaining location on the grid do you choose? ")
    available_locations.remove(fourth_turn_p1)
    if fourth_turn_p1 == "UL":
        grid_array[0][0] = mark_p1
    elif fourth_turn_p1 == "UM":
        grid_array[0][1] = mark_p1
    elif fourth_turn_p1 == "UR":
        grid_array[0][2] = mark_p1
    elif fourth_turn_p1 == "ML":
        grid_array[1][0] = mark_p1  
    elif fourth_turn_p1 == "MM":
        grid_array[1][1] = mark_p1
    elif fourth_turn_p1 == "MR":
        grid_array[1][2] = mark_p1
    elif fourth_turn_p1 == "LL":
        grid_array[2][0] = mark_p1 
    elif fourth_turn_p1 == "LM":
        grid_array[2][1] = mark_p1
    elif fourth_turn_p1 == "LR":
        grid_array[2][2] = mark_p1 

    print("\n")
    print(grid_array)
    print("\n")

    first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
    second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
    third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
    fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
    fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
    sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
    seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
    eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")
    
    fifth_player = player_2
    print(fourth_player + ", your turn.")
    fifth_turn_p2 = input("What remaining location on the grid do you choose? ")
    while fifth_turn_p2 not in available_locations:
        print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
        fifth_turn_p2 = input("What remaining location on the grid do you choose? ")
    available_locations.remove(fifth_turn_p2)  
    if fifth_turn_p2 == "UL":
        grid_array[0][0] = mark_p2
    elif fifth_turn_p2 == "UM":
        grid_array[0][1] = mark_p2
    elif fifth_turn_p2 == "UR":
        grid_array[0][2] = mark_p2
    elif fifth_turn_p2 == "ML":
        grid_array[1][0] = mark_p2  
    elif fifth_turn_p2 == "MM":
        grid_array[1][1] = mark_p2
    elif fifth_turn_p2 == "MR":
        grid_array[1][2] = mark_p2
    elif fifth_turn_p2 == "LL":
        grid_array[2][0] = mark_p2 
    elif fifth_turn_p2 == "LM":
        grid_array[2][1] = mark_p2
    elif fifth_turn_p2 == "LR":
        grid_array[2][2] = mark_p2

    print("\n")
    print(grid_array)
    print("\n")

    first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
    second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
    third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
    fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
    fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
    sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
    seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
    eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")

    last_player = fifth_player

    if ((first_win == True) or (second_win == True) or (third_win == True) or (fourth_win == True) or ((fifth_win == True)) or (sixth_win == True) or (seventh_win == True) or (eighth_win == True)):
        print("Congratulations " + last_player + "! You won the game!" )
    else: 
        sixth_player = player_1
        print(sixth_player + ", your turn.")
        sixth_turn_p1 = input("What remaining location on the grid do you choose? ")
        while sixth_turn_p1 not in available_locations:
            print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
            sixth_turn_p1 = input("What remaining location on the grid do you choose? ")
        available_locations.remove(sixth_turn_p1)
        if sixth_turn_p1 == "UL":
            grid_array[0][0] = mark_p1
        elif sixth_turn_p1 == "UM":
            grid_array[0][1] = mark_p1
        elif sixth_turn_p1 == "UR":
            grid_array[0][2] = mark_p1
        elif sixth_turn_p1 == "ML":
            grid_array[1][0] = mark_p1  
        elif sixth_turn_p1 == "MM":
            grid_array[1][1] = mark_p1
        elif sixth_turn_p1 == "MR":
            grid_array[1][2] = mark_p1
        elif sixth_turn_p1 == "LL":
            grid_array[2][0] = mark_p1 
        elif sixth_turn_p1 == "LM":
            grid_array[2][1] = mark_p1
        elif sixth_turn_p1 == "LR":
            grid_array[2][2] = mark_p1

        print("\n")
        print(grid_array)
        print("\n")

        first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
        second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
        third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
        fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
        fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
        sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
        seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
        eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")

        last_player = sixth_player

        if ((first_win == True) or (second_win == True) or (third_win == True) or (fourth_win == True) or ((fifth_win == True)) or (sixth_win == True) or (seventh_win == True) or (eighth_win == True)):
            print("Congratulations " + last_player + "! You won the game!" )
        else:
            seventh_player = player_2
            print(seventh_player + ", your turn.")
            seventh_turn_p2 = input("What remaining location on the grid do you choose? ")
            while seventh_turn_p2 not in available_locations:
                print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
                seventh_turn_p2 = input("What remaining location on the grid do you choose? ")
            available_locations.remove(seventh_turn_p2) 
            if seventh_turn_p2 == "UL":
                grid_array[0][0] = mark_p2
            elif seventh_turn_p2 == "UM":
                grid_array[0][1] = mark_p2
            elif seventh_turn_p2 == "UR":
                grid_array[0][2] = mark_p2
            elif seventh_turn_p2 == "ML":
                grid_array[1][0] = mark_p2  
            elif seventh_turn_p2 == "MM":
                grid_array[1][1] = mark_p2
            elif seventh_turn_p2 == "MR":
                grid_array[1][2] = mark_p2
            elif seventh_turn_p2 == "LL":
                grid_array[2][0] = mark_p2 
            elif seventh_turn_p2 == "LM":
                grid_array[2][1] = mark_p2
            elif seventh_turn_p2 == "LR":
                grid_array[2][2] = mark_p2

            print("\n")
            print(grid_array)
            print("\n")

            first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
            second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
            third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
            fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
            fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
            sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
            seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
            eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")

            last_player = seventh_player

            if ((first_win == True) or (second_win == True) or (third_win == True) or (fourth_win == True) or ((fifth_win == True)) or (sixth_win == True) or (seventh_win == True) or (eighth_win == True)):
                print("Congratulations " + last_player + "! You won the game!" )
            else:
                eighth_player = player_1
                print(eighth_player + ", your turn.")
                eighth_turn_p1 = input("What remaining location on the grid do you choose? ")
                while eighth_turn_p1 not in available_locations:
                    print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
                    eighth_turn_p1 = input("What remaining location on the grid do you choose? ")
                available_locations.remove(eighth_turn_p1)
                if eighth_turn_p1 == "UL":
                    grid_array[0][0] = mark_p1
                elif eighth_turn_p1 == "UM":
                    grid_array[0][1] = mark_p1
                elif eighth_turn_p1 == "UR":
                    grid_array[0][2] = mark_p1
                elif eighth_turn_p1 == "ML":
                    grid_array[1][0] = mark_p1  
                elif eighth_turn_p1 == "MM":
                    grid_array[1][1] = mark_p1
                elif eighth_turn_p1 == "MR":
                    grid_array[1][2] = mark_p1
                elif eighth_turn_p1 == "LL":
                    grid_array[2][0] = mark_p1 
                elif eighth_turn_p1 == "LM":
                    grid_array[2][1] = mark_p1
                elif eighth_turn_p1 == "LR":
                    grid_array[2][2] = mark_p1

                print("\n")
                print(grid_array)
                print("\n")

                first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
                second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
                third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
                fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
                fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
                sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
                seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
                eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")

                last_player = eighth_player
                
                if ((first_win == True) or (second_win == True) or (third_win == True) or (fourth_win == True) or ((fifth_win == True)) or (sixth_win == True) or (seventh_win == True) or (eighth_win == True)):
                    print("Congratulations " + last_player + "! You won the game!" )
                else:
                    ninth_player = player_2
                    print(ninth_player + ", your turn.")
                    ninth_turn_p2 = input("What remaining location on the grid do you choose? ")
                    while ninth_turn_p2 not in available_locations:
                        print("I am sorry, this is not an appropriate location. Please choose between " + ", ".join(available_locations)+ ".") 
                        ninth_turn_p2 = input("What remaining location on the grid do you choose? ")
                    available_locations.remove(ninth_turn_p2)  
                    if ninth_turn_p2 == "UL":
                        grid_array[0][0] = mark_p2
                    elif ninth_turn_p2 == "UM":
                        grid_array[0][1] = mark_p2
                    elif ninth_turn_p2 == "UR":
                        grid_array[0][2] = mark_p2
                    elif ninth_turn_p2 == "ML":
                        grid_array[1][0] = mark_p2  
                    elif ninth_turn_p2 == "MM":
                        grid_array[1][1] = mark_p2
                    elif ninth_turn_p2 == "MR":
                        grid_array[1][2] = mark_p2
                    elif ninth_turn_p2 == "LL":
                        grid_array[2][0] = mark_p2 
                    elif ninth_turn_p2 == "LM":
                        grid_array[2][1] = mark_p2
                    elif ninth_turn_p2 == "LR":
                        grid_array[2][2] = mark_p2

                    print("\n")
                    print(grid_array)
                    print("\n")    

                    first_win = np.all(grid_array[0] == "X") or np.all(grid_array[0] == "O")
                    second_win = np.all(grid_array[1] == "X") or np.all(grid_array[1] == "O")
                    third_win = np.all(grid_array[2] == "X") or np.all(grid_array[2] == "O")
                    fourth_win = np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][0], grid_array[2][0]]) == "O")
                    fifth_win = np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "X") or np.all(np.array([grid_array[0][1], grid_array[1][1], grid_array[2][1]]) == "O")
                    sixth_win = np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][2], grid_array[1][2], grid_array[2][2]]) == "O")
                    seventh_win = np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "X") or np.all(np.array([grid_array[0][0], grid_array[1][1], grid_array[2][2]]) == "O")
                    eighth_win = np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "X") or np.all(np.array([grid_array[2][0], grid_array[1][1], grid_array[0][2]]) == "O")

                    last_player = ninth_player

                    if ((first_win == True) or (second_win == True) or (third_win == True) or (fourth_win == True) or ((fifth_win == True)) or (sixth_win == True) or (seventh_win == True) or (eighth_win == True)):
                        print("Congratulations " + last_player + "! You won the game!" )
                    else:
                        print("The game has ended without any player winning. We still hope you had fun playing the game!")  