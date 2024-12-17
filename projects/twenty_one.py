import random
import os
import time

def clear_screen():
    os.system('clear')

def prompt(message):
    print(f'==> {message}')

def enter_to_continue():
    input('\n(Enter to continue)')

def sleep(timer=1):
    time.sleep(timer)

def player_total_prompt():
    return 'Player hand total: '

def dealer_total_prompt():
    return 'Dealer hand total: '

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
        self.cards = self.generate_deck()
        random.shuffle(self.cards)

    @staticmethod
    def generate_deck():
        return [Card(rank, suit)
                    for suit in Card.SUITS
                    for rank in Card.RANKS
                    ]

    def deal(self, player, dealer):
        for _ in range(2):
            player.hand.append(self.cards.pop())
            dealer.hand.append(self.cards.pop())

        player.update_score(player.hand)
        dealer.update_score(dealer.hand)

    def shuffle_deck(self):
        self.cards = self.generate_deck()
        random.shuffle(self.cards)

    def is_low(self):
        return len(self.cards) < 20

    def __repr__(self):
        return f"Deck({[str(card) for card in self.cards]})"


class Participant:
    def __init__(self):
        self.hand = []
        self.score = 0

    def hit(self, deck):
        self.hand.append(deck.cards.pop())
        self.update_score(self.hand)

    def is_busted(self):
        return self.score > TwentyOneGame.TWENTY_ONE

    def is_blackjack(self):
        return self.score == TwentyOneGame.TWENTY_ONE and len(self.hand) == 2

    def update_score(self, hand):
        ace_counter = 0
        hand_total = 0

        for card in hand:
            if card.rank == 'Ace':
                ace_counter += 1
                hand_total += Card.CARD_VALUES['Ace']
            else:
                hand_total += card.value

        for _ in range(ace_counter):
            if hand_total > TwentyOneGame.TWENTY_ONE:
                hand_total -= 10

        self.score = hand_total


class Player(Participant):
    def __init__(self):
        super().__init__()
        self.money = 5


class Dealer(Participant):
    def __init__(self):
        super().__init__()


class TwentyOneGame:
    TWENTY_ONE = 21
    DEALER_STAY_VALUE = 17
    HIT = 'hit'
    STAY = 'stay'

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def start(self):
        self.display_welcome_message()
        sleep()

        while True:
            clear_screen()

            if self.player.money < 1:
                self.display_money()
                self.comment_on_wealth()
                break
            elif self.player.money < 10:
                self.deal_cards()
                self.display_money()
                self.play_round()
                if self.play_again():
                    self.reset_game()
                else:
                    break
            else:
                self.display_money()
                self.comment_on_wealth()
                break

        self.display_goodbye_message()

    def play_round(self):
        if self.handle_initial_blackjack():
            return

        self.handle_player_turn()

        if not self.player.is_busted():
            self.handle_dealer_turn()

        result = self.handle_result()
        self.display_result(result)

    def handle_initial_blackjack(self):
        if self.player.is_blackjack():
            self.show_cards()
            self.display_player_score()
            enter_to_continue()
            result = self.handle_result()
            self.display_result(result)
            sleep()
            return True
        return False

    def handle_player_turn(self):
        while not self.player.is_busted():
            self.show_cards()
            self.display_player_score()
            action = self.player_turn()
            if action == self.STAY:
                break

    def handle_dealer_turn(self):
        clear_screen()
        self.show_cards()
        self.display_player_score()
        if not self.dealer.is_blackjack():
            self.dealer_turn()
        else:
            self.reveal_dealer_hidden()

    def deal_cards(self):
        if self.deck.is_low():
            self.deck.shuffle_deck()
            prompt('Shuffling deck.')
            sleep()
            clear_screen()
            prompt('Shuffling deck..')
            sleep()
            clear_screen()
            prompt('Shuffling deck...')
            sleep()
        self.deck.deal(self.player, self.dealer)
        clear_screen()

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
            sleep(2)
            return self.STAY

        if self.player.score == self.TWENTY_ONE:
            prompt(f'You have {self.TWENTY_ONE}!')
            sleep(2)
            return self.STAY

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

        prompt('You stay')
        sleep()

        return self.STAY

    def dealer_turn(self):
        self.reveal_dealer_hidden()

        if self.dealer.score == self.TWENTY_ONE:
            clear_screen()
            prompt(f'The dealer has {self.TWENTY_ONE}!')

        while self.dealer.score < self.DEALER_STAY_VALUE:
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

        if not self.dealer.is_busted() and self.dealer.score != self.TWENTY_ONE:
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
        clear_screen()
        prompt('Thanks for playing!')

    def display_player_hit(self):
        prompt(f'You draw a(n) {self.player.hand[-1]}!')

    def display_player_score(self):
        prompt(f'{player_total_prompt()}{self.player.score}')

    def display_dealer_score(self):
        prompt(f'{dealer_total_prompt()}{self.dealer.score}')

    def display_money(self):
        prompt(f'Remaining cash: ${self.player.money}')
        print()

    def add_money(self):
        self.player.money += 1

    def subtract_money(self):
        self.player.money -= 1

    def handle_result(self):
        result = None

        if self.player.is_blackjack():
            self.add_money()
            result = 'blackjack'
        elif self.dealer.is_blackjack():
            self.subtract_money()
            result = 'dealer_blackjack'
        elif self.player.is_busted():
            self.subtract_money()
            result = 'bust'
        elif self.dealer.is_busted():
            self.add_money()
            result = 'dealer_bust'
        elif self.player.score > self.dealer.score:
            self.add_money()
            result = 'win'
        elif self.dealer.score > self.player.score:
            self.subtract_money()
            result = 'loss'
        else:
            result = 'tie'

        return result

    def display_result(self, result):
        clear_screen()

        if result == 'blackjack':
            prompt(f'You were dealt {self.TWENTY_ONE}! You win!')
        elif result == 'dealer_blackjack':
            prompt(f'The dealer was dealt {self.TWENTY_ONE}! The dealer wins.')
        elif result == 'bust':
            prompt(f'{player_total_prompt()}{self.player.score}')
            prompt('You busted!')
        elif result == 'dealer_bust':
            prompt(f'{dealer_total_prompt()}{self.dealer.score}')
            prompt('The dealer busted! You win!')
        elif result == 'win':
            prompt(f'{player_total_prompt()}{self.player.score}')
            prompt(f'{dealer_total_prompt()}{self.dealer.score}')
            prompt('You win!')
        elif result == 'loss':
            prompt(f'{player_total_prompt()}{self.player.score}')
            prompt(f'{dealer_total_prompt()}{self.dealer.score}')
            prompt('The dealer wins!')
        elif result == 'tie':
            prompt(f'{player_total_prompt()}{self.player.score}')
            prompt(f'{dealer_total_prompt()}{self.dealer.score}')
            prompt('It\'s a tie!')

    def comment_on_wealth(self):
        if self.player.money >= 10:
            prompt('You\'ve doubled your cash! Quit while you\'re ahead!')
            sleep(3)
        else:
            prompt('Sorry, you\'re broke!')
            sleep(3)

    def play_again(self):
        self.display_money()
        replay = input('Play again? (y/n): ').lower()
        while not replay or replay[0] not in 'yn':
            replay = input('Please enter a valid input (y/n): ').lower()

        return replay[0] == 'y'

    def reset_game(self):
        self.player.hand.clear()
        self.dealer.hand.clear()
        self.player.update_score(self.player.hand)
        self.dealer.update_score(self.dealer.hand)


game = TwentyOneGame()
game.start()
