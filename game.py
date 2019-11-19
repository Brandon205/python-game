# HANGMAN GAME 
import random

words = ['Hello', 'Hangman', 'Word', 'Stuff']
string = random.choice(words)
# print(string)
# show = ['_'] * len(string)
# show = ''.join(show)
# print(show)
# print(string)
show_string = string
for char in string:
  if char == ' ':
    show_string = show_string.replace(char, ' ')
  else:
    show_string = show_string.replace(char, '_')
print(show_string)
guess = input("Guess a letter: ")
lives = len(string)

win_count = 0

while str(show_string) != string.lower() and lives >= 0:
  for i in range(len(string)):
    if string.lower()[i] == guess:
      show_string = list(show_string)
      show_string.insert(i, guess)
      show_string.pop(i + 1)
      show_string = ''.join(show_string)
    elif not guess in string.lower():
      print('That letter is not in the word')
      lives -= 1
      print(lives)
      guess = input('Guess another letter: ')
  if lives > 0:
    print(show_string)
    guess = input('Guess another letter: ')
  else:
    break

if lives <= 0:
  print('Game Over :(')
else:
  print(f'You Win! The word was: {string}')

# while win_count < len(string.strip()) - 1 and lives >= 0:
#   guesses = guess
#   if len(guesses) < 2 and guesses[-1] in string.lower():
#     for i, char in enumerate(show):
#       if char == guesses[-1]:
#         show = list(show)
#         print(show + 'in')
#         show.insert(i, char)
#         # show.pop(i + 1)
#         show = ''.join(show)
#     print(show + 'out')
#     win_count += 1
#     guess = input('Guess another letter: ')
#   else:
#     lives -= 1
#     print(lives)
#     guess = input('Guess another letter: ')
