import gspread
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

"""
word_meaning_examples = SHEET.worksheet('word_meaning_examples')
#this line includes the heading row and doesn't account for Sheets rows starting at 1
row_count = len(word_meaning_examples.col_values(1)) # counts all rows with data entries in col1
row_ref_start = row_count + 1 #accounts for Sheets rows starting at 1
#start the randrange at 1 if including heading row, 2 if not.
random_row = word_meaning_examples.row_values(randrange(2, row_ref_start)) #random row is the word and meaning from the dictionary(word_meaning_examples) sheet
word = random_row[0]
meaning = random_row[1]
print(random_row)
print(word)
print(meaning)
"""

print(colored("Welcome to Daily Dictionary \n", 'red'))
print("Please select an item from the menu using a number \n")
print("1. Begin Game \n")
print("2. 12 letter games (Hard)\n")
print("3. Word of the Day \n")
print("4. How to Play \n")
print("5. Dictionary Search")
