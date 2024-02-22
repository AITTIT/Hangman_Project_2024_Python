import random

random.seed()

#A function that takes in a string, the index of the letter that is replaced, and the character that it is replaced with.
def replace_letter(string, index, new_letter):
    #A condition that returns the original string if index is out of range
    if index < 0 or index >= len(string):
        return string 
    return string[:index] + new_letter + string[index + 1:]

#A function that takes user input and checks whether it is just one character, written in lower case,
#and is not a digit but a letter. If these conditions are not met, returns itself and takes new input until
#the user gives acceptable input.
#If the user input matches a word that has already been guessed and is in the playerWord variable,
#informs the user and returns itself to take correct input.
def get_user_input():
    user_input = input("Please enter a character: ")
    if len(user_input) == 1 and not user_input.isdigit() and user_input.islower():
        if user_input in playerWord:
            print("You have guessed that already.")
            return get_user_input()
        else:
            return user_input
    else:
        print("Invalid input. Please enter one lowercase letter.")
        return get_user_input()
    

#Another function that takes user input. The function only accepts 'y' or 'n' as input.
#If the input is something else, instructs the user to give 'y' or 'n', and returns itself.
def get_user_input_quit():
    user_input = input("Do you want to play again? (y/n) ")
    if user_input == "y" or user_input == "n":
        return user_input
    else:
        print("Invalid input. Please enter 'y' for yes and 'n' or no.")
        return get_user_input_quit()

#Function draws the correct iteration of the gallows depending on
#the amount of wrong guesses made by the player.
def drawHangman(wrongGuess):
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
            print("\nSomething went wrong.")





#This is the main loop that controls whether the player wants to play again after one game.
while (True):
    #Every time a new game is started, a random word is chosen from the list.
    wordList = ["submarine", "marine", "biologist", "fire", "car", "university", "measure", "hygiene", "shop"]
    chosenWord = random.choice(wordList)
    

    #A variable that stores the amount of right letters the player has guessed of the chosenWord.
    rightLetters = 0
    #A variable that store the amount of wrong letters the player has guessed.
    wrongGuess = 0
    #The wrong guesses are stored in this list and printed for the player to see later.
    wrongGuessedLetters = []

    #print(chosenWord)
    #A variable for the word that the player starts guessing.
    playerWord=""
    #This loop stores underscores into the playerWord variable.
    for letter in chosenWord:
        playerWord += "_"
    #This loop displays the length of the word to the player by printing the underscores.
    for letter in playerWord:
        print(letter, end= " ")

    print("\n")
    #The drawHangman function is called once to draw the gallows.
    drawHangman(wrongGuess)

    #The main gameplay loop which is exited when the user guesses the word, or has guessed six wrong letters.
    while (True):
        
        #Here the player input is received.
        guessedLetter = get_user_input()     
        
        if guessedLetter in chosenWord:
            counter = 0
            while counter < len(chosenWord):
                if guessedLetter in chosenWord[counter]:
                    playerWord = replace_letter(playerWord, counter, guessedLetter)
                    rightLetters += 1
                counter += 1
        else:
            print("That letter is not in the word.")
            if guessedLetter not in wrongGuessedLetters:
                wrongGuessedLetters.append(guessedLetter)
                wrongGuess += 1
        
        drawHangman(wrongGuess)

        for letter in playerWord:
            print(letter, end= " ")
        print(" ")
        print(f"Guessed letters: {wrongGuessedLetters}")

        if wrongGuess >= 6:
            print("Too many wrong guesses. You lost.")
            break
        if rightLetters == len(chosenWord):
            print("Good job, you guessed the word!")
            break  

    choice = get_user_input_quit()
    if choice == "n":
        break

print("Exiting.")



#KEHITYS:
#Pitäisikö lisätä valmiin sanan arvaus mukaan tähän versioon?
#SQlite tietokanta jossa yksi taulu jossa vaikka sata sanaa?


#Teen tämän perusversion nyt kuntoon, kommentoin sen ja siirrän githubiin.
#Kun olen saanut sen tehtyä, teen uuden branchin ja rupean katsomaan ensin sqlite kantaa
#Sitten graafista käyttöliittymää?