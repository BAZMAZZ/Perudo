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
        self.guess = {}
        self.guess[amount_of_dices] = number
        return self.guess

    def lose_a_dice(self):
        self.number_of_dices -= 1
        if self.number_of_dices == 0:
            return 'You lost'
        else:
            return self.number_of_dices

    def add_a_dice(self):
        self.number_of_dices += 1

    def call_bullshit(self):
        pass


    def reset(self):
        self.hand = [random.randint(1, 6) for number in range(self.number_of_dices)]
        self.guess = {}




# Création des joueurs:


print('Welcome to Perudo!')
player1_name = input('Player1, please provide your name and press enter ')
player1 = Player(player1_name)
player2_name = input('Player2, please provide your name and press enter ')
player2 = Player(player2_name)

# Demander a player x si il veut regarder ses dés


while player1.number_of_dices > 0 and player2.number_of_dices > 0:
    player1_action = input('{name} it\'s your turn! Press s then enter to see your dices '.format(name = player1.name))

# if player_action != 's':
#     print('I did not understand, try again..')

    if player1_action == 's':
        print(player1.look_at_hand())
        player1_choice = input('Do you want to make a guess, call bullshit, or exacto? For guess press g, for bullshit press b, for exacto press e: ')
        if player1_choice == 'g':
            player1_guess_amount = input('Time to make a guess! Start with the amount of dices: ')
            player1_guess_number = input('Of what number: ')
            print(player1.make_a_guess(player1_guess_amount, player1_guess_number))
        elif player1_choice == 'b':
            total = player1.hand + player2.hand

            if int(list(player1.guess.keys())[0]) <= total.count(int(player1.guess[player1_guess_amount])):
                player1.lose_a_dice()
                print('You\'re wrong, you lost a die')
                player2.reset()
                player1.reset()
            else:
                player2.lose_a_dice()
                print('You\'re right! {name} lost a dice'.format(name = player1.name))
                player2.reset()
                player1.reset()
        elif player1_choice == 'e':
            total = player1.hand + player2.hand
            if int(list(player2.guess.keys())[0]) == total.count(int(player2.guess[player2_guess_amount])):
                player1.add_a_dice()
                print('Congrats, you are right! You get a dice back!')
                player2.reset()
                player1.reset()
            else:
                player1.lose_a_dice()
                print('You\'re wrong, you lost a die')
                player2.reset()
                player1.reset()





    player2_action = input('{name} it\'s your turn! Press s then enter to see your dices '.format(name = player2.name))
    if player2_action == 's':
        print(player2.look_at_hand())
        player2_choice = input('Do you want to make a guess, call bullshit or exacto? For guess press g, for bullshit press b, for exacto press e ')
        if player2_choice == 'g':
            player2_guess_amount = input('Time to make a guess! Start with the amount of dices: ')
            player2_guess_number = input('Of what number: ')
            print(player2.make_a_guess(player2_guess_amount, player2_guess_number))
        elif player2_choice == 'b':
            total = player1.hand + player2.hand

            if int(list(player1.guess.keys())[0]) <= total.count(int(player1.guess[player1_guess_amount])):
                player2.lose_a_dice()
                print('You\'re wrong, you lost a die')
                player2.reset()
                player1.reset()
            else:
                player1.lose_a_dice()
                print('You\'re right! {name} lost a dice'.format(name = player1.name))
                player2.reset()
                player1.reset()
        elif player2_choice == 'e':
            total = player1.hand + player2.hand
            if int(list(player1.guess.keys())[0]) == total.count(int(player1.guess[player1_guess_amount])):
                player2.add_a_dice()
                print('Congrats, you are right! You get a dice back!')
                player2.reset()
                player1.reset()
            else:
                player2.lose_a_dice()
                print('You\'re wrong, you lost a die')
                player2.reset()
                player1.reset()


if player1.number_of_dices == 0:
    print('{name} has won the game'.format(name = player2.name))
else:
    print('{name} has won the game'.format(name = player1.name))