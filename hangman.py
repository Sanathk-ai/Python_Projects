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

letter_index = []
guessed = []
print(rand_word)
print("Word to Guess: "+ f"{len(rand_word)*'_'}")
def dashes():
    ind = 0
    dash = ""
    for char in rand_word:
        if char == guessed_letter:
            letter_index.append(ind)
        ind += 1
    for index in range(len(rand_word)):
        if index in letter_index:
            dash += rand_word[index]
        else:
            dash += "_"
    print("Word to Guess: " + f"{dash}")

while lives > 0 and (len(letter_index)!=len(rand_word)):

    guessed_letter = input("Guess a letter: ")
    if guessed_letter in guessed:
        print("You've already guessed that letter!")

    if guessed_letter not in rand_word:
        lives -= 1
        print(f"You've guessed {guessed_letter}, that's not in the word. You lose a life")
        print(diagrams[diag_count])
        diag_count += 1
        print(f"****************************{lives}/6 LIVES LEFT****************************")
    elif guessed_letter not in guessed:
        guessed.append(guessed_letter)
        dashes()

if lives == 0:
    print(f"***********************IT WAS {rand_word}! YOU LOSE**********************")
else:
    print(f'You Guessed it right!! The word is "{rand_word}"')


