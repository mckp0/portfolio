"""
MOns-T.E.H. Run
by Michael Chun
readme.txt for instructions to run this game
gamedoc.pdf for documentation
"""

# Import python libraries
import random
import time
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Define functions
def introduction():
    welcome_message = "Welcome to MOns-T.E.H. Run.\nType 'Start' to play story mode!\nType 'Arcade' for Arcade mode! "
    while True: 
        start_game = input(welcome_message)
        start_game = start_game.lower()
        if start_game == "start":
            time.sleep(1)
            print("*Floor Rumbles*")
            time.sleep(1)
            print("PW : Hey you! What are you doing just standing there!? Quick we gotta run!")
            time.sleep(4)
            print("Player : Whaaat? What's going on? Who are you?")
            time.sleep(3)
            print("*Floor Rumbles*")
            time.sleep(1)
            print("PW : You can call me PW, and that rumbling you hear, is the destroyer of worlds. His name is..")
            time.sleep(3)
            print("PW : MOns-T.E.H.")
            time.sleep(2)
            print("PW : Quick! Theres no time, we gotta run. Look, theres a series of bridges ahead that we can cross to escape the MOns-T.E.H.")
            time.sleep(3)
            print("PW : But he's smart. He's replaced some of the tiles with fakes!")
            time.sleep(3)
            print("PW : If you fall, you will lose a life and restart at the start of the bridge.")
            time.sleep(3)
            print("PW : Type Up, Down, Left or Right to move your character across the bridge.")
            time.sleep(3)
            print("PW : After each move, you'll get to see where you are. Close the display window to continue moving.")
            time.sleep(3)
            print("PW : Don't get caught by the MOns-T.E.H. Good luck!")
            time.sleep(3)
            arcade = False
            break
        elif start_game == 'arcade':
            arcade = True
            break
        else:
            print("Key in a valid gamemode!")        
    return arcade
    
def difficulty_level_selector():
    # Defining input messages
    difficulty_message = "Choose your difficulty level: Easy, Normal, Hard, Extreme. "
    failure_message = "Oops! You have input an invalid difficulty level."
    board_size = 0
    # Getting difficulty level input and assigning respective board sizes
    while board_size == 0:
        difficulty_level = input(difficulty_message)
        difficulty_level = difficulty_level.lower()
        if difficulty_level == "easy":
           board_size = 3
        elif difficulty_level == "normal":
            board_size = 4
        elif difficulty_level == "hard":
            board_size = 5
        elif difficulty_level == "extreme":
            board_size = 6
        else:
            print(failure_message)
    return board_size

# Generate Random Start and End Points
def generate_start_end_coord(board_size):
    start_coord = random.randint(0,board_size-1)
    end_coord = random.randint(0,board_size-1)
    return start_coord,end_coord

# Playing Board Generation
def generate_board(board_size,start_coord,end_coord):
    contents = ["T","F","F"]
    board = []
    # Generate rows
    for row in range(board_size):
        # Generate columns
        col_list = []
        for column in range(board_size+2):
            col_list.append(random.choice(contents))
        board.append(col_list)
    # Specifying start and end points
    board[start_coord][0] = "S"
    board[end_coord][board_size+1] = "E"
    return board

# Pathfinding function - Courtesy of Prof Matthiew
def is_there_path(board,board_size,start_coord,end_coord):
    start = [start_coord,0]
    end = [end_coord,board_size+1]
    boolean = False
    n = [start]
    s = []
    c = start
    
    while(len(n) > 0):
        coord = n.pop(0)
        s.append(coord)
        coord_next = coord[0] - 1, coord[1]
        if(coord == tuple(end)):
            boolean = True
            break
        if(not (coord_next[0] < 0 or coord_next[0] >= board_size \
           or coord_next[1] < 0 or coord_next[1] >= (board_size+2) \
           or coord_next in s)):
            if(not board[coord_next[0]][coord_next[1]] == "F"):
                n.append(coord_next)
        coord_next = coord[0] + 1, coord[1]
        if(not (coord_next[0] < 0 or coord_next[0] >= board_size \
           or coord_next[1] < 0 or coord_next[1] >= (board_size+2) \
           or coord_next in s)):
            if(not board[coord_next[0]][coord_next[1]] == "F"):
                n.append(coord_next)
        coord_next = coord[0], coord[1] - 1
        if(not (coord_next[0] < 0 or coord_next[0] >= board_size \
           or coord_next[1] < 0 or coord_next[1] >= (board_size+2) \
           or coord_next in s)):
            if(not board[coord_next[0]][coord_next[1]] == "F"):
                n.append(coord_next)
        coord_next = coord[0], coord[1] + 1
        if(not (coord_next[0] < 0 or coord_next[0] >= board_size \
           or coord_next[1] < 0 or coord_next[1] >= (board_size+2) \
           or coord_next in s)):
            if(not board[coord_next[0]][coord_next[1]] == "F"):
                n.append(coord_next)
    return boolean

