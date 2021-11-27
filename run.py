import gspread
import random
from google.oauth2.service_account import Credentials
from random import randrange  # this import will be used when getting a random row from the Google sheet
from termcolor import colored  # this import will be used to colourize the terminal
from datetime import datetime  # this import will be used to display the date for the word of the day mode
from pyfiglet import Figlet
import os

f = Figlet(font='standard')  # Figlet font variable
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('word_meaning_examples')

word_meaning_examples = SHEET.worksheet('word_meaning_examples')
# The name of the collective dictionary dataset
word_column = word_meaning_examples.col_values(1)
# The word column variable is a list of all the words in our dicitonary

row_count = len(word_meaning_examples.col_values(1))    # counts all rows with data entries in col1
row_ref_start = row_count + 1  # accounts for Sheets rows starting at 1
word = "word"
meaning = "meaning"
word_as_list = "clue"


def cls():
    """
    This function clears the terminal.  Taken from stack overflow.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    """
    This displays the main menu / opening terminal.
    The user must choose a menu item by typing the
    corresponding number from the menu list.;
    The users choice will then be passed to the validate usser choice function

    """
    while True:
        print(colored(f.renderText("Welcome to Daily Dictionary \n"), 'red'))
        print("Please select an item from the menu using a number \n")
        print(colored("1. Word Game", 'blue'))
        print(colored("2. Definition Game", 'green'))
        print(colored("3. Word of the Day", 'blue'))
        print(colored("4. Dictionary Search", 'green'))
        print(colored("5. How to play\n", 'blue'))

        menu_choice = int(input("Please choose a menu item using the numbers 1-5:\n"))

        if validate_menu_choice(menu_choice):
            print(f"You have selected menu item number:{menu_choice}")
            break
        return menu_choice


def validate_menu_choice(menu_choice):
    """

    This function will check if the user has inputted a number
    between 1 -5.
    The function will return an error if the input is invalid.
    """

    number = menu_choice
    if number == 1:
        print(f"You have selected menu item {number}")  # This function will launch the word game from menu
        word_game(row_ref_start)

    elif number == 2:  # Definition game
        print(f"You have selected menu item {number}")
        cls()
        definition_game(row_ref_start)

    elif number == 3:  # word of the day
        print(f"You have selected menu item {number}")
        cls()
        word_of_the_day()

    elif number == 4:  # dictionary search
        cls()
        print(f"You have selected menu item {number}")
        dictionary_search_loop()
        
    elif number == 5:  # how to play
        print(f"You have selected menu item {number}")
        cls()
        print("How to play the Daily Dictionary word games.\n")
        print("WORD GAME - The game selects Word at random from the Daily Dictionary Dataset")
        print("and displays the definition of that word.\n")
        print("You'll then have to determine the word from its definition description.\n")
        print("That sounds pretty tough, right?")
        print("Don't worry, to make the task easier we will display the mixed up letters of the word as a clue.\n")

        print("DEFINITION'S GAME - The game will display a definition and three words.\n")
        print("One of the words will match the Definition. The other two will be random words from our Dictionary.\n")
        print("Can you match the Definiton to the correct word?\n")

        print("DICTIONARY SEARCH - The search function allows you to look up a word in our dictionary.")
        print(f"There are {row_count} words in our Dataset. If your word is included then the search function will return the Definition.\n\n")
        a = input("To return to the main menu, please type type any letter and then press enter:\n")
        if a:
            cls()
            main_menu()
        elif a == "y":
            cls()
            main_menu()
        else: print("Please enter 'y' to return to the main menu.")

    else: print(f"{number} is not valid"), main_menu()


def word_game(row_ref_start):
    cls()
    """
    The Word game function displays the Game text, shuffled word, meaning and the user input.
    The user input will = user answer. This user answer will then be passed to the validate user answer function.
    """
    while True:
        random_row = word_meaning_examples.row_values(randrange(2, row_ref_start))  # selects a row form the sheet at random

        global word
        word = random_row[0]  # assigns the value of column 0 (words column) in the sheet to the word variable
        global meaning
        meaning = random_row[1]  # assigns the value of column 1 (meanings column) in the sheet to the meaning variable
        global word_as_list
        word_as_list = list(word)  # converts out word to a list so it can be shiffled and displayed as a clue
        random.shuffle(word_as_list)  # shuffles the word/clue

        out_str = " "
        clue = out_str.join(word_as_list)  # puts the shuffled word back together again as a clue for the user.

        word_as_list = list(word)  # Converts our word into a list so it can be shuffled.
        random.shuffle(word_as_list)  # Shuffles our word so the user has a clue of what word they are searching for.
        print(colored(f.renderText("Word Game \n"), 'green'))
        print(f"We have selected a word or phrase from our Dictionary containing {row_count} entries")
        print("Can you guess the word from its Dictionary Definition below?\n")
        print("The letters of the word have been jumbled up but we capitalised the first letter of the word to help you.\n")
        print(f"Definition: {meaning}.\n")
        print(f"Clue: {clue}\n")
        user_answer = input("Enter your answer here:\n")
        validate_user_answer(user_answer)

        if validate_user_answer(user_answer):
            print(f"Correct! {word}: {meaning}")
            break
        return main_menu()


def definition_game(row_ref_start):
    cls()
    """
    The Definition game function will create a word/definition combo as well as an additonal 2 words.
    The game will display the defintion and 3 words and the user will have to choose which word
    matches the definiton.
    """
    # the random_row x3 variables are the 3 random words
    random_row = word_meaning_examples.row_values(randrange(2, row_ref_start)) 
    random_row2 = word_meaning_examples.row_values(randrange(2, row_ref_start))
    random_row3 = word_meaning_examples.row_values(randrange(2, row_ref_start))    
    global word
    word = random_row[0]
    global meaning
    meaning = random_row[1]
    word2 = random_row2[0]
    word3 = random_row3[0]    
    definition_game_words = [word, word2, word3]  # combines the thre definitons
    random.shuffle(definition_game_words)  # this shuffles the correct answer clue
    print(colored(f.renderText("Definition's Game"), 'blue'))
    print(f"Definition: {meaning}.\n")
    print(f"Please choose the correct word to match the Definition:\n")
    print(f"{definition_game_words}\n")
    user_def_answer = input("Enter your answer here:\n")
    validate_user__definition_answer(user_def_answer)

def validate_user_answer(user_answer):
    """

    This function will check if the user answer matches the word.
    If the answer does not match the word, an error will be shown
    """

    lowercase_answer = word.lower()  # this will account for the users answer being all lowercase
    validate_answer = user_answer
    if validate_answer == word:
        print(f"Correct! {word}: {meaning}")
        play_again = input("Would you like to play again? y/n:\n")      
        if play_again == "y":
            cls()
            word_game(row_ref_start)
        elif play_again == "n":
            cls()
            main_menu()
        else: print("Please enter y/n.") 
        #this will reset the game

    elif validate_answer == lowercase_answer:
        #this will return a correct answer if the user doesn't returns a lowercase correct answer
        print(f"Correct! {word}: {meaning}")
        play_again = input("Would you like to play again? y/n:\n")
        if play_again == "y":
            cls()
            word_game(row_ref_start)
        elif play_again == "n":
            cls()
            main_menu()
        else: print(f"{play_again} is not a valid input. Please enter y/n.")

    elif validate_answer != word:
        print(f"{user_answer} is incorrect. The word we are looking for is {word}")
        play_again = input("Would you like to play again? y/n:\n")
        if play_again == "y":
            cls()
            word_game(row_ref_start)
        elif play_again == "n":
            cls()
            main_menu()
        else: print(f"{play_again} is not a valid input. Please enter y/n.")       
    else: user_answer = input("That isn't the corrent word. Please try again.\n Enter your answer here:\n")


def validate_user__definition_answer(user_def_answer):
    """

    This function will check if the user answer matches the word.
    If the answer does not match the word, an error will be shown
    """
    lowercase_def_answer = word.lower()
    validate_def_answer = user_def_answer
    if validate_def_answer == word:
        print(f"Correct! {word}: {meaning}")
        play_again = input("Would you like to play again? y/n:\n")
        if play_again == "y":
            cls()
            definition_game(row_ref_start)
        elif play_again == "n":
            cls()
            main_menu()
        else: print("Please enter y/n.")

    elif validate_def_answer == lowercase_def_answer:
        #this will return a correct answer if the user doesn't returns a lowercase correct answer
        print(f"Correct! {word}: {meaning}")
        play_again = input("Would you like to play again? y/n:\n")
        if play_again == "y":
            cls()
            definition_game(row_ref_start)
        elif play_again == "n":
            cls()
            main_menu()
        else: print(f"{play_again} is not a valid input. Please enter y/n.")

    elif validate_def_answer != word:
        print(f"{user_def_answer} is incorrect. The word we are looking for is {word}")
        play_again = input("Would you like to play again? y/n:\n")
        if play_again == "y":
            cls()
            definition_game(row_ref_start)
        elif play_again == "n":
            cls()
            main_menu()
        else: print(f"{play_again} is not a valid input. Please enter y/n."), definition_game(row_ref_start)
    else: user_def_answer = input("That isn't the corrent word. Please try again.\n Enter your answer here:\n")



def dictionary_search_loop():

    """
    The dictionary search loop function allows the user to search for a word from the dictionary.
    The function will cycle through the words in or word column and if the word matches the user search input then
    the function will return the row value - this will be the word/definition list.
    """

    word_meaning_examples = SHEET.worksheet('word_meaning_examples')
    word_column = word_meaning_examples.col_values(1) # The is the list of words from the word column in our sheet

    print(colored(f.renderText("Dictionary Search"), 'red'))
    print(f"Feel free to search for a word from our Dictionary.")
    print(f"We have {row_count} words in our collection.\n")
    print("Here are some examples you could try:\n")

    print("Pollyannaish, Septuagenarian, or Chiaroscuro \n")

    user_search = input("Please search for a word or type ""menu"" to return to the main menu:\n")
    user_search_capitalize = user_search.title() # This is needed to capitalize the first letter of the user search input
    try:
        if user_search == "menu":
            cls()
            main_menu()

        elif user_search_capitalize != "menu":
            if user_search_capitalize in word_column:
                print(SHEET.worksheet('word_meaning_examples').row_values(SHEET.worksheet('word_meaning_examples').find(f"{user_search_capitalize}").row))
                search_again = input("Would you like to search again? y/n:\n")
                if search_again == "y":
                    cls()
                    dictionary_search_again()
                elif search_again == "n":
                    cls()
                    main_menu()
                else: print("invalid input"), dictionary_search_loop()
            else: print("Sorry, we unfortunately we don't have that word in our Dictionary, please search for another word. \n"), dictionary_search_again()
        else: print("Sorry, unfortunately we don't have that word in our Dictionary, please search for another word.\n"), dictionary_search_again()

    except ValueError: print("Apologies! That word isn't in our Dictionary collection, please try again.\n"), dictionary_search_again()

def dictionary_search_again():

    """
    This function is a duplicate of the the dictionary_search_again() function
    The title and intro to the section has been removed for better user experience.
    """
    user_search = input("Please search for a word or type ""menu"" to return to the main menu:\n")
    user_search_capitalize = user_search.title() # This is needed to capitalize the first letter of the user search input
    try:
        if user_search == "menu":
            cls()
            main_menu()

        elif user_search_capitalize != "menu":
            if user_search_capitalize in word_column:
                print(SHEET.worksheet('word_meaning_examples').row_values(SHEET.worksheet('word_meaning_examples').find(f"{user_search_capitalize}").row))
                search_again = input("Would you like to search again? y/n:\n")
                if search_again == "y":
                    cls()
                    dictionary_search_again()
                elif search_again == "n":
                    cls()
                    main_menu()
                else: print("invalid input"), dictionary_search_loop()
            else: print("Sorry, unfortunately we don't have that word in our Dictionary, please search for another word\n"), dictionary_search_again()
        else: print("Sorry, we unfortunately we don't have that word in our Dictionary, please search for another word.\n"), dictionary_search_again()

    except ValueError: print("Apologies! That word isn't in our Dictionary collection, please try again."), dictionary_search_again()


def word_of_the_day():
    """
    This function displays the word of the day section.
    The current date is shown and a word/defintion from the dictionary.
    This can be used to help the user expand their vocabulary.
    """

    random_row = word_meaning_examples.row_values(randrange(2, row_ref_start))
    global word
    word = random_row[0]
    global meaning
    meaning = random_row[1]
    today = datetime.now().date()
    print(colored(f.renderText("Word of the Day"), 'yellow'))
    print(f"You're daily word for {today} is {word}.\n")
    print(f"{word}: {meaning}.\n")
    a = input("To return to the main menu, please type any letter and then press enter:\n")
    if a:
        cls()
        main_menu()
    else: print("Please enter 'y' to return to the main menu.")


def main():
    main_menu()

main()
