import random

# Predefined list of words
word_list = ["apple", "bread", "chair", "dance", "eagle"]
# Randomly choose one word
secret_word = random.choice(word_list)

# Create a list to display guessed letters and underscores
guessed_word = ["_"] * len(secret_word)

# List to keep track of wrong guesses
wrong_guesses = []
max_attempts = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have", max_attempts, "incorrect guesses allowed.")

# Game loop
while "_" in guessed_word and len(wrong_guesses) < max_attempts:
    print("\nCurrent word: ", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single valid letter.")
        continue

    if guess in guessed_word or guess in wrong_guesses:
        print("⚠️ You already guessed that letter.")
        continue

    if guess in secret_word:
        print("✅ Good guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        wrong_guesses.append(guess)
        print("Incorrect guesses left:", max_attempts - len(wrong_guesses))

# End of game result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 Game Over! The word was:", secret_word)
