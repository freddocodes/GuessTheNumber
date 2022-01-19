import random

print ('Hello. What is your name?')
name=input()

print ('Well '+ name +', I am thinking of a number between 1 and 20, can you guess it ?')
secretNumber = random.randint(1,20)    #generate a random number between 1-20

for guessesTaken in range(1,7):         #here I am giving 6 chances to guess 
    print ('Take a guess.')
    guess = int(input())              
#input returns a string, so we turn it into an integer to apply the if function later

    if guess < secretNumber:
        print ('Your guess is too low.')
    elif guess > secretNumber:
        print ('Your guess is too high.')
    else:
        break                      #the only else in this case would be equal to, or the break after 6 tries.
        
        
# so we code an if/else for both scenarios

if guess == secretNumber:
    print('Good job ' + name + ', you took ' + str(guessesTaken) + ' guesses to find it.')
else:
    print ('Nope. The number I was thinking of was ' + str(secretNumber) + '.')
