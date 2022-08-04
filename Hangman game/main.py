
import os
import random
import hangman_art
import hangman_words
#another method
from hangman_art import logo,stages
#logo
print(hangman_art.logo)
#choose the word
chosen_word = random.choice(hangman_words.word_list)

#lives intialize
lives = 6
#creating blocks
display = []
for x in range(0,len(chosen_word)):
  display.append("_")
#set the flag
flag = False
#while
while flag != True:
  guess = input("Guess a letter: ").lower()
  os.system('cls')
  if guess in display:
    print(f"You've already guessed {guess}")

  #Checking the guess
  for letter in range(0,len(chosen_word)):
      if guess == chosen_word[letter]:
        display[letter] = guess  
        
# Method 1
      # for i in range(0,len(display)):
      #   if display[i] == "_":
      #     flag = False
      #   else:
      #     flag = True
# Method 2
# You Win/ Game Over
      if "_" not in display:
        flag = True
        print("You won")
          
  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
# You Lose/Game Over
  if lives == 0:
    flag = True
    print("\nYou Lose")
    print(f"The word is: {chosen_word}")

  print(f"{' '.join(display)}")
  print(hangman_art.stages[lives])

input("Press Enter to exit")