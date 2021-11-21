import gspread
import random
from google.oauth2.service_account import Credentials
from random import randrange
from termcolor import colored
import os
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('CREDS.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('word_meaning_examples')

word_meaning_examples = SHEET.worksheet('word_meaning_examples')

row_count = len(word_meaning_examples.col_values(1))  # counts all rows with data entries in col1
row_ref_start = row_count + 1  # accounts for Sheets rows starting at 1
    # start the randrange at 1 if including heading row, 2 if not.
# random_row = word_meaning_examples.row_values(randrange(2, row_ref_start))
# random row is the word and meaning from the dictionary(word_meaning_examples) sheet
# word = random_row[0]
# meaning = random_row[1]
# word_as_list = list(word)  # Converts our word into a list so it can be shuffled.
# random.shuffle(word_as_list)  # Shuffles our word so the user has a clue of what word they are searching for.
# shuffled_word = random.shuffle(word_as_list)
word = "word"
meaning = "meaning"
word_as_list = "clue"
# print(word)

def new_word(row_ref_start):
    random_row = word_meaning_examples.row_values(randrange(2, row_ref_start))
    global word
    word = random_row[0]
    global meaning
    meaning = random_row[1]
    global word_as_list
    word_as_list = list(word)
    random.shuffle(word_as_list)

    word_as_list = list(word)  # Converts our word into a list so it can be shuffled.
    random.shuffle(word_as_list)  # Shuffles our word so the user has a clue of what word they are searching for.
    
    print(f"Welcome, here is your word and definition:")
    print(f"word: {word}")
    print(f"def: {meaning}")
    print(f"{word_as_list}")
    
    


# print(word)
# print(meaning)
    




def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def main_menu():
    while True:
        print(colored("Welcome to Daily Dictionary \n", 'red'))
        print("Please select an item from the menu using a number \n")
        print("1. Begin Game")
        print("2. 12 letter games (Hard)")
        print("3. Word of the Day")
        print("4. How to Play")
        print("5. Dictionary Search")

        menu_choice = int(input("Please choose a menu item using the numbers 1-5:"))

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
        print(f"You have selected menu item {number}")
        #This function will launch the word game if the user selects play game from the menu.
        word_game(row_ref_start)

    elif number == 2:
        # 12 letter games
        print(f"You have selected menu item {number}")

    elif number == 3:
        # word of the day
        print(f"You have selected menu item {number}")

    elif number == 4:
        # how to play
        print(f"You have selected menu item {number}")
        cls()
        print("How to play the Daily Dictionary word games.")
        print("The game selects Word at random from the Daily Dictionary Dataset")
        print("and displays the definition of that word.\n")
        print("You will then have to Guess what the selected word from its definition description.\n")
        print("That sounds pretty tough, right?")
        print("Don't worry, to make the task easier we will display the mixed up letters of the word as a clue.\n")
        a = input("To return to the main menu, please type type any letter and then press enter:")
        if a:
            cls()
            main_menu()
        
        if return_to_menu == "y":
            cls()
            main_menu()
        
        else: print("Please enter 'y' to return to the main menu.")


    elif number == 5:
        # dictionary search
        print(f"You have selected menu item {number}")

    else: print(f"{number} is not valid")


def word_game(row_ref_start):
    cls()
    """
    The Word game function displays the Game text, shuffled word, meaning and the user input.
    The user input will = user answer. This user answer will then be passed to the validate user answer function.
    
    """
    
    while True:
        random_row = word_meaning_examples.row_values(randrange(2, row_ref_start))

        global word
        word = random_row[0]
        global meaning
        meaning = random_row[1]
        global word_as_list
        word_as_list = list(word)
        random.shuffle(word_as_list)

        word_as_list = list(word)  # Converts our word into a list so it can be shuffled.
        random.shuffle(word_as_list)  # Shuffles our word so the user has a clue of what word they are searching for.
        print(f"We have selected a word or phrase from our Dictionary containing {row_count} entries")
        print("Can you guess the word from its Dictionary Definition below? The letters of the word have been jumbled up but we capitalised the first letter of the word to help you.\n")
        # print(f"Letters: {word_as_list}")
        print(f"Definition: {meaning}.")
        print(f"Answer: {word}")
        print(f"Clue: {word_as_list}")
        user_answer = input("Enter your answer here:\n")
        validate_user_answer(user_answer)

        if validate_user_answer(user_answer):
            print(f"Correct! {word}: {meaning}")
            break
        return main_menu()



def validate_user_answer(user_answer):
    """

    This function will check if the user answer matches the word.
    If the answer does not match the word, an error will be shown
    """

    lowercase_answer = word.lower()
    validate_answer = user_answer
    if validate_answer == word:
        print(f"Correct! {word}: {meaning}")
        play_again = input("Would you like to play again? y/n:")
        
        
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
        play_again = input("Would you like to play again? y/n:")
        
        if play_again == "y":
            cls()
            word_game(row_ref_start)
        elif play_again == "n":
            cls()
            main_menu()
        else: print(f"{play_again} is not a valid input. Please enter y/n.")

    elif validate_answer != word:
        print(f"{user_answer} is incorrect. The word we are looking for is {word}")
        play_again = input("Would you like to play again? y/n:")
        if play_again == "y":
            cls()
            word_game(row_ref_start)
        elif play_again == "n":
            cls()
            main_menu()
        else: print(f"{play_again} is not a valid input. Please enter y/n.")
        
        
        
    else: user_answer = input("That isn't the corrent word. Please try again.\n Enter your answer here:\n")

def main():
    main_menu()

main()