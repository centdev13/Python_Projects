##########################################################################
##
## CS 101
## Program 2
## J Clement	
## JJC7WB@mail.umkc.edu
##
## PROBLEM: We will be simulating Roulette. We will need to get the pot, wager, type of bet, number slot the ball will land on and increments/decrements variable values accordingly based
##          on if the user wins each round or not.  Output the results when the user is done playing.
##
## ALGORITHM: 
##	1. Get the amount of money the user wants to add to their pot. If less than/equal to 0 than reprompt the
##	   user for this value.
##	2. Get the amount they'd like to wager.  If less than/equal to 0 than reprompt the
##	   user for this value. If more than the pot value, reprompt the user for this value.
##	2. Get the type of bet the user would like to do- either Straight/Even/Odd.  If the type of bet entered from the user is
##	   s, e, or o it is valid and there will be pieces of code that will run based on which type of bet is chosen.  The remaining code
##	   will be nested within each of the sections of code sectioned off by the type of bet chosen.
##	3. Ask for a slot number they guess that the roulette ball will drop into after the wheel stops spinning.
##	4. Generate a random number and compare the person's number guess with this random number. If they guessed
##	   right, increment their pot.  If wrong decrement it. When they win- add the pot's value to a list that we
##	   we will use to enumerate the highest pot value attained during the game for the user.
##	5. Increment the rounds variable to keep track of how many rounds they are playing.
##	6. Ask the user if they want to play again.
## 	7. If yes, send them back to the loop that encapsulates the code starting at getting the 
##	   user's waging amount.
##	8. If no, output how many rounds they've played and the highest value in the list of pot values we collected, and
##	   end the game.



import random

pot = 0
wager_loop_restart = 'y'
wager = 0
type_of_bet = ''
number_guess = -1
play_again = 'y'
play_again_loop_restart = 'y'
s_rand = -1
e_rand = -1
o_rand = -1
pot_initialized = 'n'
game_loop_restart = 'y'
rounds = 0
high_amount_calc = [pot]
extra_info = "\n\nRoulette is a game where you have a pot(total money to bet with), a wager(the amount you are betting in a specific hand), \
The type of bet (Straight-any number, Even-only even number, Odd-only odd numbers), and the number slot where you think the \
roulette wheel will drop the ball in (win/lose). The roulette wheel will then spin and if the ball lands in the slot you \
guessed then you win the odds based on the type of bet.  Straight wins 35, loses 1.  Even wins 1, loses 1. Odd wins 1, loses 1.\n\n"
extra_info_input = ''
high_amount = 0
amount_began_game_with = 0



