# Daily Dictionary

![Main_menu](https://github.com/bobbydeane/Project_3/blob/main/images/Daily-Dictionary.png?raw=true)

## live site

[Daily Dictionary](http://daily-dictionary-project3.herokuapp.com/)

## Repository

https://github.com/bobbydeane/Project_3

## Objective

Create a word game that helps that can be informative tool for the user. The project will use an API for the Dictionary, and will be created with Python.

*The project was created to be a part of my Code Institute portfolio*

## Brief

### Daily Dictionary

The goal of this site is to provide word games to provide a fun way to bolster the user's vocabulary.

-   the project will be written in Python
-   the project should be free from errors
-   have a varied word pool to allow the user to have a unique experience with each visit
-   handle user inputs and provide feedback for incorrect inputs
-   the project will have a large dictionary to ensure the has a vast pool of words to search from

## UX Design

### User Requirements

**First time user**
"As a user, I would like to test my existing knowledge of Words and Defintions".

"As as game/quiz fan, I want to play something that tests me and gives me feedback when I give an incorrect input."

**Returning User**
"As a returning user, I want to benefit from the dictionary search function."

"I would like to use the Daily word mode to better my vocabulary."

### Initial  Project Concept

My original idea was to have an anagram solver tool that would show anagrams of user input text. The idea morphed when searching for Dictionary Datasets, but the current project does have an anagram aspect to the Word Game mode.

### Colour Scheme and Typography

The project will be a Python Project that will be display to a Python terminal, because of this, the output will be quite basic color-wise. I imported red, blue, yellow and green colors form the `termcolor` package, and used a block text style generator function imported from Figlet.

## Logic

I created a flowchart using LucidChart to map put the programme flow. The idea was that the 'Home' page would include the main menu. The user would then select the game mode from the menu. The user input would then call a function and that function would run the game mode.

![flow](https://github.com/bobbydeane/Project_3/blob/main/images/Flow.png?raw=true)

The Dictionary was a googlesheet that was found on [Google Datasets](https://datasetsearch.research.google.com/).



## Features

### Existing features

**UX**

***"As a user, I would like to test my existing knowledge of Words and Definitions".***

![wordgame](https://github.com/bobbydeane/Project_3/blob/main/images/Word%20Game.png?raw=true)

 - The Word game and Definition game both call on the Dictionary Dataset that has over 13,000 words. This library is used to display a random word for the word game and gives  word definition alongside the word as an anagram as a clue.
 - The Definition game shows multiple words and the user has to match one of the words to the given definition, this will test the users vocabulary.

 ![Def_Game](https://github.com/bobbydeane/Project_3/blob/main/images/Definition.png?raw=true)

***"As as game/quiz fan, I want to play something that tests me and gives me feedback when I give an incorrect input."***

 - Each game gives feedback that would be informative to the user.

***"As a returning user, I want to benefit from the dictionary search function.*"**
![Search](https://github.com/bobbydeane/Project_3/blob/main/images/Search.png?raw=true)
 - The user can call upon the dictionary search in their everyday life to look up a word.

***"I would like to use the Daily word mode to better my vocabulary."***


 - The Daily word mode give a new word and definition each day. The user can revisit each day to learn something new.

##



## Features left to Implement

 - Add more words to the library or connect a larger Dataset
 - A mode that allows the user to choose the length of the words in their word game eg 12 letter word games
 - An ability for the user to add their own words and definition to the to the Dictionary.

##

## Technologies used

 **Python:**
 gspread
Imported random to generated a random word from the dictionary
Credentials from google.oauth2.service_account
Colored text from colored
Current Date data from datetime
Block text for titles imported from Figlet

**Heroku**

## Validator Testing

The programme underwent PEP8 validation from - http://www.pep8online.com/

![PEP8](https://github.com/bobbydeane/Project_3/blob/main/images/PEP8_validator.png?raw=true)

### Manual Python Testing

The specification within the project requires manual testing. I have performed multiple tests on the deployed site and during the development stage to ensure data is handled correctly and all functions are carrying out their intended actions.

##

## Bugs

I had some issues with text being too long for the terminal, this was fixed but splitting sentences into separate lines.

There was initial issues with the dictionary search, when the user entered a word that wasn't in the dictionary the programme would crash. I relied on the community at stack for help and Dave Horrocks offered a solution to nest my if/else statement in the Dict search loop function.

I had to remove all functions from the main() function because this would cause the previous inputs to be passed to the main menu when the user returned to the menu.

I had to add code to accommodate for the user answers being in lowercase because all entries in the dictionary began with a capital.

#
## Deployment

The site was deployed to GitHub pages. The steps to deploy are as follows: In the GitHub repository, navigate to the Settings tab From the source section drop-down menu, select the Master Branch Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found here - http://daily-dictionary-project3.herokuapp.com/

## Credits

**Content**
I used Google Datasets to search to find my Dictionary.

W3schools for random functions

Stackoverflow to find a method to return a row value from my sheet.

GeeksforGeeks to find Figlet text.

Lucid.app for flow chart generation

Thanks to Codeinstitute for the opportunity.

Thanks to Dave 'Californication' Horrocks from the slack community for providing me with the code to generate a random word from my dataset, and also for the feedback and README inspo. Much appreciated.




