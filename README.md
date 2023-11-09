# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## 1. Setting up the Hangman class  
Arguments: 
- `word_list`: takes in a series of words in list format
- `num_lives`: (defaulted to 5) sets the maximum number of unique letters the user is allowed to guess, before a player loses the game  

Other Variables that need to be initialised:
- `word`: this variable randomly selects a single member from  `word_list`. 
- `word_guessed`: A list that compiles the valid characters that the user has already attempted
- `num_letters`: Calculates number of letters that have not yet been guessed correctly from `word`

## check_guess() Function
The check_guess function is the brain of the code. This is where the user input is compared to the letters in the self.word variable. 


Firstly, the code checks if the guessed letter `guess` is a member of the list of characters in `word`. 
- If it is, it prints a "Good guess!..." message. 
- It then also places `guess` in every position of `guess_word` where the 'if' statement is True. 

```
if guess in self.word: 
    print(f'Good guess! {guess} is in the word.')
        
    for letter in range(len(self.word)):
        if self.word[letter] == guess:
            self.word_guessed[letter] = guess 
            self.num_letters -= 1
```

Otherwise in the case where the if statement is false: 
- The number of lives remaining decreases by 1

```
else:
    self.num_lives -=1 
    print(f'Sorry, {guess} is not in the word.')
    print(f'You have {self.num_lives} lives left.')
```

## ask_for_input() Function:

1. Firstly, `ask_for_input()` checks takes in a user input
2. It then checks if the user input is valid
    - The user input is valid if it is a single alphabetical character.


If the user input is valid, it then calls the `check_guess(guess)` function. This means that the `check_guess()` function is taking in the valid user input - assigned to the variable `guess` - as an argument. 

```
 def ask_for_input(self):

    guess = input('guess a single letter: ') 

    if len(guess) != 1 or guess.isalpha() == False: 
        print('Invalid Letter. Please enter a single alphabetical character.')

    elif guess in self.list_of_guesses: 
        print("You already tried that letter!")
    
    else:
        self.check_guess(guess) 
        self.list_of_guesses.append(guess) #keeps track of the letters that the user has already tried
```

After executing the `check_guess(guess)` function, it appends `list_of_guesses`with `guess`. 
- This allows the `ask_for_input()` to check for duplicate inputs. 


# play_game() Function
The `play_game()` function contains the logic of the game: 
- If the number of lives reduces to zero, `play_game()` prints a statement to inform you that you have lost
- If the number of remaining characters you have to guess is zero AND you have a non-zero value of lives left, the `play_game()` prints a statement to inform you that you have won
- If you have a non-zero number of lives and a non-zero number of characters left to guess in `word`, then the `play_game()` function executes the `ask_for_input()` function 

## To play the hangman game
To play the game: 
1. Execute the play_game() function, and enter a list of words as the argument
2. Follow the instructions given in the terminal!