# Converting T/F Board into integers for plotting
def create_display_board(board_size,start_coord,end_coord):
    display_board = []
    # Generate rows
    for row in range(board_size):
        # Generate columns
        col_list = []
        for column in range(board_size+2):
            col_list.append(0)
        display_board.append(col_list)
    # Specifying start and end points
    display_board[start_coord][0] = 1
    display_board[end_coord][board_size+1] = 3
    return display_board

def display_board_progress(coord_next,display_board,board_size,start_coord):
    display_board[start_coord][0] = 2
    display_board[coord_next[0]][coord_next[1]] = 1
    fig, ax = plt.subplots()
    colormap = colors.ListedColormap(['white','brown','orange','green'])
    im = ax.imshow(display_board,cmap = colormap)
    x = []
    for x_0 in range(0,board_size+1,1):
        x.append(x_0+0.5)
    y = []
    for y_0 in range(0,board_size-1,1):
        y.append(y_0+0.5)
    ax.set_xticks(x)
    ax.set_yticks(y)
    plt.tick_params(
        axis='both',
        which='both',  
        bottom=False,
        top=False,
        labelbottom=False,
        labelleft=False)
    plt.rc('grid', linestyle="-", color='black')
    plt.grid()
    plt.title("Current path. Close to continue.\nYou are at the red tile. Orange tiles are where you've been. \nMove to the Green Tile.  ")
    plt.show()
    display_board[coord_next[0]][coord_next[1]] = 2
    return display_board

def gameplay(board,board_size,display_board,start_coord,end_coord):
    start = (start_coord,0)
    end = (end_coord,board_size+1)
    n = [start]
    s = []
    lives = board_size+3
    action_message = "Where would you like to go next? Up, Down, Left or Right? "
    action_errormessage = "Invalid action entered"
    win = False
    fig, ax = plt.subplots()
    colormap = colors.ListedColormap(['white','brown','orange','green'])
    im = ax.imshow(display_board,cmap = colormap)
    x = []
    for x_0 in range(0,board_size+1,1):
        x.append(x_0+0.5)
    y = []
    for y_0 in range(0,board_size-1,1):
        y.append(y_0+0.5)
    ax.set_xticks(x)
    ax.set_yticks(y)
    plt.tick_params(
        axis='both',
        which='both',  
        bottom=False,
        top=False,
        labelbottom=False,
        labelleft=False)
    plt.rc('grid', linestyle="-", color='black')
    plt.grid()
    plt.title("Current path. Close to continue.\nYou are at the red tile. Orange tiles are where you've been. \nMove to the Green Tile.  ")
    plt.show()
    while(len(n) > 0):
        # Set current coordinate
        coord = n.pop(0)
        s.append(coord)
        valid_nextmove = False
        while not valid_nextmove:
            # Player inputs next move
            coord_next_input = input(action_message)
            coord_next_input = coord_next_input.lower()
            if coord_next_input == "up":
                coord_next = coord[0]-1,coord[1]
                valid_nextmove = True
            elif coord_next_input == "down":
                coord_next = coord[0]+1,coord[1]
                valid_nextmove = True
            elif coord_next_input == "left":
                coord_next = coord[0],coord[1]-1
                valid_nextmove = True
            elif coord_next_input == "right":
                coord_next = coord[0],coord[1]+1
                valid_nextmove = True
            elif coord_next_input == "extralives":
                lives += 5
                print("sus, your number of lives magically increased to {}".format(lives))
                continue
            else:
                # Failure to input valid action restarts action loop
                print(action_errormessage)
                continue
            # Check if player is within the board
            if (coord_next[0] < 0 or coord_next[0] >= board_size \
            or coord_next[1] < 0 or coord_next[1] >= (board_size+2)):
                print("Stay within the board!")
                valid_nextmove = False
                continue
            # Check if player repeated path
            if coord_next in s:
                print("Hmm, you've been here before. Try a new path.")
                valid_nextmove = False
                continue
        #print(coord_next)
        # Check if player moved to end tile
        if(coord_next == tuple(end)):
            win = True
            break
        # Check if there are no valid moves left
        # Check if player selected a valid tile
        if(not board[coord_next[0]][coord_next[1]] == "F"):
                n.append(coord_next)
                display_board = display_board_progress(coord_next,display_board,board_size,start_coord)
        else:
            print("AHHHHH! You fell down.")
            n.clear()
            s.clear()
            n = [start]
            lives -= 1
            display_board = create_display_board(board_size,start_coord,end_coord)
            time.sleep(1)
            print("Back to the start!")
            time.sleep(1)
            print("Lives left = {}".format(lives))
            if lives == 0:
                print("Out of lives! You lose. The MOns-T.E.H caught you.")
                break
            time.sleep(1)
            input("Press Enter to respawn.")
            fig, ax = plt.subplots()
            colormap = colors.ListedColormap(['white','brown','orange','green'])
            display_board[start_coord][0] = 1
            im = ax.imshow(display_board,cmap = colormap)
            x = []
            for x_0 in range(0,board_size+1,1):
                x.append(x_0+0.5)
            y = []
            for y_0 in range(0,board_size-1,1):
                y.append(y_0+0.5)
            ax.set_xticks(x)
            ax.set_yticks(y)
            plt.tick_params(
                axis='both',
                which='both',  
                bottom=False,
                top=False,
                labelbottom=False,
                labelleft=False)
            plt.rc('grid', linestyle="-", color='black')
            plt.grid()
            plt.title("Current path. Close to continue.\nYou are at the red tile. Orange tiles are where you've been. \nMove to the Green Tile.  ")
            plt.show()
    return win

