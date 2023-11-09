import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list #list of words 
        self.num_lives = num_lives #number of lives the player has at the start of the game

        self.word = random.choice(self.word_list) #selects a random word from the word_list
        
        self.word_guessed = [] #list of the letters of the word that have been guessed correctly, with '_' used in places of letters in the word that have not yet been guessed
        for letter in range(len(self.word)):
            self.word_guessed.append('_')
      
        self.list_of_guesses = [] #list of the letters that have been guessed so far
        self.num_letters = len(self.word) #number of UNIQUE letters that have not been guessed yet

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word: #random_word is the randomised word selected from the list 'word_list'
            print(f'Good guess! {guess} is in the word.')
        
            for letter in range(len(self.word)):
                if self.word[letter] == guess:
                    self.word_guessed[letter] = guess #updates the guessed word with all the correctly guessed letters     
                    self.num_letters -= 1
        else:
            self.num_lives -=1 #reduces the number of lives left by 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')
        
        
        print(self.word_guessed) #shows the user the parts of the word they have guessed correctly so far

    def ask_for_input(self):

        guess = input('guess a single letter: ') #the user's guessed letter

        if len(guess) != 1 or guess.isalpha() == False: #check if input character is valid
            print('Invalid Letter. Please enter a single alphabetical character.')

        elif guess in self.list_of_guesses: #check if the same input character has already been made before
            print("You already tried that letter!")
        
        else:
            self.check_guess(guess) #execute function to see the input character is in the mystery word
            self.list_of_guesses.append(guess) #keeps track of the letters that the user has already tried
            
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        
        elif game.num_letters == 0 and game.num_lives > 0:
            print('Congratulations, you won the game!')
            break

        elif game.num_letters > 0: 
            game.ask_for_input()

        


play_game(['banana', 'apple', 'kiwi', 'orange', 'mango', 'pineapple'])
