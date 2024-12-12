import random
import os
import time

def clear_screen():
    os.system('clear')

def prompt(message):
    print(f'==> {message}')

def enter_to_continue():
    input('\n(Enter to continue)')

def sleep(timer=2):
    time.sleep(timer)

class Card:
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10,
            'Jack', 'Queen', 'King', 'Ace'
            )
    CARD_VALUES = {
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11,
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.CARD_VALUES[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def __repr__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit)
                    for suit in Card.SUITS
                    for rank in Card.RANKS
                    ]
        random.shuffle(self.cards)

    def __repr__(self):
        return self.cards


class Participant:
    def __init__(self):
        self.hand = []
        self.score = 0

    def hit(self, deck):
        self.hand.append(deck.cards.pop())
        self.update_score(self.hand)

    def is_busted(self):
        return self.score > 21

    def update_score(self, hand):
        ace_counter = 0
        hand_total = 0

        for card in hand:
            if card.rank == 'Ace':
                ace_counter += 1
            else:
                hand_total += card.value

        for _ in range(ace_counter):
            if hand_total + Card.CARD_VALUES['Ace'] <= 21:
                hand_total += Card.CARD_VALUES['Ace']
            else:
                hand_total += 1

        self.score = hand_total

class Player(Participant):
    def __init__(self):
        super().__init__()


class Dealer(Participant):
    def __init__(self, deck):
        self.deck = deck
        super().__init__()

    def deal(self, player):
        for _ in range(2):
            player.hand.append(self.deck.cards.pop())
            self.hand.append(self.deck.cards.pop())

        player.update_score(player.hand)
        self.update_score(self.hand)


class TwentyOneGame:
    TWENTY_ONE = 21

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer(self.deck)
        pass

    def start(self):
        self.display_welcome_message()
        self.deal_cards()

        if self.player.score == self.TWENTY_ONE:
            self.show_cards()
            enter_to_continue()
            self.display_result()
            sleep()
        else:
            while not self.player.is_busted():
                self.show_cards()
                if (self.player.score == self.TWENTY_ONE
                or not self.player_turn()
                ):
                    break

                if self.player.is_busted():
                    self.display_result()
                    sleep()
                else:
                    self.dealer_turn()

        self.display_goodbye_message()

    def deal_cards(self):
        self.dealer.deal(self.player)

    def show_cards(self):
        prompt('The dealer\'s hand is: ')
        for card in self.dealer.hand[1:]:
            prompt(card)
        prompt('And one face down card')
        print()

        prompt('Your hand is: ')
        for card in self.player.hand:
            prompt(card)

        self.display_player_score()

    def player_turn(self):
        if (self.player.score == self.TWENTY_ONE
        and len(self.player.hand) == 2
        ):
            prompt(f'You were dealt {self.TWENTY_ONE}!')
            sleep()
            return None

        prompt('Hit or stay? (h/s)')
        hit_or_stay = input().strip()

        while hit_or_stay[0].lower() not in 'hs':
            prompt('Please enter a valid input: (h/s)')
            hit_or_stay = input().strip()

        if hit_or_stay[0].lower() == 'h':
            prompt('You hit!')
            sleep()
            self.player.hit(self.deck)
            self.display_player_hit()
            sleep()
            clear_screen()

            return hit_or_stay == 'h'
        else:
            prompt('You stay')
            sleep()

            return hit_or_stay == 'h'

    def dealer_turn(self):
        clear_screen()
        prompt('The dealer\'s hand is:')

        for card in self.dealer.hand[1:]:
            prompt(card)

        prompt('And the face down card was:')
        sleep()
        prompt(f'the {self.dealer.hand[0]}')
        sleep()

        if self.dealer.score == self.TWENTY_ONE:
            clear_screen()
            prompt(f'The dealer has {self.TWENTY_ONE}!')

        while self.dealer.score < 16:
            clear_screen()
            self.display_player_score()
            print()
            prompt('The dealer\'s hand is:')
            for card in self.dealer.hand:
                prompt(card)
            prompt(f'Dealer hand total: {self.dealer.score}')

            enter_to_continue()
            prompt('The dealer hits!')
            sleep()

            self.dealer.hit(self.deck)
            clear_screen()
            prompt(f'The dealer draws a(n) {self.dealer.hand[-1]}')
            prompt(f'Dealer hand total: {self.dealer.score}')
            enter_to_continue()
        else:
            prompt('The dealer stays')
            sleep()

    def display_welcome_message(self):
        clear_screen()
        print('Welcome to Twenty One')

    def display_goodbye_message(self):
        clear_screen()
        prompt('Thanks for playing!')

    def display_player_hit(self):
        prompt(f'You draw a(n) {self.player.hand[-1]}!')

    def display_player_score(self):
        prompt(f'Player hand total is: {self.player.score}')

    def display_result(self):
        if self.player.score > self.TWENTY_ONE:
            clear_screen()
            self.display_player_score()
            prompt('You busted!')

        if self.TWENTY_ONE >= self.player.score > self.dealer.score:
            clear_screen()
            prompt(f'Player hand total: {self.player.score}')
            prompt(f'Dealer hand total: {self.dealer.score}')
            prompt(f'You win!')

        if self.TWENTY_ONE >= self.dealer.score > self.player.score:
            clear_screen()
            prompt(f'Player hand total: {self.player.score}')
            prompt(f'Dealer hand total: {self.dealer.score}')
            prompt(f'The dealer wins!')

        if self.player.score == self.dealer.score:
            clear_screen()
            prompt(f'Player hand total: {self.player.score}')
            prompt(f'Dealer hand total: {self.dealer.score}')
            prompt(f'It\'s a tie!')


game = TwentyOneGame()
game.start()