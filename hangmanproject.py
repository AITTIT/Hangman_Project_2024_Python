import random
import sqlite3

random.seed()

#Siirrä hangman eri moduuliin. Voisiko getWordFromDatabase myös olla databasecreate moduulissa?

def getWordFromDatabase():
    """" Connects to the word database, picks a word at random, and returns it. """
    connection = sqlite3.connect("worddatabase.db")
    randomID = random.randrange(2, 55)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Words WHERE ID = {randomID}")
    data = cursor.fetchall()

    for record in data:
        tempWord = record[1]
    
    return tempWord

def replace_letter(string, index, new_letter):
    """ A function that takes in a string, the index of the letter that is replaced, and the character that it is replaced with."""
    # A condition that returns the original string if index is out of range
    if index < 0 or index >= len(string):
        return string 
    return string[:index] + new_letter + string[index + 1:]


def get_user_input():
    """ A function that takes user input and checks whether it has the length of one character, it is written in lower case,
    and is a letter. If these conditions are not met, returns itself and takes new input until
    the user gives acceptable input. 
    If the user input matches a letter that has already been guessed and is in the userWord variable,
    informs the user and returns itself to take correct input. """
    user_input = input("Please enter a character: ")
    if len(user_input) == 1 and not user_input.isdigit() and user_input.islower():
        if user_input in userWord:
            print("You have guessed that already.")
            return get_user_input()
        else:
            return user_input
    else:
        print("Invalid input. Please enter one lowercase letter.")
        return get_user_input()
    

def get_user_input_quit():
    """ Another function that takes user input. The function only accepts 'y' or 'n' as input.
    If the input is something else, instructs the user to give 'y' or 'n', and returns itself. """
    user_input = input("Do you want to play again? (y/n) ")
    if user_input == "y" or user_input == "n":
        return user_input
    else:
        print("Invalid input. Please enter 'y' for yes and 'n' or no.")
        return get_user_input_quit()


def drawHangman(wrongGuess):
    """ Function draws the correct iteration of the gallows depending on
    the amount of wrong guesses made by the user. """
    match wrongGuess:
        case 0:
            print("   _____")
            print("  |     |")
            print("  |      ")
            print("  |      ")
            print("  |      ")
            print("__|___________")
        case 1:
            print("   _____")
            print("  |     |")
            print("  |     O")
            print("  |      ")
            print("  |      ")
            print("__|___________")
        case 2:
            print("   _____")
            print("  |     |")
            print("  |     O")
            print("  |     |")
            print("  |      ")
            print("__|___________")
        case 3:
            print("   _____")
            print("  |     |")
            print("  |    \\O")
            print("  |     |")
            print("  |      ")
            print("__|___________")
        case 4:
            print("   _____")
            print("  |     |")
            print("  |    \\O/")
            print("  |     |")
            print("  |      ")
            print("__|___________")
        case 5:
            print("   _____")
            print("  |     |")
            print("  |    \\O/")
            print("  |     |")
            print("  |    / ")
            print("__|___________")
        case 6:
            print("   _____")
            print("  |     |")
            print("  |    \\O/")
            print("  |     |")
            print("  |    / \\")
            print("__|___________")
        case _:
            print("Something went wrong.")




#This is the main loop that controls whether the user wants to play again.
while (True):
    #Every time a new game is started, getWordFromDatabase is called and a new random word is fetched.
    chosenWord = getWordFromDatabase()
    print(chosenWord)

    #A variable that stores the amount of right letters the user has guessed of the chosenWord.
    rightLetters = 0
    #A variable that stores the amount of wrong letters the user has guessed.
    wrongGuess = 0
    #The wrong guesses are stored in this list and printed for the user to see.
    wrongGuessedLetters = []

    #A variable that stores the users guessed word.
    userWord=""
    #This loop stores underscores into the userWord variable.
    for letter in chosenWord:
        userWord += "_"
    #This loop displays the length of the word to the user by printing the underscores.
    for letter in userWord:
        print(letter, end= " ")

    print("\n")
    #The drawHangman function is called once to draw the gallows.
    drawHangman(wrongGuess)

    #The main gameplay loop which is exited when the user guesses the word, or has guessed six wrong letters.
    while (True):
        
        #Here the function get_user_input() is called to receive correct input from the user,
        #which is then stored in the variable guessedLetter.
        guessedLetter = get_user_input()     
        
        #If-statement that checks whether the letter the user has given is in the chosenWord.
        #If not, the guessed letter is checked against letters that have been guessed prior,
        #and if there is no match, the letter is added to the wrongGuessedLetters list and 
        #the counter for wrong guesses is incremented once.
        if guessedLetter in chosenWord:
            counter = 0
            #This loop goes through checks the guessedLetter against the ChosenWord.
            #When it finds a match, the replace_letter function is called and a new string
            #with the new letter is created and stored in userWord. the rightLetters 
            #counter is also incremented by one every time a new letter is added to the
            #userWord.
            while counter < len(chosenWord):
                if guessedLetter in chosenWord[counter]:
                    userWord = replace_letter(userWord, counter, guessedLetter)
                    rightLetters += 1
                counter += 1
        else:
            print("That letter is not in the word.")
            if guessedLetter not in wrongGuessedLetters:
                wrongGuessedLetters.append(guessedLetter)
                wrongGuess += 1
        
        #drawHangman function is called and a new gallows is drawn according to the amount of wrong guesses.
        drawHangman(wrongGuess)

        #The userWord is now printed with possible new letters.
        for letter in userWord:
            print(letter, end= " ")
        print(" ")
        #Here the already guessed letters that are not in the word are displayed.
        print(f"Guessed letters: {wrongGuessedLetters}")

        #These if statements are entered if the end of the game is reached, whether
        #it is too many wrong guesses or the user having guessed the word, and then
        #the main gameplay loop is broken out of.
        if wrongGuess >= 6:
            print("Too many wrong guesses. You lost.")
            break
        #The while loop is broken out of if the amount of right letters guessed matches
        #the length of the right word.
        if rightLetters == len(chosenWord):
            print("Good job, you guessed the word!")
            break  
    #Here the user get_user_input_quit() function is called to receive either 'y'
    # or 'n' from the user. If the user inputs 'n', the while-loop is exited and
    # the game ends.
    choice = get_user_input_quit()
    if choice == "n":
        break

print("Exiting.")