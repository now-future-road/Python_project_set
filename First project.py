import random
low = int(input('Enter lower bound: '))
high = int(input('Enter higher bound: '))

number_bot = random.randint(low,high)
attempt = 6
guess = 0
while guess< attempt:
    guess +=1
    guesses = int(input('Enter guesses number: '))

    if guesses == number_bot:
        print('CORRECT!')
        break

    elif guess>=attempt and guesses !=number_bot:
        print('Try next one!')
    elif guesses > high:
        print('Error!')
        continue


    elif guesses> number_bot:
        print('lower')
    
    elif guesses < number_bot:
        print('higher')
    