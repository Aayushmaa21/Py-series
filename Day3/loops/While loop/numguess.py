secret_number = 777

print(
"""
+================================+
| Welcome to my game, user!      |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
guess = int(input("Enter your guess: "))
while(guess != secret_number):
    print("Try Again!!")
    guess = int(input("Enter your guess: "))
print("Congrats, You guessed it correctly!!")