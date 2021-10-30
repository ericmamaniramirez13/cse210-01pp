#Import random package to generate random numbers
import random as rd
#Function hilo will be the game itself
def hilo(card, score, again):
    #The while statement will repeat the game until score goes below 0 or again is n
    while again == "y" and score>0:
        print("The card is: ", card)
        guess = input("Higher or Lower? [h/l]: ")
        card_next = rd.randint(1,13)
        #Here we verify the card and next card must be different
        if card == card_next:
            card_next = final_card(card, card_next)
        print("Next card was: ", card_next)
        #Here we add 100 to score if guess is correct
        if card_next > card and guess =="h":
            score+=100
        elif card_next < card and guess == "l":
            score+=100
        #If the guess is incorrect we substract 75
        else:
            score-=75
        print("Score: ", score)
        card = card_next
        #We ask the user if he/she wants to play again
        again = input("Do you want to play again? [y/n]: ")
        #If player decides to stop playing and score is greater than 0 it will print the score
        if(score> 0 and again == "n"):
            print("\nYour final SCORE is: ", score)
        #If player score goes to 0 or below it will print "YOU LOST"
        elif score<=0:
            print("YOU LOST!!")
#Function final_card will return us the next card in case we receive the same card number
def final_card(x, card_next):
    card_next= rd.randint(1,13)
    while card_next == x:
        card_next = rd.randint(1,13)
    return(card_next)
#The main function will give us the start values 
def main():
    print("Welcome to Hilo_Game: \n")
    card = rd.randint(1,13)
    score = 300
    again = "y"
    hilo(card, score, again)
#Here we start the probram by calling the function main
main()