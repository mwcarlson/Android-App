#used for the computer's rock, paper, scissors selection
from random import randint

#used to give the computer time to try the trick
import time 

#lets the player choose their terrain and difficulty
def player_selections():
    print("Choose where you want to play:")
    print("\t1. Flatground")
    print("\t2. Manual pad")
    print("\t3. Ledge")
    print("\t4. Rail")
    print("\t5. Gap")
    print("\t6. Small stair set")
    print("\t7. Large stair set")
    print("\t8. Quarterpipe")
    print("\t9. Vert ramp")
    terrain = input("\t")                             #FINISHED

    print("\nChoose your difficulty:")
    print("\t1. Beginner")
    print("\t2. Easy")
    print("\t3. Intermediate")
    print("\t4. Advanced")
    print("\t5. Impossible")
    difficulty = input("\t")

    return terrain, difficulty

def populate_list(trick_file):
    trick_list = [] #declare a list to store tricks in
    trick_dict = dict()
    file = open(trick_file, "r")                          #TODO: populate trick_dict
    for line in file:
        line = line.strip()
        trick_list.append(line)

    i = 0
    for line in file: #populate the trick dictionary with tricks and incremented i as indices
        line = line.strip()
        trick_dict[i] = line #this line should work but i'm not sure (how you append to a dictionary)
        i += 1

    return trick_list, trick_dict

#decided which file to get tricks from
def get_tricks(terrain, difficulty):
    if terrain == "1" and difficulty == "1":
        trick_list, trick_dict = populate_list("flatground.txt") #flatground    #TODO: add trick_dict to the rest of these lines

    elif terrain == "1" and difficulty == "2":
        trick_list = populate_list("flatground_easy.txt")                       #FINISHED?

    elif terrain == "1" and difficulty == "3":
        trick_list = populate_list("flatground_intermediate.txt")

    elif terrain == "1" and difficulty == "4":
        trick_list = populate_list("flatground_advanced.txt")

    elif terrain == "1" and difficulty == "5":
        trick_list = populate_list("flatground_impossible.txt")

    elif terrain == "2" and difficulty == "1":
        trick_list = populate_list("manual_beginner.txt") #manual pad

    elif terrain == "2" and difficulty == "2":
        trick_list = populate_list("manual_easy.txt")

    elif terrain == "2" and difficulty == "3":
        trick_list = populate_list("manual_intermediate.txt")

    elif terrain == "2" and difficulty == "4":
        trick_list = populate_list("manual_advanced.txt")

    elif terrain == "2" and difficulty == "5":
        trick_list = populate_list("manual_impossible.txt")

    elif terrain == "3" and difficulty == "1": #ledge
        trick_list = populate_list("ledge_beginner.txt")

    elif terrain == "3" and difficulty == "2":
        trick_list = populate_list("ledge_easy.txt")

    elif terrain == "3" and difficulty == "3":
        trick_list = populate_list("ledge_intermediate.txt")

    elif terrain == "3" and difficulty == "4":
        trick_list = populate_list("ledge_advanced.txt")

    elif terrain == "3" and difficulty == "5":
        trick_list = populate_list("ledge_impossible.txt")

    elif terrain == "4" and difficulty == "1": #rail
        trick_list = populate_list("rail_beginner.txt")

    elif terrain == "4" and difficulty == "2":
        trick_list = populate_list("rail_easy.txt")

    elif terrain == "4" and difficulty == "3":
        trick_list = populate_list("rail_intermediate.txt")

    elif terrain == "4" and difficulty == "4":
        trick_list = populate_list("rail_advanced.txt")

    elif terrain == "4" and difficulty == "5":
        trick_list = populate_list("rail_impossible.txt")

    elif terrain == "5" and difficulty == "1": #gap
        trick_list = populate_list("gap_beginner.txt")

    elif terrain == "5" and difficulty == "2":
        trick_list = populate_list("gap_easy.txt")

    elif terrain == "5" and difficulty == "3":
        trick_list = populate_list("gap_intermediate.txt")

    elif terrain == "5" and difficulty == "4":
        trick_list = populate_list("gap_advanced.txt")

    elif terrain == "5" and difficulty == "5":
        trick_list = populate_list("gap_impossible.txt")

    elif terrain == "6" and difficulty == "1": #small stair set
        trick_list = populate_list("small_stair_beginner.txt")

    elif terrain == "6" and difficulty == "2":
        trick_list = populate_list("small_stair_easy.txt")

    elif terrain == "6" and difficulty == "3":
        trick_list = populate_list("small_stair_intermediate.txt")

    elif terrain == "6" and difficulty == "4":
        trick_list = populate_list("small_stair_advanced.txt")

    elif terrain == "6" and difficulty == "5":
        trick_list = populate_list("small_stair_impossible.txt")

    elif terrain == "7" and difficulty == "1": #large stair set
        trick_list = populate_list("large_stair_beginner.txt")

    elif terrain == "7" and difficulty == "2":
        trick_list = populate_list("large_stair_easy.txt")

    elif terrain == "7" and difficulty == "3":
        trick_list = populate_list("large_stair_intermediate.txt")

    elif terrain == "7" and difficulty == "4":
        trick_list = populate_list("large_stair_advanced.txt")

    elif terrain == "7" and difficulty == "5":
        trick_list = populate_list("large_stair_impossible.txt")

    elif terrain == "8" and difficulty == "1": 
        trick_list = populate_list("quarter_beginner.txt") #quarterpipe

    elif terrain == "8" and difficulty == "2":
        trick_list = populate_list("quarter_easy.txt")

    elif terrain == "8" and difficulty == "3":
        trick_list = populate_list("quarter_intermediate.txt")

    elif terrain == "8" and difficulty == "4":
        trick_list = populate_list("quarter_advanced.txt")

    elif terrain == "8" and difficulty == "5":
        trick_list = populate_list("quarter_impossible.txt")

    elif terrain == "9" and difficulty == "1": 
        trick_list = populate_list("vert_beginner.txt") #vert ramp

    elif terrain == "9" and difficulty == "2":
        trick_list = populate_list("vert_easy.txt")

    elif terrain == "9" and difficulty == "3":
        trick_list = populate_list("vert_intermediate.txt")

    elif terrain == "9" and difficulty == "4":
        trick_list = populate_list("vert_advanced.txt")

    elif terrain == "9" and difficulty == "5":
        trick_list = populate_list("vert_impossible.txt")

    return trick_list, trick_dict
        

