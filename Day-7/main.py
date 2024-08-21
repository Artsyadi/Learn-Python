import random
import ascii_art

num = 0
lives = len(ascii_art.hangman)-1
word_list = ["orange" , "apple", "fireworks" , "animal", "image"]
chosen_word = random.choice(word_list)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

correct_letter = []
game_over = 0
while game_over==0:
    print(f"---------You have {lives} lives left-----------")
    guess = input("Guess the letter: ").lower()
    print(guess)

    if guess in correct_letter:
        print(f"You have already guessed {guess}")

    display = ""
    for i in chosen_word:
        if i == guess:
            display += i
            correct_letter.append(i)
        elif i in correct_letter:
            display += i
        else:
            display += "_" 
    print(display)

    if guess not in chosen_word:
        lives -= 1
        num += 1
        print(f"You guessed {guess},that is not the word, you lose a life!")
        if lives == 0:
            game_over = 1
            print(f"-----You Lose!, The word was {chosen_word}-----")

    if "_" not in display:
        print("-------You win!!-------")
        game_over = 1

    print(ascii_art.hangman[num])