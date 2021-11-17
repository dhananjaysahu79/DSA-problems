# hangman game
import random
words = ['Hello', 'World', 'huehuehue', 'lalishq', 'yobitch', 'hottie']
def loadGame(word,life):
    guessed = ['_'] * len(word)
    while life and '_' in guessed:
        print('Guess a letter')
        curr_guess = input()
        if curr_guess in word:
            if curr_guess in guessed:
                print('This letter is already guessed :|')
            else:
                print('Its a currect guess :)')
                for i in range(len(word)):
                    if curr_guess == word[i]: guessed[i] = curr_guess
                print(guessed)
        else:
            print('Wrong guess :(')
            print(guessed)
            life -= 1
    print('You Won!' if life else 'Marr gya MC xd')
loadGame(random.choice(words),8)