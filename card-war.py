# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 16:54:19 2023

@author: sreek
"""
import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ('ace', 'two', 'three', 'four', 'five', 'six', 'seven',
         'eight', 'nine', 'ten', 'jack', 'queen', 'king')
arr = {'ace': 14, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
       'eight': 8, 'nine': 9, 'ten': 10, 'jack': 11, 'queen': 12, 'king': 13}


class card:

    def __init__(self, suit, rank):
        self.suit = suit.lower()
        self.rank = rank
        self.value = -1

    # For human player (v2 project)

    def find_value(self):
        try:
            if(int(self.rank)) % 1 == 0:
                self.value = int(self.rank)
        except ValueError:
            self.rank = self.rank.lower()
            if(self.rank == "one"):
                self.rank = "ace"
            elif(self.rank == "joker"):
                self.rank = "jack"
            try:
                self.value = arr[self.rank]
            except KeyError:
                return "Enter correct rank"

    def __str__(self):
        return f"{self.rank.capitalize()} of {self.suit.capitalize()}"


class deck:
    def __init__(self):
        self.all_cards = []
        for i in suits:
            for j in ranks:
                self.all_cards.append(card(i, j))
        # print(len(self.all_cards))
        for i in self.all_cards:
            i.find_value()

    def shuffle(self):
        random.shuffle(self.all_cards)

    def take_out_one_card(self):
        return self.all_cards.pop()

    def __str__(self):
        return f"Deck currently has {len(self.all_cards)} cards"


class player:
    def __init__(self, name):
        self.name = name
        self.player_cards = []

    def add_cards(self, n):
        if type(n) == type([]):
            self.player_cards += n
        else:
            self.player_cards.append(n)

    def remove_card(self):
        return self.player_cards.pop(0)

    def __str__(self):
        return (f"Player {self.name} has {len(self.player_cards)} card(s)")


"""
# For human player (v2 project)
def new_card():
    while True:
        suit = input("Enter suit: ").split()
        if(len(suit) == 0) or (len(suit) > 1):
            print("Enter suit correctly")
            continue
        else:
            suit = suit[0]
            try:
                suit = int(suit)
            except ValueError:
                suit = suit.lower()
                break
            else:
                print("Enter suit correctly")
                continue

    while True:
        rank = input("Enter rank: ").split()
        if(len(rank) == 0) or (len(rank) > 1):
            print("Enter rank correctly")
            continue
        else:
            rank = rank[0]
            break

    return card(suit, rank)


x = new_card()
x.find_value()
print(x)"""

war_card_count = 3
# Players creation
p1_name = input(">> What's your name, Player 1? ").split()
while(len(p1_name) != 1):
    print("Enter your name! Don't worry I won't store it")
    p1_name = input(">> What's your name, Player 1? ").split()
p1 = player(p1_name[0])
p2_name = input(">> What's your name, Player 2? ").split()
while(len(p2_name) != 1):
    print("Enter your name! Don't worry I won't store it")
    p2_name = input(">> What's your name, Player 2? ").split()
p2 = player(p2_name[0])

deck1 = deck()
deck1.shuffle()

# add cards
# p1.add_cards(deck1.all_cards[:(len(deck1.all_cards)//2)])
# p1.add_cards(deck1.all_cards[(len(deck1.all_cards)//2):])

for i in range(0, 26, 1):
    p1.add_cards(deck1.take_out_one_card())
    p2.add_cards(deck1.take_out_one_card())

# game
ctr = 0
war_ctr = 0
game_flag = True
while game_flag:
    ctr += 1
    if(len(p1.player_cards) < 1):
        print(f"{p1.name} is out of cards. {p2.name} wins!")
        game_flag = False
        break
    if(len(p2.player_cards) < 1):
        print(f"{p2.name} is out of cards. {p1.name} wins!")
        game_flag = False
        break
    # for comparision
    p1_cards = []
    p2_cards = []
    p1_cards.append(p1.remove_card())
    p2_cards.append(p2.remove_card())

    # war
    while True:
        print(
            f"Round {ctr}: {p1.name}'s '{p1_cards[-1]}' vs {p2.name}'s '{p2_cards[-1]}'")
        if(p1_cards[-1].value > p2_cards[-1].value):
            p1.add_cards(p1_cards+p2_cards)
            break
        elif(p1_cards[-1].value < p2_cards[-1].value):
            p2.add_cards(p1_cards+p2_cards)
            break
        else:
            # both are equal
            war_ctr += 1
            print(f">> WAR!! (count: {war_ctr})")
            if(len(p1.player_cards) < war_card_count):
                print(
                    f"{p1.name} doesn't have enough cards for war. {p2.name} wins!")
                game_flag = False
                break
            elif(len(p2.player_cards) < war_card_count):
                print(
                    f"{p2.name} doesn't have enough cards for war. {p1.name} wins!")
                game_flag = False
                break
            else:
                for i in range(0, war_card_count, 1):
                    if(len(p1.player_cards) > 0):
                        p1_cards.append(p1.remove_card())
                    else:
                        print(f"{p1.name} is out of cards. {p2.name} wins!")
                        game_flag = False
                        break
                    if(len(p2.player_cards) > 0):
                        p2_cards.append(p2.remove_card())
                    else:
                        print(f"{p2.name} is out of cards. {p1.name} wins!")
                        game_flag = False
                        break
print("End of game!")
