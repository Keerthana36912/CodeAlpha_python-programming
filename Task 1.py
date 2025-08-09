import random
words = ["apple", "table", "chair", "water", "train"]
secret_word = random.choice(words)
guessed_word = ["_"] * len(secret_word) 
attempts_left = 6
guessed_letters = []
print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed_word))
while attempts_left > 0 and "_" in guessed_word:
    guess = input("\nEnter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in secret_word:
        print("Good guess!")
        for index, letter in enumerate(secret_word):
            if letter == guess:
                guessed_word[index] = guess
    else:
        print("Wrong guess!")
        attempts_left -= 1
    print("Word:", " ".join(guessed_word))
    print("Attempts left:", attempts_left)
if "_" not in guessed_word:
    print("\n Congratulations! You guessed the word:", secret_word)
else:
    print("\n Game Over! The word was:", secret_word)