def main():
    # Game introduction
    arcade = introduction()
    if arcade:
        # Choose difficulty level for arcade mode
        board_size = difficulty_level_selector()
        start_coord,end_coord = generate_start_end_coord(board_size)
        is_board_ok = False
        while not is_board_ok:
            board = generate_board(board_size,start_coord,end_coord)
            is_board_ok = is_there_path(board,board_size,start_coord,end_coord)
        print("Game Start!")
        display_board = create_display_board(board_size,start_coord,end_coord)
        win = gameplay(board,board_size,display_board,start_coord,end_coord)
        if win:
            print("Congratulations, you've won")
    else:
        # LEVEL 1 
        board_size = 3
        # Generate Easy Board
        start_coord,end_coord = generate_start_end_coord(board_size)
        is_board_ok = False
        while not is_board_ok:
            board = generate_board(board_size,start_coord,end_coord)
            is_board_ok = is_there_path(board,board_size,start_coord,end_coord)
        print("Game Start!")
        display_board = create_display_board(board_size,start_coord,end_coord)
        # Board display - for debugging purposes only
        # for i in board:
        #     print(i)
        win = gameplay(board,board_size,display_board,start_coord,end_coord)
        if win:
            print("PW : Nice job! But its not over yet. Theres another bridge ahead!")
            time.sleep(3)
            print("PW : And it looks like its getting more difficult!")
            time.sleep(3)
            print("PW : Here we gooooo...")
            time.sleep(3)
            input("Press Enter to continue")
        else:
            return
        # LEVEL 2
        board_size = 4
        # Generate Normal Board
        start_coord,end_coord = generate_start_end_coord(board_size)
        is_board_ok = False
        while not is_board_ok:
            board = generate_board(board_size,start_coord,end_coord)
            is_board_ok = is_there_path(board,board_size,start_coord,end_coord)
        print("Game Start!")
        display_board = create_display_board(board_size,start_coord,end_coord)
        # Board display - for debugging purposes only
        # for i in board:
        #     print(i)
        win = gameplay(board,board_size,display_board,start_coord,end_coord)
        if win:
            print("PW : Amazing! Don't celebrate too soon, though. There's one more bridge left!")
            time.sleep(3)
            print("PW : Oh no.. Its the hardest one yet..")
            time.sleep(3)
            input("Press Enter to continue")
        else:
            return
        # LEVEL 3
        board_size = 5
        # Generate Hard Board
        start_coord,end_coord = generate_start_end_coord(board_size)
        is_board_ok = False
        while not is_board_ok:
            board = generate_board(board_size,start_coord,end_coord)
            is_board_ok = is_there_path(board,board_size,start_coord,end_coord)
        print("Game Start!")
        display_board = create_display_board(board_size,start_coord,end_coord)
        # Board display - for debugging purposes only
        # for i in board:
        #     print(i)
        win = gameplay(board,board_size,display_board,start_coord,end_coord)
        if win:
            print("PW : Congratulations! You've escape the evil, horrible MOns-T.E.H.")
            time.sleep(3)
            print("PW : Good job kid. Lets hope you won't have to deal with him again.")
            time.sleep(3)
            print("SYSTEM : RUN 'MOnsTEH_Run.py' again to play Story mode again or try Arcarde mode.\nThanks for playing!")
        else:
            return

# Runs the game
if __name__ == "__main__":
    main()


