# define an instance method GuessingGame#guess (hashtags in documentation generally means it is a method. In our case, GuessingGame has a method called guess)

import random 

class GuessingGame:
    def __init__ (self, answer_num):
        self.answer_num = answer_num
        self.recent_guess = None
        
     # guess takes an integer called user_guess as its input
     # guess should return the string "high" if the user_guess is larger than the [answer]
     # guess should return the string "correct" if the user_guess is equal to the [answer]
     # guess should return the string "low" if the user_guess is lower than the [answer]    
    def guess(self, user_guess):
        if user_guess > self.answer_num:
            self.recent_guess = False
            return "high"
        elif user_guess < self.answer_num:
            self.recent_guess = False
            return "low"
        elif user_guess == self.answer_num:
            self.recent_guess = True
            return "correct"
     # define an instance method GuessingGame#solved which returns True if the most recent user_guess was correct and False otherwise    
    
    def solved(self):
        if self.recent_guess == False:
            return self.recent_guess
        elif self.recent_guess == True:
            return self.recent_guess
        else:
            return "No guess attempted"
            
        
game = GuessingGame(13)

print(game.guess(13))
print(game.solved())

