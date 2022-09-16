#The secret word the player is trying to guess 
secretword = "library"
lettersguessed = ""

#The number of turns before the player loses
failurecount = 6

#Loop until the player has made too many failed attempts
#will 'break' loop if they succeed instead
while failurecount > 0:

    #Get a guessed letter from the player
    guess = input("Enter a letter: ")

    if guess in secretword:
        #If a player guesses a correct letter
        print(f"Correct! There is one or more {guess} in the secret word.")
    else:
        failurecount -= 1
        print(f"Incorrect. There are no {guess} in the secret word. {failurecount} turn(s) left.")

    #Maintain a list of all letters guessed
    lettersguessed = lettersguessed + guess
    wronglettercount = 0

    for letter in secretword:
        if letter in lettersguessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wronglettercount += 1
    print("")

    #If there were no wrong letters, then the player won!
    if wronglettercount == 0:
        print(f"Congratulations! The secret word was: {secretword}. You won!")
        break

else:
    print("Sorry, you didn't win it this time. Try Again!")
