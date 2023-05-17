import random

class Player:

    def __init__(self, name, number_of_dices = 5):
        self.name = name
        self.number_of_dices = number_of_dices
        self.hand = [random.randint(1, 6) for number in range(number_of_dices)]
        self.guess = {}
    
    def __repr__(self):
        return 'This is {name} and I have {dices} dices left!'.format(name = self.name, dices = self.number_of_dices)
    
    def look_at_hand(self):
        return self.hand
    
    def make_a_guess(self, amount_of_dices, number):
        self.guess[amount_of_dices] = number
        return self.guess
    
    def lose_a_dice(self):
        self.number_of_dices -= 1
        if self.number_of_dices == 0:
            return 'You lost'
        else:
            return self.number_of_dices
        
    def call_bullshit(self):
        pass

    
    
# Création des joueurs:

print('Welcome to Perudo!')
player1_name = input('Player1, please provide your name and press enter ') 
player1 = Player(player1_name)
player2_name = input('Player2, please provide your name and press enter ')
player2 = Player(player2_name)

# Demander a player x si il veut regarder ses dés

player1_action = input('{name} it\'s your turn! Press s then enter to see your dices '.format(name = player1.name))

# if player_action != 's':
#     print('I did not understand, try again..')

if player1_action == 's':
    print(player1.look_at_hand())
    player1_guess_amount = input('Time to make a guess! Start with the amount of dices: ')
    player1_guess_number = input('Of what number: ')
    print(player1.make_a_guess(player1_guess_amount, player1_guess_number))

player2_action = input('{name} it\'s your turn! Press s then enter to see your dices '.format(name = player2.name))

if player2_action == 's':
    print(player2.look_at_hand())
    player2_choice = input('Do you want to make a guess or call bullshit? For guess press g, for bullshit press b: ')
    if player2_choice == 'g':
        player2_guess_amount = input('Time to make a guess! Start with the amount of dices: ')
        player2_guess_number = input('Of what number: ')
        print(player2.make_a_guess(player2_guess_amount, player2_guess_number))
    elif player2_choice == 'b':
        total = player1.hand + player2.hand
        for key, value in player1.guess:
            if int(key) <= total.count(value):
                player2.lose_a_dice()
                print('You\'re wrong, you lost a die') 
            else:
                player1.lose_a_dice()
                print('You\'re right! {name} lost a dice'.format(name = player1.name))

print(player1)



        # Check if the total between player 1 hand and player 2 hand is higher or equal to 
        






# print(player1.look_at_hand())
# print(player2.look_at_hand())





# print(player_1.hand)
# # print(player_2)
