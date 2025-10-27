import random
from typing import Union


class Card:
    def __init__(self, color: str, value: int):
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.color} - {self.value}"


class Deck:
    def __init__(self, cards: list[Card]):
        self.cards = cards

    def get_cards_quantity(self):
        return len(self.cards)

    def get_card(self, index: int):
        return self.cards[index]

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, index: int):
        card = self.cards.pop(index)
        return card

    def __str__(self):
        deck_str = ''

        for i in range(len(self.cards)):
            deck_str += f"{i + 1}. {self.cards[i]}\n"

        return deck_str


class Rebound:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)


class Player:
    def __init__(self, name: str, deck: Deck):
        self.name = name
        self.deck = deck

    def make_step(self, active_card: Union[Card, None], card_index: int):
        if active_card is None:
            return self.deck.remove_card(card_index)
        else:
            card = self.deck.get_card(card_index)

            if card.color == active_card.color and card.value > active_card.value:
                return self.deck.remove_card(card_index)
            else:
                return None



class Round:
    def __init__(self):
        self.steps = []

    def get_steps_quantity(self):
        return len(self.steps)

    def check_if_second_player_made_step(self):
        return len(self.steps[-1]) == 2

    def __first_player_step__(self, player):
        if len(self.steps) == 0:
            self.add_first_card(player)
            return True
        else:
            choice = input("\nХотите сделать еще 1 ход в этом раунде? (Y/n): ")

            if choice == '' or choice == 'Y':
                self.add_first_card(player)
                return True
            else:
                return False

    def __second_player_step__(self, player):
        current_step = self.steps[-1]
        print(f"\nПротивник сделал ход: {current_step[0]}")
        choice = input("Будете отбиваться? (Y/n): ")
        print()

        if choice == '' or choice == 'Y':
            self.add_second_card(player)
            return True
        else:
            self.get_all_round_cards(player)
            return False

    def ask_to_make_step(self, player: Player):
        if len(self.steps) == 0:
            print('\nНовый раунд')

        print(f"\nХод игрока {player.name}")
        print(f"\n{player.deck}")

        if len(self.steps) == 0 or len(self.steps[-1]) == 2:
            return self.__first_player_step__(player)
        else:
            return self.__second_player_step__(player)

    def get_all_round_cards(self, player):
        for step in self.steps:
            for step_card in step:
                player.deck.add_card(step_card)

    def add_first_card(self, player: Player):
        card_number = int(input("\nВведите номер карты для хода: "))
        card_index = max(0, card_number - 1)
        card = player.make_step(None, card_index)
        self.steps.append([card])

    def add_second_card(self, player: Player):
        current_step = self.steps[-1]
        card_number = int(input("\nВведите номер карты для хода: "))
        card_index = max(0, card_number - 1)
        card = player.make_step(current_step[0], card_index)

        if card:
            self.steps[-1].append(card)
        else:
            self.get_all_round_cards(player)


def generate_deck():
    cards = []
    card_colors = ['blue', 'green', 'yellow', 'red']

    for color in card_colors:
        for i in range(9):
            cards.append(Card(color, i + 1))

    random.shuffle(cards)

    return Deck(cards)


def initiate_player_deck(main_deck: Deck):
    deck = Deck([])

    for i in range(6):
        card = main_deck.remove_card(0)
        deck.add_card(card)

    return deck


class Game:
    def __init__(self, player_names):
        self.rounds = []
        self.deck = generate_deck()
        self.players = [Player(name, initiate_player_deck(self.deck)) for name in player_names]
        self.rebound = Rebound()

    def get_cards_to_start_new_round(self):
        for player in self.players:
            need_cards_quantity = 6 - player.deck.get_cards_quantity()
            if need_cards_quantity > 0:
                for i in range(need_cards_quantity):
                    if self.deck.get_cards_quantity():
                        new_card = self.deck.remove_card(-1)
                        player.deck.add_card(new_card)

    def update_players_queue(self):
        first_player = self.players.pop(0)
        self.players.append(first_player)

    def start_round(self, end_round: list[bool]):
        while self.rounds[-1].get_steps_quantity() < 6 and not end_round[0]:
            for player in self.players:
                made_step = self.rounds[-1].ask_to_make_step(player)

                if not made_step:
                    end_round[0] = True
        else:
            self.get_cards_to_start_new_round()

    def start(self):
        while True:
            end_round = [False]
            self.rounds.append(Round())

            self.start_round(end_round)

            if not end_round[0]:
                self.update_players_queue()


game = Game(['Kenny', 'John'])
game.start()
