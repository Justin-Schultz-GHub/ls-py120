import random
import os
import time

def clear_screen():
    os.system('clear')
    pass

def prompt(message):
    print(f'==> {message}')

def enter_to_continue():
    input('\n(Enter to continue)')

def sleep(timer=2):
    time.sleep(timer)

def player_total_prompt():
    return f'Player hand total: '

def dealer_total_prompt():
    return f'Dealer hand total: '

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
        self._rank = rank
        self._suit = suit
        self._value = self.CARD_VALUES[rank]

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    def __str__(self):
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

    def is_blackjack(self):
        return self.score == 21 and len(self.hand) == 2

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
    HIT = 'hit'
    STAY = 'stay'

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer(self.deck)

    def start(self):
        self.display_welcome_message()
        self.deal_cards()

        if self.player.score == self.TWENTY_ONE:
            self.show_cards()
            self.display_player_score()
            enter_to_continue()
            self.display_result()
            sleep()
        else:
            while not self.player.is_busted():
                self.show_cards()
                self.display_player_score()
                player_action = self.player_turn()
                if (self.player.score == self.TWENTY_ONE
                or player_action == self.STAY
                ):
                    break

            if self.player.is_busted():
                self.display_result()
                sleep()
            else:
                clear_screen()
                self.show_cards()
                self.display_player_score()
                if not self.dealer.is_blackjack():
                    self.dealer_turn()
                else:
                    self.reveal_dealer_hidden()

        self.display_result()
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

    def player_turn(self):
        if (self.player.score == self.TWENTY_ONE
        and len(self.player.hand) == 2
        ):
            prompt(f'You were dealt {self.TWENTY_ONE}!')
            sleep()
            return None

        prompt('Hit or stay? (h/s)')
        hit_or_stay = input().strip()

        while not hit_or_stay or hit_or_stay[0].lower() not in 'hs':
            prompt('Please enter a valid input: (h/s)')
            hit_or_stay = input().strip()

        if hit_or_stay[0].lower() == 'h':
            prompt('You hit!')
            sleep()
            self.player.hit(self.deck)
            self.display_player_hit()
            sleep()
            clear_screen()

            return self.HIT
        else:
            prompt('You stay')
            sleep()

            return self.STAY

    def dealer_turn(self):
        self.reveal_dealer_hidden()

        if self.dealer.score == self.TWENTY_ONE:
            clear_screen()
            prompt(f'The dealer has {self.TWENTY_ONE}!')

        while self.dealer.score < 16:
            clear_screen()
            self.display_player_score()
            print()
            self.show_dealer_hand()
            self.display_dealer_score()

            enter_to_continue()
            prompt('The dealer hits!')
            sleep()

            self.dealer.hit(self.deck)
            clear_screen()
            prompt(f'The dealer draws a(n) {self.dealer.hand[-1]}')
            self.display_dealer_score()
            enter_to_continue()
        else:
            if not self.dealer.is_busted() and self.dealer.score != 21:
                prompt('The dealer stays')
                sleep()

    def reveal_dealer_hidden(self):
        clear_screen()
        prompt('The dealer\'s hand is:')

        for card in self.dealer.hand[1:]:
            prompt(card)

        prompt('And the face down card was:')
        sleep()
        prompt(f'the {self.dealer.hand[0]}')
        enter_to_continue()

    def show_dealer_hand(self):
        prompt('The dealer\'s hand is:')
        for card in self.dealer.hand:
            prompt(card)

    def display_welcome_message(self):
        clear_screen()
        print('Welcome to Twenty One')

    def display_goodbye_message(self):
        prompt('Thanks for playing!')

    def display_player_hit(self):
        prompt(f'You draw a(n) {self.player.hand[-1]}!')

    def display_player_score(self):
        prompt(f'{player_total_prompt()}{self.player.score}')

    def display_dealer_score(self):
        prompt(f'{dealer_total_prompt()}{self.dealer.score}')

    def display_result(self):
        if self.player.is_blackjack():
            clear_screen()
            self.display_player_score()
            prompt('You were dealt 21! You win!')

        elif self.dealer.is_blackjack():
            clear_screen()
            prompt('The dealer was dealt 21! The dealer wins')

        elif self.player.is_busted():
            clear_screen()
            self.display_player_score()
            prompt('You busted!')

        elif self.dealer.is_busted():
            clear_screen()
            prompt('The dealer busted! You win!')

        else:
            if self.player.score > self.dealer.score:
                clear_screen()
                prompt(f'{player_total_prompt()}{self.player.score}')
                prompt(f'{dealer_total_prompt()}{self.dealer.score}')
                prompt(f'You win!')

            elif self.dealer.score > self.player.score:
                clear_screen()
                prompt(f'{player_total_prompt()}{self.player.score}')
                prompt(f'{dealer_total_prompt()}{self.dealer.score}')
                prompt(f'The dealer wins!')

            else:
                clear_screen()
                prompt(f'{player_total_prompt()}{self.player.score}')
                prompt(f'{dealer_total_prompt()}{self.dealer.score}')
                prompt(f'It\'s a tie!')


game = TwentyOneGame()
game.start()