import random

print('''

██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
''')

words = ["tycoon", "word", "hangman", "laptop", "bird", "mouse", "monitor", "keyboard"]
diag_count = 0
diagrams= ['''  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''+---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''+---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''+---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''+---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



rand_word = random.choice(words)
lives = 6
print(rand_word)
while lives > 0:
    print("Word to Guess: "+ f"{len(rand_word)*'_'}")
    guessed_letter = input("Guess a letter: ")

    if guessed_letter not in rand_word:
        lives -= 1
        print(f"You've guessed {guessed_letter}, that's not in the word. You lose a life")
        print(diagrams[diag_count])
        diag_count += 1
        print(f"****************************{lives}/6 LIVES LEFT****************************")
    else:
        letter_index = rand_word.find(guessed_letter)

        print(letter_index)
if(lives == 0):
    print(f"***********************IT WAS {rand_word}! YOU LOSE**********************")


