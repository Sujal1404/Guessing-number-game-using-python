import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")
print("change the number using high and low ")
low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")
num = random.randint(low, high) 
ch = 7                        
gc = 0                        

while gc < ch:
    gc += 1
    guess = int(input('Enter your guess: '))

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
        break

    elif gc >= ch and guess != num:
        print(f'orry! The number was {num}. Better luck next time. Try again game  guess the number')

    elif guess > num:
        print('Too high! Try again a lower number.')

    elif guess < num:
        print('Too low! Try again ' 
              'a higher number.')
