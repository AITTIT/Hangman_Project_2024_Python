
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