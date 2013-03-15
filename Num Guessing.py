#this is a number game
import random, sys
import time
def main():
    guesses = 6

    name=raw_input("Please enter your name.")

    number = random.randint(1,20)

    print "Okay,"+name+", are you ready?"
    print"I am thinking of a number between 1 and 20"

    while guesses > 0:
        print "Take a guess, wish you luck!"
        guess = int(raw_input("Type in your guess."))
        if guess < number:
            print"Too low."
            guesses = guesses - 1
        if guess > number:
            print "Too high."
            guesses = guesses - 1
        if guess == number:
            break
    if guess == number:
        guesses = guesses - 1
        print "Hooray! You got it "+name+"!"
        print "Your score:"
        print guesses
        time.sleep(10)    
    if guess != number:
        number = str(number)
        print "Sorry, "+name+",the number was",number
def playagain():
    time.sleep(5)
    for looper in[1,2]:
        play = raw_input("Play again? (y or n)")
        if play == 'y':
            main()
            break
        if play == 'n':       
            sys.exit()
            break
main()
while 1:
    playagain()
