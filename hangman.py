import random

words = {
    "python": "Programming Language",
    "elephant": "A Large Animal",
    "computer": "Electronic Device",
    "football": "Popular Sport",
    "internet": "Global Network"
}

HANGMAN = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def play_game():
    word, hint = random.choice(list(words.items()))
    guessed = []
    wrong = 0
    max_attempts = 6

    print("\n🎮 Welcome to Advanced Hangman!")
    print("💡 Hint:", hint)

    while wrong < max_attempts:
        print(HANGMAN[wrong])

        display = ""
        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "

        print("Word:", display)

        if "_" not in display:
            print("\n🏆 Congratulations! You guessed:", word)
            return

        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Enter only one alphabet.")
            continue

        if guess in guessed:
            print("⚠ Letter already guessed.")
            continue

        guessed.append(guess)

        if guess not in word:
            wrong += 1
            print("❌ Wrong Guess!")
            print("Remaining Attempts:", max_attempts - wrong)
        else:
            print("✅ Correct Guess!")

    print(HANGMAN[6])
    print("\n💀 Game Over!")
    print("Correct Word:", word)

while True:
    play_game()

    choice = input("\nPlay Again? (y/n): ").lower()

    if choice != "y":
        print("👋 Thanks for Playing!")
        break