import gspread
from google.oauth2.service_account import Credentials
from random import randrange
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
random_row = word_meaning_examples.row_values(randrange(1, row_ref_start)) #random row is the word and meaning from the dictionary(word_meaning_examples) sheet
word = random_row[0]
meaning = random_row[1]
print(random_row)
print(word)
print(meaning)

