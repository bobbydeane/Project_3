import gspread
import random
from google.oauth2.service_account import Credentials
from random import randrange
from termcolor import colored
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('CREDS.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('word_meaning_examples')
"""
def word_meaning():
    word_meaning_examples = SHEET.worksheet('word_meaning_examples')
    num = 99
    data = word_meaning_examples.get_all_values()[]
    print(data)

word_meaning()

"""


word_meaning_examples = SHEET.worksheet('word_meaning_examples')
#this line includes the heading row and doesn't account for Sheets rows starting at 1
row_count = len(word_meaning_examples.col_values(1)) # counts all rows with data entries in col1
row_ref_start = row_count + 1 #accounts for Sheets rows starting at 1
#start the randrange at 1 if including heading row, 2 if not.
random_row = word_meaning_examples.row_values(randrange(2, row_ref_start)) #random row is the word and meaning from the dictionary(word_meaning_examples) sheet
word = random_row[0]
meaning = random_row[1]
word_as_list = list(word) # Converts our word into a list so it can be shuffled.
random.shuffle(word_as_list) # Shuffles our word so the user has a clue of what word they are searching for.
print(word_as_list) 
shuffled_word = random.shuffle(word_as_list)
# print(meaning)
# print(word)
"""
print(random_row)
print(word)
print(meaning)
"""


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
        word_game()

    elif number == 2:
        print(f"You have selected menu item {number}")

    else: print(f"{number} is not valid")

def word_game():
    """
    The Word game function displays the Game text, shuffled word, meaning and the user input.
    The user input will = user answer. This user answer will then be passed to the validate user answer function.
    """
    while True:
        print(f"We have selected a word or phrase from our Dictionary containing {row_count} entries")
        print("Can you guess the word from its Dictionary Definition below? The letters of the word have been jumbled up but we capitalised the first letter of the word to help you.\n")
        print(f"Letters: {word_as_list}")
        print(f"Definition: {meaning}.")
        print(f"Answer: {word}")
        user_answer = input("Enter your answer here:\n")
        validate_user_answer(user_answer)

        if validate_user_answer(user_answer):
            print(f"Correct! {word}: {meaning}")


def validate_user_answer(user_answer):
    """
    This function will check if the user answer matches the word.
    If the answer does not match the word, an error will be shown
    """
    try:
        
        if user_answer != word:
            raise ValueError(
                f"The answer {user_answer} is incorrect. Please try again."
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

def main():
    main_menu()
    

main()