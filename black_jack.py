#!/usr/bin/env python3
'''

black_jack.py

'''

import os
import sys
import time
from ascii_cards import Cards


os.system('clear')


def main():
    '''Start the game'''

    play = True
    return play


def print_slow(text, delay=0.5):
    '''Print text in the terminal with a delay.'''

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(" ")


def display_hidden_card():
    '''Print the hidden card of the dealer.'''

    print("Dealer's hidden card is {} of {}.".format(hidden_rank,
          hidden_suit))
    print(player_hand.display_card(hidden_suit, hidden_rank,
          hidden_value))


class Hand(Cards):
    '''Start each player with a hand of cards.'''

    def __init__(self):

        self.player_total = []
        self.dealer_total = []
        self.value = 0
        self.aces = 0

    def add_card(self, value):
        '''Add a card to the hand of the player.'''

        self.player_total.append(value)
        self.dealer_total.append(value)
        if self.value == 11:
            self.aces += 1

    def adjust_for_ace(self, hand_total):
        '''Change the value of the Ace to 1 if necessary.'''

        while hand_total > 21 and self.ace:
            if self.value == 11:
                self.aces -= 1


class Chips():

    def __init__(self):

        self.total = 1000
        self.bet = 0

    def win_bet(self, message, total):
        '''Display message that player won.'''

        print_slow(message, 0.1)
        self.total += self.bet

    def lose_bet(self, message, total):
        '''Display message that player lost.'''

        print_slow(message, 0.1)
        self.total -= self.bet

    def push(self, message):
        '''Display message that players tied.'''

        print_slow(message, 0.1)

    def display_chips(self):
        '''Show amount of chips player holds.'''

        print(f'Player has {self.total} dollars.')


def take_bet(chips):
    '''Allow player to make a bet'''

    while True:
        try:
            chips.bet = int(input("Enter amount to bet (maximum $1000)? "))
        except ValueError as e:
            print(e)
        else:
            if chips.bet > chips.total:
                print("Your bet cannot exceed the number of chips you have.")
                print(f'Current amount: {chips.total}')
            else:
                break


def menu():
    '''Display hit or stay menu.'''

    global answer
    menu_list = ['Hit', 'Stay']
    for count, item in enumerate(menu_list, 1):
        print(f'{count}. {item}')
    answer = input("Select an number 1-2: ")
    return answer


def print_divider(count):

    print(f'{"="*count}')


def show_cards(dealer_total, player_total):
    '''Show cards once last player has hit.'''

    print_divider(25)
    print('Dealer\'s cards: ')
    for count, value in enumerate(dealer_hand.dealer_total, 1):
        print(f'Card {count}: {value}')
    print(f'Dealer total: {sum(dealer_hand.dealer_total)}')
    print_divider(25)
    print('Player\'s cards: ')
    for count, value in enumerate(player_hand.player_total, 1):
        print(f'Card {count}: {value}')
    print(f'Player total: {sum(player_hand.player_total)}')
    print_divider(25)


title = '''
     ___ _     _   __  _  _    _   _   __  _  _
    | o ) |   / \ / _|| |//   | | / \ / _|| |// \\
    | o \ |_ | o ( (_ |  (  n_| || o ( (_ |  ( \\
    |___/___||_n_|\__||_|\\\ \__/ |_n_|\__||_|\\\\

'''

print_slow(title, 0.009)

play = input('Would you like to play Blackjack? ').lower().startswith('y')
if play is False:
    print('BYE!')
    sys.exit()


while True:

    deck = Cards()

    dealer_hand = Hand()
    player_hand = Hand()

    player_chips = Chips()
    take_bet(player_chips)

    os.system('clear')

    print('DEALER\'S CARDS: ')
    suit, rank, value = deck.select_random_card()
    dealer_hand.add_card(value)
    print(dealer_hand.display_card(suit, rank, value, hidden=True))
    hidden_suit, hidden_rank, hidden_value = (suit, rank, value)
    suit, rank, value = deck.select_random_card()
    dealer_hand.add_card(value)
    print(dealer_hand.display_card(suit, rank, value))
    time.sleep(1.9)
    print("PLAYER'S CARDS: ")
    suit, rank, value = deck.select_random_card()
    player_hand.add_card(value)
    print(player_hand.display_card(suit, rank, value))
    suit, rank, value = deck.select_random_card()
    player_hand.add_card(value)
    print(player_hand.display_card(suit, rank, value))

    while play:
        menu()
        if int(answer) == 1:
            print("Player hits...")
            suit, rank, value = deck.select_random_card()
            if rank == 'A' and sum(player_hand.player_total) > 21:
                value = 1
            player_hand.add_card(value)
            # player_hand.adjust_for_ace(value)
            print(player_hand.display_card(suit, rank, value))
            if sum(player_hand.player_total) > 21:
                show_cards(dealer_hand.dealer_total,
                           player_hand.player_total)
                display_hidden_card()
                player_chips.lose_bet("PLAYER LOSES!", player_chips.bet)
                player_chips.display_chips()
                break
            continue
        elif int(answer) == 2:
            if sum(player_hand.player_total) <= 21:
                while sum(dealer_hand.dealer_total) < 17:
                    print("Dealer hits...")
                    suit, rank, value = deck.select_random_card()
                    if rank == 'A' and sum(player_hand.player_total) > 21:
                        value = 1
                    dealer_hand.add_card(value)
                    # dealer_hand.adjust_for_ace(value)
                    print(player_hand.display_card(suit, rank, value))
                show_cards(dealer_hand.dealer_total, player_hand.player_total)

        if sum(dealer_hand.dealer_total) > 21:
            display_hidden_card()
            player_chips.win_bet("DEALER LOSES!", player_chips.bet)
            player_chips.display_chips()
            break
        elif sum(dealer_hand.dealer_total) > sum(player_hand.player_total):
            player_chips.lose_bet("PLAYER LOSES!", player_chips.bet)
            player_chips.display_chips()
            break
        elif sum(dealer_hand.dealer_total) < sum(player_hand.player_total):
            display_hidden_card()
            player_chips.win_bet("PLAYER WINS!", player_chips.bet)
            player_chips.display_chips()
            break
        else:
            display_hidden_card()
            player_chips.push("DEALER AND PLAYER ARE TIED.")
            break

    play_again = input("Would you like to play again? ")

    if play_again.lower().startswith('y'):
        play = True
        main()
    else:
        print("BYE.")
        break


if __name__ == '__main__':
    main()
