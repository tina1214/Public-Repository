import cs50, random, time, os, datetime
# lists
date = datetime.datetime.now()
music = ["piano", "orchestra", "ensemble", "notes", "harmony","violin","scores","conductor","recital","flute","woodwind","precussion","strings"]
animals=["flamingo", "cat", "turtle", "frog", "monkey","sheep","llama","giraffe","snake","chicken","pig","duck","horse"]
fruits=["banana", "grape", "orange", "apple", "cherry", "papaya", "strawberry", "mango", "kiwi","watermelon","blueberry","coconut","pineapple"]

# getWord function to restrict user input to letter
def getWord():
    check = True
    global answer
    while check:
        try:
            answer = cs50.get_string("Enter a word that you found: ")
            if answer.isalpha():
                answer=answer.lower()
                check = False
            else:
                print("Enter one word please")
        except ValueError:
            print("Enter one word please")

# selectBank to choose 10 random words from the selected list into word bank
def selectBank():
    global wordBank
    wordBank = []
    global category
    # randomize word from the chosen list
    i = 0
    if '2' in choice:
        for i in range (10):
            word = random.choice(music)
            while word in wordBank:
                word = random.choice(music)
            wordBank.append(word)
            i = i+1
        category = 'music'
    elif '3' in choice:
        for i in range (10):
            word = random.choice(animals)
            while word in wordBank:
                word = random.choice(animals)
            wordBank.append(word)
            i = i+1
        category = 'animals'
    elif '4' in choice:
        for i in range (10):
            word = random.choice(fruits)
            while word in wordBank:
                word = random.choice(fruits)
            wordBank.append(word)
            i = i+1
        category = 'fruits'
    # sort the wordBank according to length of word from longest to shortest
    wordBank = sorted(wordBank, key=len, reverse = True)
    print(wordBank)

# showList function to reveal the correct words at the end of the game
def showBank():
    print("#####################")
    print("  Word Bank Reveal:  ")
    for word in len(wordBank):
        print("\t",word)
    print("#####################")

# scoreBoard function to print scoreboard in terminal
def scoreBoard():
    scores = []
    with open("scoreBoard.txt", 'r') as myFile:
        for line in myFile.readlines():
            scores.append(((int)(line.split("\t")[0]), line.split("\t")[1], line.split("\t")[2]))
            # add each user to the list with their score, name, and date split
        sorted_scores = sorted(scores, reverse = True)
        # sort the list based on their scores
        print("Score Board\n")
        for i in range(3):
        # print the top three players
            board_score, board_name, board_date = sorted_scores[i]
            print(f"{board_score}\t{board_name}\t{board_date}")
    input("Press enter to return to menu")

# wordSearch function places the words in wordBank into a word search
def wordSearch():
    grid = [[]]
    rows = 15
    grid = [[0 for j in range(rows)] for i in range(rows)]
    for word in wordBank:
        for letter in word:
            try:
                index = grid.index(letter)
                break
            except ValueError:
                index = 0
                continue
        if index == 0:
            i = random.randrange(0,14)
            j = random.randrange(0,14)
        if (grid[int(index[0])][int(index[2])-1]).isalpha or (grid[int(index[0])][int(index[2])+1]).isalpha:
        # no horizontal space
            if ([int(index[0])-1][int(index[2])]).isalpha or ([int(index[0])+1][int(index[2])]).isalpha:
            # no vertical space, generate random position
                i = random.randrange(0,14)
                j = random.randrange(0,14)
            else:
            # no horizontal space but there's vertical space
                element = word.index(letter)
                for i in range(len(word)):
                # store the word vertically
                    grid[int(index[0])][int(index[2])-element] = word[i]


# menu function for user to navigate game
def menu():
    global choice
    os.system('clear')
    # print menu
    print("###############################")
    print("#    Word Search Game Menu    #")
    print("#       1 Instructions        #")
    print("#       2 Music               #")
    print("#       3 Animals             #")
    print("#       4 Fruits              #")
    print("#       5 Scoreboard          #")
    print("#       6 Exit                #")
    print("###############################")
        # prompt user input to proceed
    choice = input("Enter your choice ")
    os.system('clear')
    if '1' in choice:
    # print menu
        print("################################################")
        print("#               Game Instructions              #")
        print("# How to Play:                                 #")
        print("#  Select a category (music, animals, fruits), #")
        print("#  and 10 random words from the category will  #")
        print("#  be selected and arbitrarily placed in a     #")
        print("#  word grid. The player is expected to find   #")
        print("#  all 10 words under 2 minutes. If the player #")
        print("#  successfully finds all the words within the #")
        print("#  time constraint, they will be scored based  #")
        print("#  on the amount of time they spent completing #")
        print("#  the search and the number of turns it took. #")
        print("#                                              #")
        print("# Checking the Scoreboard:                     #")
        print("#  Based on different players' scores, they    #")
        print("#  be ranked accordingly and the top three     #")
        print("#  will be displayed on the Scoreboard         #")
        print("#                                              #")
        print("#            Have fun word searching!          #")
        print("################################################\n")
        input("Press press enter to go return to main menu" )
        menu()
    elif '6' in choice:
    # exit game
        print ("Goodbye!")
        exit()
    elif '3' in choice or '2' in choice or '4' in choice:
        selectBank()
        # call select bank
        global name
        # ask for user name
        name = input ("Name of player: ")
        # wordSearch()
        # create grid
        playing()
        # play game
        menu()
         # return to menu
    elif '5' in choice:
        scoreBoard()
        # print scoreBoard
        menu()
        # return to menu
    else:
    # invalid user input
        print("Please enter a valid option")
        menu()

def playing():
    # get start of time
    start = time.time()
    turn =0
    score =0
    correct = 0
    global found
    found = []
    while len(found) != len(wordBank):
        getWord()
        if answer in wordBank:
            if  answer in found:
            # if the word has been guessed before
                print("You have found this word already")
            else:
                # add 10 points to correct everytime the user guesses correctly
                correct = correct + 10
                # add word found by the user to found
                found.append(answer)
                os.system('clear')
                print("Nice guess!\nGuessed words:")
                # print the words that they've found
                for i in range (len(found)):
                    print(found[i])
                # get end of time
                end = time.time()
                if end-start > 120:
                # if 2 minutes have elapsed user loses then exit game
                    print("Sorry, you ran out of time!")
                    break
                if len(found) == len(wordBank):
                # if user guessed all correct user wins then exit game
                    score = round(turn + correct - (int)(start-end)/10)
                    f2 = open('scoreBoard.txt', 'a')
                    f2.write(str(score)+"\t"+name+"\t"+date.strftime("%Y-%m-%d")+"\n")
                    print("Congratulations, you have completed the word search!")
                    print("Your final score is", score)
                    input("Press enter to return to menu")
        else:
            print("Sorry, try again...")

menu()
