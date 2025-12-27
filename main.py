import random
from hangman_word import word_list
from hangman_art import stages, logo

lives = 6
print(logo)


choosen_word = random.choice(word_list)

place_holder = ''
word_length = len(choosen_word)
for position in range(word_length):
    place_holder += '_'
print(place_holder)

game_over = False
correct_latter = []

while not game_over:
    
    guesse = input("Gusse a latter: ").lower()
    
    print(f"************* {lives} /6 LIVES LEFT*************.")
    
    if guesse in correct_latter:
        print(f"You've already guessed {guesse}")
    
    display = ""
    for latter in choosen_word:
        if latter == guesse:
            display += latter
            correct_latter.append(guesse)
        elif latter in correct_latter:
            display += latter
        else:
            display += "_"

    print(f"Word to guess: " + display)
    
    if guesse not in choosen_word:
        lives -= 1
        print(f"You guessed {guesse}, that latter not in the word. You lose a life")
        if lives == 0:
            game_over = True
            print(f'************* It Was {choosen_word}! YOU LOSE*************.')
    
    if "_" not in display:
        game_over = True
        print('*************YOU WIN*************.')
        
    print(stages[lives])