#simulates a game of rock, paper, scissors
def roshambo():        #TODO: print the computer's choice (maybe use a dictionary or just a list)
    print("*** Rock, paper, scissors! ***")

    possibilities = ["Rock", "Paper", "Scissors"]
    finish = False #decides if the game has been finished playing (no ties)
    player_win = False #decides if the player won or the computer won
    
    while finish == False:
        player_choice = int(input("\t1. Rock\n\t2. Paper\n\t3. Scissors\n\t")) #player chooses a value between 1 and 3
        computer_choice = randint(1,3) #computer chooses a random number between 1 and 3

        print("You chose: ", possibilities[player_choice - 1], "\nComputer chose: ", possibilities[computer_choice - 1], sep="")

        if player_choice == computer_choice: #tie
            print("Tie! Choose again!")
            finish = False

        elif player_choice == 1 and computer_choice == 2: #player rock, computer paper
            print("The computer wins!")
            finish = True

        elif player_choice == 1 and computer_choice == 3: #player rock, computer scissors               #FINISHED
            print("The player wins!")
            player_win = True
            finish = True

        elif player_choice == 2 and computer_choice == 1: #player paper, computer rock
            print("The player wins!")
            player_win = True
            finish = True

        elif player_choice == 2 and computer_choice == 3: #player paper, computer scissors
            print("The computer wins!")
            finish = True

        elif player_choice == 3 and computer_choice == 1: #player scissors, computer rock
            print("The computer wins!")
            finish = True

        elif player_choice == 3 and computer_choice == 2: #player scissors, computer paper
            print("The player wins!")
            player_win = True
            finish = True        

    return player_win #returns True if the player won, False if they didn't

