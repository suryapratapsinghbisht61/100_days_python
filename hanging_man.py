import random

word_list = ["billionaire", "money", "sell_drugs", "make_more_money"]
chosen_word = random.choice(word_list)

# Create blanks
display = ""
for _ in range(len(chosen_word)):
    display += "_"

stages = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]

game_end = False
lives = 6
guessed_letters = []

print("Welcome to Hangman!")
print(display)

while not game_end:
    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)
    new_display = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            new_display += letter
        else:
            new_display += "_"

    display = new_display
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")

    print(stages[6 - lives])
    if "_" not in display:
        game_end = True
        print("You win!")
    if lives == 0:
        game_end = True
        print("you lose")
        print(f"The word was: {chosen_word}")