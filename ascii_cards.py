#!/usr/bin/env python3
'''

ascii_cards.py


'''


import random


class Cards():
    '''Ascii card deck'''

    def __init__(self):
        '''Initialize the card deck.'''
        self.card_values = {
                'hearts': [(2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8,
                           8), (9, 9), (10, 10), ('J', 10), ('K', 10), ('Q',
                           10), ('A', 11)],
                'diamonds': [(2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                             (8, 8), (9, 9), (10, 10), ('J', 10), ('K', 10),
                             ('Q', 10), ('A', 11)],
                'clubs': [(2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8,
                          8), (9, 9), (10, 10), ('J', 10), ('K', 10), ('Q',
                          10), ('A', 11)],
                'spades': [(2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8,
                           8), (9, 9), (10, 10), ('J', 10), ('K', 10), ('Q',
                           10), ('A', 11)]
                }

    def select_random_card(self):
        '''Select a card randomly from deck.'''
        self.suit = random.choice(list(self.card_values.keys()))
        self.rank, self.value = random.choice(self.card_values[self.suit])
        del self.card_values[self.suit][self.card_values[self.suit].index((
            self.rank, self.value))]
        return self.suit, self.rank, self.value

    def display_card(self, suit, rank, value, dealer=False):
        '''Display a card to the players.'''
        self.suit = suit
        self.rank = rank
        self.value = value
        # Set the correct icon for the card.
        if self.suit == 'hearts':
            suit_icon = '♥'
        elif self.suit == 'clubs':
            suit_icon = '♣'
        elif self.suit == 'diamonds':
            suit_icon = '♦'
        else:
            suit_icon = '♠'

        self.face_down = """\
        ╔═════════╗
        ║░▓░▓░▓░▓░║
        ║▓░▓░▓░▓░▓║
        ║▒▓░▓▒▓░▓▒║
        ║▓░▓▒░▒▓░▓║
        ║▒▓░▓▒▓░▓▒║
        ║▓░▓░▓░▓░▓║
        ║░▓░▓░▓░▓░║
        ╚═════════╝
        """
        self.ace = """\
        ╔═════════╗
        ║ {}       ║
        ║         ║
        ║         ║
        ║    {}    ║
        ║         ║
        ║         ║
        ║       {} ║
        ╚═════════╝
        """.format('A', suit_icon, 'A')
        self.two = """\
        ╔═════════╗
        ║ {}       ║
        ║         ║
        ║         ║
        ║         ║
        ║         ║
        ║         ║
        ║       {} ║
        ╚═════════╝
        """.format(suit_icon, suit_icon)
        self.three = """\
        ╔═════════╗
        ║ {}       ║
        ║         ║
        ║         ║
        ║    {}    ║
        ║         ║
        ║         ║
        ║       {} ║
        ╚═════════╝
        """.format(suit_icon, suit_icon, suit_icon)
        self.four = """\
        ╔═════════╗
        ║ {}     {} ║
        ║         ║
        ║         ║
        ║         ║
        ║         ║
        ║         ║
        ║ {}     {} ║
        ╚═════════╝
        """.format(suit_icon, suit_icon, suit_icon, suit_icon)
        self.five = """\
        ╔═════════╗
        ║ {}     {} ║
        ║         ║
        ║         ║
        ║    {}    ║
        ║         ║
        ║         ║
        ║ {}     {} ║
        ╚═════════╝
        """.format(suit_icon, suit_icon, suit_icon, suit_icon, suit_icon)
        self.six = """\
        ╔═════════╗
        ║ {}     {} ║
        ║         ║
        ║         ║
        ║ {}     {} ║
        ║         ║
        ║         ║
        ║ {}     {} ║
        ╚═════════╝
        """.format(suit_icon, suit_icon, suit_icon, suit_icon, suit_icon,
                   suit_icon)
        self.seven = """\
        ╔═════════╗
        ║         ║
        ║    {}    ║
        ║ {}     {} ║
        ║    {}    ║
        ║ {}     {} ║
        ║    {}    ║
        ║         ║
        ╚═════════╝
        """.format(suit_icon, suit_icon, suit_icon, suit_icon, suit_icon,
                   suit_icon, suit_icon)
        self.eight = """\
        ╔═════════╗
        ║ {}     {} ║
        ║    {}    ║
        ║         ║
        ║ {}     {} ║
        ║         ║
        ║    {}    ║
        ║ {}     {} ║
        ╚═════════╝
        """.format(suit_icon, suit_icon, suit_icon, suit_icon, suit_icon,
                   suit_icon, suit_icon, suit_icon)
        self.nine = """\
        ╔═════════╗
        ║ {}     {} ║
        ║         ║
        ║ {}     {} ║
        ║    {}    ║
        ║ {}     {} ║
        ║         ║
        ║ {}     {} ║
        ╚═════════╝
        """.format(suit_icon, suit_icon, suit_icon, suit_icon, suit_icon,
                   suit_icon, suit_icon, suit_icon, suit_icon)
        self.ten = """\
        ╔═════════╗
        ║ {}     {} ║
        ║    {}    ║
        ║ {}     {} ║
        ║         ║
        ║ {}     {} ║
        ║    {}    ║
        ║ {}     {} ║
        ╚═════════╝
        """.format(suit_icon, suit_icon, suit_icon, suit_icon, suit_icon,
                   suit_icon, suit_icon, suit_icon, suit_icon, suit_icon)
        self.jack = """\
        ╔═════════╗
        ║ {}       ║
        ║ {}       ║
        ║         ║
        ║         ║
        ║         ║
        ║       {} ║
        ║       {} ║
        ╚═════════╝
        """.format('J', suit_icon, 'J', suit_icon)
        self.queen = """\
        ╔═════════╗
        ║ {}       ║
        ║ {}       ║
        ║         ║
        ║         ║
        ║         ║
        ║       {} ║
        ║       {} ║
        ╚═════════╝
        """.format('Q', suit_icon, suit_icon, 'Q')
        self.king = """\
        ╔═════════╗
        ║ {}       ║
        ║ {}       ║
        ║         ║
        ║         ║
        ║         ║
        ║       {} ║
        ║       {} ║
        ╚═════════╝
        """.format('K', suit_icon, suit_icon, 'K')

        if dealer:
            return self.face_down

        if self.rank == 2:
            return self.two
        elif self.rank == 3:
            return self.three
        elif self.rank == 4:
            return self.four
        elif self.rank == 5:
            return self.five
        elif self.rank == 6:
            return self.six
        elif self.rank == 7:
            return self.seven
        elif self.rank == 8:
            return self.eight
        elif self.rank == 9:
            return self.nine
        elif self.rank == 10:
            return self.ten
        elif self.rank == 'J':
            return self.jack
        elif self.rank == 'Q':
            return self.queen
        elif self.rank == 'K':
            return self.king
        else:
            return self.ace