def player_turn(trick_list, trick_dict, computer_letters, player_letters):                     #TODO: implement!
    print("\n*** Player's turn ***")

    turn == True

    while turn == True:
        player_trick = input("\nEnter the trick you want to try:\n") #find the trick they entered in the actual trick list
        trick_index_from_dict = trick_dict[player_trick] #returns the index of the trick in trick_list
        trick_from_list = trick_list[trick_index_from_dict] #returns the trick itself
        print("You are trying a:", trick_from_list) #echo the trick they're trying from trick_list

        land = input("Did you land the trick?:\n\t1. Yes\n\t2. No")

        if land == "1": #player landed the trick
            print("The computer is trying the trick!")
            time.sleep(2)
            computer_land = randint(0,1) #current odds of computer landing the trick are 50% no matter what

            if computer_land == 0: #computer missed the trick, give it a letter #TODO: make sure the computer gets 2 tries on the last trick
                if len(computer_letters) == 0:
                    computer_letters.append("S.") #TODO: could get rid of the first 4 nested ifs using len(computer_letters) as in index for a char list with S.K.A.T.E.
                    print("The computer got an S!")

                elif len(computer_letters) == 1:
                    computer_letters.append("K.")
                    print("The computer got a K!")

                elif len(computer_letters) == 2:
                    computer_letters.append("A.")
                    print("The computer got a A!")

                elif len(computer_letters) == 3:
                    computer_letters.append("T.")
                    print("The computer got a T!")

                elif len(computer_letters) == 4: #computer gets 2 tries for last letter
                    print("The computer is on its last letter, giving it a second try!")
                    time.sleep(2)
                    computer_land = randint(0,1)

                    if computer_land == 0: #computer missed the last trick, game is over
                        print("The computer missed the last trick! You win!")
                        turn = False

                    else: #computer landed the last trick
                        print("The computer landed it! The game continues!")

            else: #computer landed the trick
                print("The computer landed the trick and didn't get a letter!")

        else: #player didn't land the trick, turn over
            print("You didn't land the trick!")
            turn = False
    return computer_letters, player_letters

def computer_turn(trick_list, trick_dict, computer_letters, player_letters):                   #TODO: return stuff! (like a Boolean value on whether the game is over)
    print("\n*** Computer's turn ***")

    turn == True #determines whether or not it's still the computer's turn

    while turn == True: #do these things while it's still the computer's turn
        computer_index = randint(0,139) #this could be simplified into the next step
        computer_trick = trick_list[computer_index]

        print("\nThe computer tries a", computer_trick)

        odds = randint(0,1) #current odds of landing the trick are 50%

        if odds == 0:
            print("The computer missed the trick!")
            turn = False #turn is over

        else:
            print("The computer landed the trick!") 
            print("Your turn!")                 
            landed = input("Did you land it?:\n\t1. Yes\n\t2. No")

            if landed == "1":
                print("Good job! You didn't get a letter.")

            else: #decides what letter to give you based on how many you have
                if len(player_letters) == 0:
                    player_letters.append("S.")
                    print("You got an 'S'!")

                elif len(player_letters) == 1:
                    player_letters.append("K.")
                    print("You got a 'K'!")

                elif len(player_letters) == 2:
                    player_letters.append("A.")
                    print("You got an 'A'!")

                elif len(player_letters) == 3:
                    player_letters.append("T.")
                    print("You got a 'T'! Be careful!")

                elif len(player_letters) == 4: #2 tries for last letter
                    print("Last try!")
                    last_try = input("Did you land it?:\n\t1. Yes\n\t2. No")

                    if last_try == "1":
                        print("You're still in it!")

                    elif last_try == "2":
                        player_letters.append("E.")
                        print("You lose!")
                        turn = False #turn is over because game is over

    return computer_letters, player_letters

def main():                                                  #TODO: give letter progress for each player each turn
    print("\n*** Welcome to the game of S.K.A.T.E.! ***\n")  #TODO: make the game replayable

    letters = ["S.", "K.", "A.", "T.", "E."] #TODO: possibly pass this into player_turn() and computer_turn() for optimization
    computer_letters = [] #will be populated with letters
    player_letters = [] 
    
    terrain, difficulty = player_selections()
    trick_list, trick_dict = get_tricks(terrain, difficulty)
    player_win = roshambo()

    if player_win == True:
        computer_letters, player_letters = player_turn(trick_list, trick_dict, computer_letters, player_letters) #TODO: set variables equal to the turn() function calls
        print("\nPlayer turn is over!\n")

    else:
        computer_letters, player_letters = computer_turn(trick_list, trick_dict, computer_letters, player_letters)
        print("\nComputer turn is over!\n")

    while len(computer_letters) < 5 or len(player_letters) < 5: #while the game is still going on
        if player_win == True: #TODO: not sure if the player_win logic is correct
            computer_letters, player_letters = computer_turn(trick_list, trick_dict, computer_letters, player_letters)
            print("\nComputer turn is over!\n")
            player_win = False

        else:
            computer_letters, player_letters = player_turn(trick_list, trick_dict, computer_letters, player_letters)
            print("\nPlayer turn is over!\n")
            player_win = True

main()
