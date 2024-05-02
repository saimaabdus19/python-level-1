print("Welcome to the quiz on Capital cities of the world")

while True:
  guess = str(input("What is the capital of England?"))
  if guess == "London":
    print(f"Correct! The capital of England is {guess}!")
    break
  else:
    print(f"Incorrect, the capital of England is not {guess}")
    print("Try again!")
