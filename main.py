import random

best = None

while True:
  number = random.randint(1, 50)
  guesses_left = 7
  
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 50.")
  print("You have 7 guesses. Good luck!\n")
  while guesses_left > 0:
    user_input = input("Enter your guess: ")

    if not user_input.isdigit():
      print("Please enter a whole number.\n")
      continue

    guess = int(user_input)


    if guess < 1 or guess > 50:
      print("Stay in range: 1-50\n")
      continue
    
    if guess == number:
      used_guesses = 7 - guesses_left + 1
      tries_word = "try" if used_guesses == 1 else "tries"
      print(f"Correct! You win!\n You guessed the number in  {used_guesses} {tries_word}!")
      
      if best is None or used_guesses < best:
        best = used_guesses
        print(f"New best: {best} {'try' if best == 1 else 'tries'}!")
        print(f"Best so far: {best} {'try' if best == 1 else 'tries'}!")
      break
    else:
      guesses_left -= 1
    if guess < number:
      print("Too low!")
    else:
      print("Too high!")
    print(f"Wrong! You have {guesses_left} guesses left.\n")
  if guesses_left == 0:
    print(f"Sorry, you lose. The number was {number}. Better luck next time!")
  playAgain = input("\nPlay again? (yes/no): ").lower()
  if playAgain != "yes":
    print("Thanks for playing!")
    break