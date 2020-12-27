from wordsAndDraws import draw_hangman, words
import os, random, time

class HangmanGame():
    __tries = 0
    __predicted = False
    __predict_letter = []
    __predict_word = []
    __secret_word = ""
    __real_word = ""

    def __init__(self, *args, **kwargs): # The user name is taken with the constructor and the screen is pressed.
        os.system('cls' if os.name=='nt' else 'clear')
        word = input("Enter your name for start game : ")
        print("Welcome {}, let's play starting...".format(word))
    
    def __variableInitialize(self): # The variables are reset for game repetitions.
        self.__tries = 6 #right to guess
        self.__predicted = False # guess flag
        self.__predict_letter = [] # wrong predictions what said before
        self.__predict_word = [] # wrong predictions what said before
        self.__secret_word = "" # hidden version of the value to be predicted.
        self.__real_word = "" # value to be predict

    def __getWord(self): # Random word selection is made.
        self.__real_word = (random.choice(words)).upper()
    
    def __secretWordİnitialize(self,word): # It helps to hide the randomly selected word with underscores.
        self.__secret_word = "".join(["_" if x != " " else " " for x in word])
    
    def __secretWordUpdate(self, letterGuess): # secret_word, doğru harf tahminleri için güncellenmiştir.
        correctIndexs = [x for x, char in enumerate(self.__real_word) if letterGuess == char]
        temp = list(self.__secret_word)
        for index in correctIndexs:
            temp[index] = letterGuess
        self.__secret_word = "".join(temp)
    
    def play(self):
        while True:
            self.__variableInitialize() # required methods are executed.
            self.__getWord()
            self.__secretWordİnitialize(self.__real_word)
            
            while not self.__predicted and self.__tries > 0: # game starting.
                time.sleep(1.5)
                os.system('cls' if os.name=='nt' else 'clear')
                print(draw_hangman(self.__tries))
                print((' '.join(x for x in self.__secret_word)) + "\n")
                guess = input("Please guess a letter or word : ").upper() # user is asked to guess.

                if len(guess) == len(self.__real_word) and guess.isalpha(): # if word prediction is made
                    if guess == self.__real_word: # if guess is correct
                        self.__predicted = True
                    else: # if guess is wrong
                        if guess not in self.__predict_word: # if guess is not said before
                            self.__tries -=1
                            print(guess + " is not the requested word.")
                            print("Your right to guess : ", self.__tries)
                            self.__predict_word.append(guess)
                        else: # if guess is said before
                            print("You said {} before.".format(guess))
                            print("Your right to guess : ", self.__tries)

                elif len(guess) == 1 and guess.isalpha(): # if letter prediction is made
                    if guess not in self.__predict_letter: # if guess is not said before
                        if guess in self.__real_word: # if the letter is in the word trying to guess
                            self.__secretWordUpdate(guess)
                            print("Good job, {} is in the word!".format(guess))
                            print("Your right to guess : ", self.__tries)
                            self.__predict_letter.append(guess)
                            if self.__secret_word == self.__real_word:
                                self.__predicted = True
                        else: # if the letter isn't in the word trying to guess
                            self.__tries -= 1
                            print("{} is not in the word.".format(guess))
                            print("Your right to guess : ", self.__tries)
                            self.__predict_letter.append(guess)
                    else: # if guess is said before
                        print("You said {} before.".format(guess))
                        print("Your right to guess : ", self.__tries)

                else: # if invalid prediction is made
                    self.__tries -= 1
                    self.__predict_word.append(guess)
                    print(guess + " is not the requested word.")
                    print("Your right to guess : ", self.__tries)
                    
            time.sleep(1.5)
            os.system('cls' if os.name=='nt' else 'clear')
            print(draw_hangman(self.__tries))
            print(self.__real_word + "\n")

            if self.__predicted == True:
                print("Congrats, you guessed the word! You win!")
            else:
                print("Sorry, your guess is over. Maybe next time.")  

            if input("Play Again? (Y/N) : ").upper() == "Y":
                continue
            else:
                break
        
if __name__ == "__main__":
    game = HangmanGame()
    game.play()