#while loop to keep game restarting automatically
while game_loop_restart == 'y':
    ##once the user puts a cash value amount in the pot, they can't add any to the pot for the rest of the game, so when pot is initialized with a value, the pot is unaccessable
    if pot_initialized == 'n':
        ##before the game starts we ask if the user wants to learn more about Roulette before starting.
        extra_info_input = input("Enter 'H' to learn more about the game of Roulette before beginning.\n").lower()
        if extra_info_input == 'h':
            print(extra_info)
        ##if the user enters anything but 'h', we just move on to the game and they'd have to restart the python program to see it again.
        elif extra_info_input != 'h':
            print("I guess we'll move on then...\n\n")
        pot = int(input("Enter a pot amount ==>  "))
        ##while the pot value input that the user gives is not greater than 0, keep prompting them for this information.
        while pot <= 0:
            print("You must enter a positive integer.\n\n")
            pot = int(input("Pot amount ==>  "))
        amount_began_game_with = pot
    ##setting this value is what prevents the pot from being added to once the game begins.
    pot_initialized = 'y'





    
    ##This if loop is in place so that if the user wants to play again, we start here instead of asking for a pot value again. The play_again value is used to conditionally break out of nested loops below.
    if pot_initialized == 'y' and play_again == 'y':
        wager = int(input("Enter an amount to wager ==>  "))
        ##if the amount the user wants to wager is less than or equal to '0', then we want to ask the user for a positive integer.
        while wager <= 0:
            print("You must enter a positive integer.\n\n")
            wager = int(input("wager amount ==>  "))
        ##if the amount the user wants to wager is more than what is in their pot currently, then we need to get a new value from the user that is valid.
        while wager > pot:
            print("The amount you are wagering cannot be more than pot amount")
            wager = int(input("Enter an amount to wager ==>  "))
        type_of_bet = input("What type of bet would you like to make? (S)traight, (E)ven, or (O)dd.").lower()
        ##if the user chooses the straight type bet, do the following code...





        
        if type_of_bet == 's':
            ##Prompt the user for an even number 
            number_guess = int(input("Enter a number between 0 and 36 ==>  "))
            ##is the even number guessed within the correct range??
            while number_guess >= 0 and number_guess <= 36:
                ##get a fresh random number and store it in a variable that is only going to be used with the straight bet type
                s_rand = random.randint(0,36)
                print("Spinning roulette wheel.\n\n")
                ##let the user know where their ball landed on the roulette wheel (to check if the random number generated matches their number guess)
                print("The ball landed on "+str(s_rand))
                ##if they guessed correctly, do the following..
                if number_guess == s_rand:
                    print("You won!\n")
                    ##increment the round total
                    rounds += 1
                    ##add the pot amount currently to the high amount calc list for later analysis
                    high_amount_calc.append(pot)
                    ##give the user their win, add it to their pot total
                    pot += 35
                    ##get the high pot amounts sorted and check the highest numeric value in the range.
                    high_amount_calc.sort()
                    ##whatever that value is, put it in the variable so we can report it to the user.
                    high_amount = high_amount_calc.pop()
                    print("You have $"+str(pot)+" left.")
                    play_again = input("Do you want to play again? ==>  ").lower()
                    ##if the user has entered 'n' to discontinue playing the game, then we execute the following code...
                    if play_again == 'n':
                        ##by setting the below variable equal to 'n', we ensure that the encapsulating loop which restarts the game will not run anymore.
                         game_loop_restart = 'n'
                         ##when we got the pot value initially from the user, we set this value equal to another variable called 'amount_began_with' to keep track if the user ever gets higher than what they started with
                         ## in their pot.  
                         if high_amount != amount_began_game_with:
                             ##You played [this number of rounds], and had a high pot value of [this much]...
                             print("You played a total of "+str(rounds)+" and had a high amount of "+str(high_amount))
                             print("\n\nGame Over...\n\n")
                             break
                         ##If the user's end pot value is below what they started with then we dont give them any updated news, but just remind them that they didnt make any profit..
                         elif high_amount == amount_began_game_with:
                             ##You played [this number of rounds], and had a high pot value of [this much]...
                             print("You played a total of "+str(rounds)+" and your highest pot amount was what you started with.")
                             print("\n\nGame Over...\n\n")
                             break
                    ##If play_again is set to true, then we give 'number_guess' the value outside it's conditional range which will break the enclosing loop and restart the sequence above.
                    elif play_again == 'y':
                        ##reset all loop values
                        wager_loop_restart = 'y'
                        wager = 0
                        type_of_bet = ''
                        number_guess = -1
                        play_again = 'y'
                        s_rand = -1
                        e_rand = -1
                        o_rand = -1
                        number_guess = 37
                ##if their ball didnt land in the right slot
                elif number_guess != s_rand:
                    print("You lost!\n")
                    ##increment the round total
                    rounds += 1
                    ##add the pot amount currently to the high amount calc list for later analysis
                    high_amount_calc.append(pot)
                    ##decrement their pot total
                    pot -= 1
                    ##get the high pot amounts sorted and check the highest numeric value in the range.
                    high_amount_calc.sort()
                    ##whatever that value is, put it in the variable so we can report it to the user.
                    high_amount = high_amount_calc.pop()
                    print("You have $"+str(pot)+" left.")
                    play_again = input("Do you want to play again? ==>  ").lower()

                    
                    if play_again_loop_restart == 'y':
                        if play_again == 'n':
                             game_loop_restart = 'n'
                             if high_amount != amount_began_game_with:
                                 print("You played a total of "+str(rounds)+" and had a high amount of "+str(high_amount))
                                 print("\n\nGame Over...\n\n")
                                 break
                             elif high_amount == amount_began_game_with:
                                 print("You played a total of "+str(rounds)+" and your highest pot amount was what you started with.")
                                 print("\n\nGame Over...\n\n")
                                 break
                             break
                        else:
                            play_again_loop_restart = 'n'
                    play_again_loop_restart = 'n'
                    if play_again == 'y':
                        ##reset all loop values
                        wager_loop_restart = 'y'
                        wager = 0
                        type_of_bet = ''
                        number_guess = -1
                        play_again = 'y'
                        play_again_loop_restart = 'y'
                        s_rand = -1
                        e_rand = -1
                        o_rand = -1
                        number_guess = 37
        ##if the user chooses the even type bet, do the following code...                        
        elif type_of_bet == 'e':
            number_guess = int(input("Enter a number between 2 and 36 ==>  "))
            while number_guess >= 2 and number_guess <= 36:
                while number_guess %2 != 0:
                    print("You must enter an even number.\n")
                    number_guess = int(input("Enter a number between 2 and 36 ==>  "))
                e_rand = random.randint(2,36)
                print("Spinning roulette wheel.\n\n")
                print("The ball landed on "+str(e_rand))
                if number_guess == e_rand:
                    print("You won!\n")
                    rounds += 1
                    high_amount_calc.append(pot)
                    pot += 1
                    high_amount_calc.sort()
                    high_amount = high_amount_calc.pop()
                    print("You have $"+str(pot)+" left.")
                    play_again = input("Do you want to play again? ==>  ").lower()
                    if play_again_loop_restart == 'y':
                        if play_again == 'n':
                             game_loop_restart = 'n'
                             if high_amount != amount_began_game_with:
                                 print("You played a total of "+str(rounds)+" and had a high amount of "+str(high_amount))
                                 print("\n\nGame Over...\n\n")
                                 break
                             elif high_amount == amount_began_game_with:
                                 print("You played a total of "+str(rounds)+" and your highest pot amount was what you started with.")
                                 print("\n\nGame Over...\n\n")
                                 break
                             break
                        else:
                            play_again_loop_restart = 'n'
                    play_again_loop_restart = 'n'
                    if play_again == 'y':
                        ##reset all loop values
                        wager_loop_restart = 'y'
                        wager = 0
                        type_of_bet = ''
                        number_guess = -1
                        play_again = 'y'
                        play_again_loop_restart = 'y'
                        s_rand = -1
                        e_rand = -1
                        o_rand = -1
                        number_guess = 37
                elif number_guess != e_rand:
                    print("You lost!\n")
                    ##Increment the global variable keeping track of the amount of rounds played
                    rounds += 1
                    ##add the initial value of the user's pot from the start of the game to the high_amount list, so we can calculate the user's highest pot amount when they are done playing.
                    high_amount_calc.append(pot)
                    ##If the pot is greater than 0, then decrement the pot's value by one, because if not it will be a negative value, which is invalid for our purposes.
                    if pot > 0:
                        pot -= 1
                    ##sort all the high pot amount values
                    high_amount_calc.sort()
                    ##pop off the last value on the list, which is the greatest numeric value and set it equal to a variable 'high_amount'
                    high_amount = high_amount_calc.pop()
                    ##read the numeric value currently in the 'pot' variable and let the user know how much money they have left to play with in their pot.
                    print("You have $"+str(pot)+" left.")
                    play_again = input("Do you want to play again? ==>  ").lower()                    
                    if play_again_loop_restart == 'y':
                        if play_again == 'n':
                             game_loop_restart = 'n'
                             if high_amount != amount_began_game_with:
                                 print("You played a total of "+str(rounds)+" and had a high amount of "+str(high_amount))
                                 print("\n\nGame Over...\n\n")
                                 break
                             elif high_amount == amount_began_game_with:
                                 print("You played a total of "+str(rounds)+" and your highest pot amount was what you started with.")
                                 print("\n\nGame Over...\n\n")
                                 break
                             break
                        else:
                            play_again_loop_restart = 'n'
                    play_again_loop_restart = 'n'
                    if play_again == 'y':
                        ##reset all loop values
                        wager_loop_restart = 'y'
                        wager = 0
                        type_of_bet = ''
                        number_guess = -1
                        play_again = 'y'
                        play_again_loop_restart = 'y'
                        s_rand = -1
                        e_rand = -1
                        o_rand = -1
                        number_guess = 37
        ##if the user chooses the odd type bet, do the following code...
        elif type_of_bet == 'o':
            number_guess = int(input("Enter a number between 1 and 36 ==>  "))
            while number_guess >= 1 and number_guess <= 36:
                while number_guess %2 == 0:
                    print("You must enter an odd number.\n")
                    number_guess = int(input("Enter a number between 1 and 36 ==>  "))
                o_rand = random.randint(1,36)
                print("Spinning roulette wheel.\n\n")
                print("The ball landed on "+str(e_rand))
                if number_guess == o_rand:
                    print("You won!\n")
                    rounds += 1
                    high_amount_calc.append(pot)
                    pot += 1
                    high_amount_calc.sort()
                    high_amount = high_amount_calc.pop()
                    print("You have $"+str(pot)+" left.")
                    play_again = input("Do you want to play again? ==>  ").lower()
                    if play_again_loop_restart == 'y':
                        if play_again == 'n':
                             game_loop_restart = 'n'
                             if high_amount != amount_began_game_with:
                                 print("You played a total of "+str(rounds)+" and had a high amount of "+str(high_amount))
                                 print("\n\nGame Over...\n\n")
                                 break
                             elif high_amount == amount_began_game_with:
                                 print("You played a total of "+str(rounds)+" and your highest pot amount was what you started with.")
                                 print("\n\nGame Over...\n\n")
                                 break
                             break
                        else:
                            play_again_loop_restart = 'n'
                    play_again_loop_restart = 'n'
                    if play_again == 'y':
                        ##reset all loop values
                        wager_loop_restart = 'y'
                        wager = 0
                        type_of_bet = ''
                        number_guess = -1
                        play_again = 'y'
                        play_again_loop_restart = 'y'
                        s_rand = -1
                        e_rand = -1
                        o_rand = -1
                        number_guess = 37
                elif number_guess != o_rand:
                    print("You lost!\n")
                    ##Increment the global variable keeping track of the amount of rounds played
                    rounds += 1
                    ##add the initial value of the user's pot from the start of the game to the high_amount list, so we can calculate the user's highest pot amount when they are done playing.
                    high_amount_calc.append(pot)
                    ##If the pot is greater than 0, then decrement the pot's value by one, because if not it will be a negative value, which is invalid for our purposes.
                    if pot > 0:
                        pot -= 1
                    ##sort all the high pot amount values
                    high_amount_calc.sort()
                    ##pop off the last value on the list, which is the greatest numeric value and set it equal to a variable 'high_amount'
                    high_amount = high_amount_calc.pop()
                    ##read the numeric value currently in the 'pot' variable and let the user know how much money they have left to play with in their pot.
                    print("You have $"+str(pot)+" left.")
                    play_again = input("Do you want to play again? ==>  ").lower()                    
                    if play_again_loop_restart == 'y':
                        ##if the user has entered 'n' to discontinue playing the game, then we execute the following code...
                        if play_again == 'n':
                            ##by setting the below variable equal to 'n', we ensure that the encapsulating loop which restarts the game will not run anymore.
                             game_loop_restart = 'n'
                             ##when we got the pot value initially from the user, we set this value equal to another variable called 'amount_began_with' to keep track if the user ever gets higher than what they started with
                             ## in their pot.  
                             if high_amount != amount_began_game_with:
                                 ##You played [this number of rounds], and had a high pot value of [this much]...
                                 print("You played a total of "+str(rounds)+" and had a high amount of "+str(high_amount))
                                 print("\n\nGame Over...\n\n")
                                 break
                             ##If the user's end pot value is below what they started with then we dont give them any updated news, but just remind them that they didnt make any profit..
                             elif high_amount == amount_began_game_with:
                                 ##You played [this number of rounds], and had a high pot value of [this much]...
                                 print("You played a total of "+str(rounds)+" and your highest pot amount was what you started with.")
                                 print("\n\nGame Over...\n\n")
                                 ##break out of the elif loop
                                 break
                             ##break out of the if loop
                             break
                        else:
                            ##if the user entered 'n' for not continuing the game, then set a variable 'play_again_loop_restart'  equal to 'n' so that its condition is false and it doesnt run again.
                            play_again_loop_restart = 'n'
                    ##If play_again is set to true, then we give 'number_guess' the value outside it's conditional range which will break the enclosing loop and restart the sequence above.
                    if play_again == 'y':
                        ##reset all loop values
                        wager_loop_restart = 'y'
                        wager = 0
                        type_of_bet = ''
                        number_guess = -1
                        play_again = 'y'
                        play_again_loop_restart = 'y'
                        s_rand = -1
                        e_rand = -1
                        o_rand = -1
                        number_guess = 37



