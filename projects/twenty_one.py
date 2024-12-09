class Card:
    def __init__(self):
        # STUB
        # What attributes does a card need? Rank? Suit?
        #   Points?
        pass

class Deck:
    def __init__(self):
        # STUB
        # What attributes does a deck need? A collection of
        #   52 cards?
        # Some data structure, like a list or dictionary,
        #   might be required.
        pass

    def deal(self):
        # STUB
        # Does the dealer or the deck deal the cards?
        pass

class Participant:
    def __init__(self):
        # STUB
        # What attributes does a participant require? Score?
        #   Hand? Betting balance?
        # What else goes here? all the redundant behaviors
        #   from Player and Dealer?
        pass

class Player(Participant):
    def __init__(self):
        # STUB
        # What additional attributes might a player need?
        # Score? Hand? Amount of money available?
        pass

    def hit(self):
        # STUB
        pass

    def stay(self):
        # STUB
        pass

    def is_busted(self):
        # STUB
        pass

    def score(self):
        # STUB
        pass

class Dealer(Participant):
    def __init__(self):
        # STUB
        # Very similar to a Player; do we need this?
        pass

    def hit(self):
        # STUB
        pass

    def stay(self):
        # STUB
        pass

    def is_busted(self):
        # STUB
        pass

    def score(self):
        # STUB
        pass

    def hide(self):
        # STUB
        pass

    def reveal(self):
        # STUB
        pass

    def deal(self):
        # STUB
        # Does the dealer or the deck deal?
        pass

class TwentyOneGame:
    def __init__(self):
        # STUB
        # What attributes does the game need? A deck? Two
        #   participants?
        pass

    def start(self):
        # SPIKE
        self.display_welcome_message()
        self.deal_cards()
        self.show_cards()
        self.player_turn()
        self.dealer_turn()
        self.display_result()
        self.display_goodbye_message()

    def deal_cards(self):
        # STUB
        pass

    def show_cards(self):
        # STUB
        pass

    def player_turn(self):
        # STUB
        pass

    def dealer_turn(self):
        # STUB
        pass

    def display_welcome_message(self):
        # STUB
        pass

    def display_goodbye_message(self):
        # STUB
        pass

    def display_result(self):
        # STUB
        pass

game = TwentyOneGame()
game.start()