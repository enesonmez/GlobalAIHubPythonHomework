from wordsAndDraws import draw_hangman, words
import os, random, time


class HangmanGame():
    __tries = 0
    __predicted = False
    __predict_letter = []
    __predict_word = []
    __secret_word = ""
    __real_word = ""

    def __init__(self, *args, **kwargs):
        os.system('cls' if os.name=='nt' else 'clear')
        word = input("Enter your name for start game : ")
        print("Welcome {}, let's play starting...".format(word))
    
    def __variableInitialize(self):
        self.__tries = 6
        self.__predicted = False
        self.__predict_letter = []
        self.__predict_word = []
        self.__secret_word = ""
        self.__real_word = ""

    def __getWord(self):
        self.__real_word = (random.choice(words)).upper()
    
    def __secretWordİnitialize(self,word):
        self.__secret_word = "".join(["_" if x != " " else " " for x in word])
    
    def __secretWordUpdate(self, letterGuess):
        correctIndexs = [x for x, char in enumerate(self.__real_word) if letterGuess == char]
        temp = list(self.__secret_word)
        for index in correctIndexs:
            temp[index] = letterGuess
        self.__secret_word = "".join(temp)
    
    def play(self):
        while True:
            self.__variableInitialize()
            self.__getWord()
            self.__secretWordİnitialize(self.__real_word)
            
            while not self.__predicted and self.__tries > 0:
                time.sleep(1.5)
                os.system('cls' if os.name=='nt' else 'clear')
                print(draw_hangman(self.__tries))
                print((' '.join(x for x in self.__secret_word)) + "\n")
                guess = input("Please guess a letter or word : ").upper()

                if len(guess) == len(self.__real_word) and guess.isalpha():
                    if guess == self.__real_word:
                        self.__predicted = True
                    else:
                        if guess not in self.__predict_word:
                            self.__tries -=1
                            print(guess + " is not the requested word.")
                            print("Your right to guess : ", self.__tries)
                            self.__predict_word.append(guess)
                        else:
                            print("You said {} before.".format(guess))
                            print("Your right to guess : ", self.__tries)

                elif len(guess) == 1 and guess.isalpha():
                    if guess not in self.__predict_letter:
                        if guess in self.__real_word:
                            self.__secretWordUpdate(guess)
                            print("Good job, {} is in the word!".format(guess))
                            print("Your right to guess : ", self.__tries)
                            self.__predict_letter.append(guess)
                            if self.__secret_word == self.__real_word:
                                self.__predicted = True
                        else:
                            self.__tries -= 1
                            print("{} is not in the word.".format(guess))
                            print("Your right to guess : ", self.__tries)
                            self.__predict_letter.append(guess)
                    else:
                        print("You said {} before.".format(guess))
                        print("Your right to guess : ", self.__tries)

                else:
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