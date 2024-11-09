# # Circular Buffer
# class CircularBuffer:
#     def __init__(self, size):
#         self.size = size
#         self.buffer = [None] * self.size
#         self.get_cycle = 0
#         self.put_cycle = 0

#     def get(self):
#         if all(pos is None for pos in self.buffer):
#             return None

#         idx_value = self.buffer[self.get_cycle]
#         self.buffer[self.get_cycle] = None
#         self.get_cycle += 1

#         self.get_cycle %= len(self.buffer)

#         return idx_value

#     def put(self, num):
#         self.buffer[self.put_cycle] = num
#         self.put_cycle += 1

#         self.put_cycle %= len(self.buffer)

#         if self.put_cycle == self.get_cycle - 1 and None not in self.buffer:
#             self.get_cycle -= 1

#         if self.put_cycle > self.get_cycle and None not in self.buffer:
#             self.get_cycle += 1


# buffer = CircularBuffer(3)

# print(buffer.get() is None)          # True

# buffer.put(1)
# buffer.put(2)

# print(buffer.get() == 1)             # True

# buffer.put(3)
# buffer.put(4)
# print(buffer.get() == 2)             # True

# buffer.put(5)
# buffer.put(6)
# buffer.put(7)
# print(buffer.get() == 5)             # True
# print(buffer.get() == 6)             # True
# print(buffer.get() == 7)             # True
# print(buffer.get() is None)          # True

# buffer2 = CircularBuffer(4)

# print(buffer2.get() is None)         # True

# buffer2.put(1)
# buffer2.put(2)
# print(buffer2.get() == 1)            # True

# buffer2.put(3)
# buffer2.put(4)
# print(buffer2.get() == 2)            # True

# buffer2.put(5)
# buffer2.put(6)
# buffer2.put(7)
# print(buffer2.get() == 4)            # True
# print(buffer2.get() == 5)            # True
# print(buffer2.get() == 6)            # True
# print(buffer2.get() == 7)            # True
# print(buffer2.get() is None)         # True

# print(buffer.buffer)


# # Number Guesser Part 1
# # First iteration
# import random
# class GuessingGame:
#     def play(self):
#         rand_num = random.randint(1, 100)
#         guesses = 7

#         while guesses:
#             self.guesses_remaining(guesses)
#             guess = self.get_guess()
#             result = self.check_guess(guess, rand_num)

#             if result == 'Winner':
#                 self.announce_win()
#                 break
#             else:
#                 self.announce_result(result)
#                 guesses = self.subtract_guess(guesses)

#         else:
#             self.announce_loss(rand_num)

#     def guesses_remaining(self, guesses):
#         print(f'You have {guesses} guesses remaining.')

#     def get_guess(self):
#         guess = input('Enter a number from 1 to 100 (including 100): ')

#         while not self.valid_guess(guess):
#             guess = input('Enter a number from 1 to 100 (including 100): ')

#         return int(guess)

#     def valid_guess(self, guess):
#         try:
#             guess = int(guess)
#         except ValueError:
#             print('Invalid guess: Must be a number')
#             return False

#         if 1 <= guess <= 100:
#             return guess
#         else:
#             print('Invalid guess: Must be between 1 and 100')
#             return False

#     def check_guess(self, guess, rand_num):
#         if guess == rand_num:
#             return 'Winner'

#         if guess > rand_num:
#             return 'High'

#         if guess < rand_num:
#             return 'Low'

#     def announce_win(self):
#         print('That\'s the number! You win!')

#     def announce_result(self, result):
#         print(f'Your guess is too {result.lower()}.')
#         print('')

#     def subtract_guess(self, num):
#         return num - 1

#     def announce_loss(self, number):
#         print(f'You\'re out of guesses!')
#         print(f'The number was {number}!')


# game = GuessingGame()
# game.play()

# # ChatGPT recommendations implemented (some)
# import random
# class GuessingGame:
#     MESSAGES = {
#         'win': 'That\'s the number! You win!',
#         'loss': 'You\'re out of guesses!\nThe number was {number}!',
#         'high': 'Your guess is too high!',
#         'low': 'Your guess is too low!',
#         'input_prompt': 'Enter a number from 1 to 100 (including 100): ',
#         'out_of_range': 'Invalid guess: Must be between 1 and 100',
#         'not_a_number': 'Invalid guess: Must be a number',
#         'remaining_guesses': 'You have {guesses} guesses remaining.',

#     }

#     def play(self):
#         rand_num = random.randint(1, 100)
#         guesses = 7

#         while guesses:
#             self.guesses_remaining(guesses)
#             guess = self.get_guess()
#             result = self.check_guess(guess, rand_num)

#             if result == 'Winner':
#                 self.announce_win()
#                 break
#             else:
#                 self.announce_result(result)
#                 guesses -= 1

#         else:
#             self.announce_loss(rand_num)

#     def guesses_remaining(self, guesses):
#         print(self.MESSAGES['remaining_guesses'].format(guesses=guesses))

#     def get_guess(self):
#         guess = None

#         while guess is None:
#             user_input = input(f"{self.MESSAGES['input_prompt']}")
#             guess = self.valid_guess(user_input)

#         return guess

#     def valid_guess(self, guess):
#         try:
#             guess = int(guess)
#         except ValueError:
#             print(f"{self.MESSAGES['not_a_number']}")
#             return None

#         if 1 <= guess <= 100:
#             return guess
#         else:
#             print(f"{self.MESSAGES['out_of_range']}")
#             return None

#     def check_guess(self, guess, rand_num):
#         if guess == rand_num:
#             return 'Winner'
#         elif guess > rand_num:
#             return 'High'
#         else:
#             return 'Low'

#     def announce_win(self):
#         print(self.MESSAGES['win'])

#     def announce_result(self, result):
#         if result == 'High':
#             print(self.MESSAGES['high'])
#         elif result == 'Low':
#             print(self.MESSAGES['low'])
#         print('')

#     def announce_loss(self, number):
#         print(self.MESSAGES['loss'].format(number=number))


# game = GuessingGame()
# game.play()


# # Number Guesser Part 2
# import random
# import math

# class GuessingGame:
#     MESSAGES = {
#         'win': 'That\'s the number! You win!',
#         'loss': 'You\'re out of guesses!\nThe number was {number}!',
#         'high': 'Your guess is too high!',
#         'low': 'Your guess is too low!',
#         'input_prompt': (
#             'Enter a number from {low} to {high} (including {high}): '
#             ),
#         'out_of_range': 'Invalid guess: Must be between {low} and {high}',
#         'not_a_number': 'Invalid guess: Must be a number',
#         'high_is_low': (
#             'Invalid maximum (must be higher than the minimum ({minimum}))'
#             ),
#         'remaining_guesses': 'You have {guesses} guesses remaining.',
#         'enter_min': 'Enter a minimum value: ',
#         'enter_max': 'Enter a maximum value: ',

#     }

#     def play(self):
#         low, high = self.get_range()
#         rand_num = random.randint(low, high)
#         guesses = int(math.log2(high - low + 1)) + 1

#         while guesses:
#             self.guesses_remaining(guesses)
#             guess = self.get_guess(low, high)
#             result = self.check_guess(guess, rand_num)

#             if result == 'Winner':
#                 self.announce_win()
#                 break
#             else:
#                 self.announce_result(result)
#                 guesses -= 1

#         else:
#             self.announce_loss(rand_num)

#     def get_range(self):
#         low = None

#         while low is None:
#             low = input(self.MESSAGES['enter_min'])
#             low = self.valid_min_value(low)

#         high = None

#         while high is None:
#             high = input(self.MESSAGES['enter_max'])
#             high = self.valid_max_value(low, high)

#         return low, high

#     def valid_min_value(self, value):
#         try:
#             int(value)
#         except ValueError:
#             print(f"{self.MESSAGES['not_a_number']}")
#             return None

#         return int(value)

#     def valid_max_value(self, value, high):
#         try:
#             int(high)
#         except ValueError:
#             print(f"{self.MESSAGES['not_a_number']}")
#             return None

#         if int(high) <= value:
#             print(f"{self.MESSAGES['high_is_low'].format(minimum=value)}")
#             return None

#         return int(high)

#     def guesses_remaining(self, guesses):
#         print(self.MESSAGES['remaining_guesses'].format(guesses=guesses))

#     def get_guess(self, low, high):
#         guess = None

#         while guess is None:
#             user_input = input(
#                 f"{self.MESSAGES['input_prompt'].format(low=low, high=high)}"
#                 )
#             guess = self.valid_guess(user_input, low, high)

#         return guess

#     def valid_guess(self, guess, low, high):
#         try:
#             guess = int(guess)
#         except ValueError:
#             print(f"{self.MESSAGES['not_a_number']}")
#             return None

#         if low <= guess <= high:
#             return guess
#         else:
#             print(
#                 f"{self.MESSAGES['out_of_range'].format(low=low, high=high)}"
#                 )
#             return None

#     def check_guess(self, guess, rand_num):
#         if guess == rand_num:
#             return 'Winner'
#         elif guess > rand_num:
#             return 'High'
#         else:
#             return 'Low'

#     def announce_win(self):
#         print(self.MESSAGES['win'])

#     def announce_result(self, result):
#         if result == 'High':
#             print(self.MESSAGES['high'])
#         elif result == 'Low':
#             print(self.MESSAGES['low'])
#         print('')

#     def announce_loss(self, number):
#         print(self.MESSAGES['loss'].format(number=number))


# game = GuessingGame()
# game.play()


# Highest and Lowest Ranking Cards
# class Card:
#     RANKS = [*range(2, 11), 'Jack', 'Queen', 'King', 'Ace']
#     RANK_RANKS = {rank: num for num, rank in enumerate(RANKS)}

#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit

#     def __str__(self):
#         return f'{self.rank} of {self.suit}'

#     def __lt__(self, other):
#         return self.RANK_RANKS[self.rank] < other.RANK_RANKS[other.rank]

#     def __eq__(self, other):
#         return str(self) == str(other)


# # Further exploration
# class Card:
#     RANKS = [*range(2, 11), 'Jack', 'Queen', 'King', 'Ace']
#     RANK_RANKS = {rank: num for num, rank in enumerate(RANKS)}
#     SUITS = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
#     SUIT_RANKS = {suit: num for num, suit in enumerate(SUITS)}

#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit

#     def __str__(self):
#         return f'{self.rank} of {self.suit}'

#     def __lt__(self, other):
#         if self.RANK_RANKS[self.rank] == other.RANK_RANKS[other.rank]:
#             return self.SUIT_RANKS[self.suit] < other.SUIT_RANKS[other.suit]

#         return self.RANK_RANKS[self.rank] < other.RANK_RANKS[other.rank]

#     def __eq__(self, other):
#         return str(self) == str(other)

# cards = [Card('Ace', 'Spades'),
#         Card('Ace', 'Clubs'),
#         Card('Ace', 'Diamonds')]
# print(min(cards) == Card('Ace', 'Diamonds'))    # True
# print(max(cards) == Card('Ace', 'Spades'))      # True
# print(str(min(cards)) == "Ace of Diamonds")     # True
# print(str(max(cards)) == "Ace of Spades")       # True

# cards = [Card(2, 'Hearts'),
#          Card(10, 'Diamonds'),
#          Card('Ace', 'Clubs')]
# print(min(cards) == Card(2, 'Hearts'))             # True
# print(max(cards) == Card('Ace', 'Clubs'))          # True
# print(str(min(cards)) == "2 of Hearts")            # True
# print(str(max(cards)) == "Ace of Clubs")           # True

# cards = [Card(5, 'Hearts')]
# print(min(cards) == Card(5, 'Hearts'))             # True
# print(max(cards) == Card(5, 'Hearts'))             # True
# print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

# cards = [Card(4, 'Hearts'),
#          Card(4, 'Diamonds'),
#          Card(10, 'Clubs')]
# print(min(cards).rank == 4)                        # True
# print(max(cards) == Card(10, 'Clubs'))             # True
# print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

# cards = [Card(7, 'Diamonds'),
#          Card('Jack', 'Diamonds'),
#          Card('Jack', 'Spades')]
# print(min(cards) == Card(7, 'Diamonds'))           # True
# print(max(cards).rank == 'Jack')                   # True
# print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

# cards = [Card(8, 'Diamonds'),
#          Card(8, 'Clubs'),
#          Card(8, 'Spades')]
# print(min(cards).rank == 8)                        # True
# print(max(cards).rank == 8)                        # True


# Deck Of Cards
# import random

# class Card:
#     RANKS = [*range(2, 11), 'Jack', 'Queen', 'King', 'Ace']
#     RANK_RANKS = {rank: num for num, rank in enumerate(RANKS)}
#     SUITS = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
#     SUIT_RANKS = {suit: num for num, suit in enumerate(SUITS)}

#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit

#     def __str__(self):
#         return f'{self.rank} of {self.suit}'

#     def __lt__(self, other):
#         if self.RANK_RANKS[self.rank] == other.RANK_RANKS[other.rank]:
#             return self.SUIT_RANKS[self.suit] < other.SUIT_RANKS[other.suit]

#         return self.RANK_RANKS[self.rank] < other.RANK_RANKS[other.rank]

#     def __eq__(self, other):
#         return str(self) == str(other)


# class Deck:
#     RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
#     SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

#     def __init__(self):
#         self._reset()

#     def _reset(self):
#         self._deck = [Card(rank, suit)
#                     for rank in self.RANKS
#                     for suit in self.SUITS]

#         random.shuffle(self._deck)

#     def draw(self):
#         if not self._deck:
#             self._reset()

#         return self._deck.pop()


# deck = Deck()
# drawn = []
# for _ in range(52):
#     drawn.append(deck.draw())

# count_rank_5 = sum([1 for card in drawn if card.rank == 5])
# count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

# print(count_rank_5 == 4)      # True
# print(count_hearts == 13)     # True

# drawn2 = []
# for _ in range(52):
#     drawn2.append(deck.draw())

# print(drawn != drawn2)        # True (Almost always).

# Poker
import random

class Card:
    RANKS = [*range(2, 11), 'Jack', 'Queen', 'King', 'Ace']
    RANK_RANKS = {rank: num + 2 for num, rank in enumerate(RANKS)}
    SUITS = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
    SUIT_RANKS = {suit: num for num, suit in enumerate(SUITS)}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def __lt__(self, other):
        if self.RANK_RANKS[self.rank] == other.RANK_RANKS[other.rank]:
            return self.SUIT_RANKS[self.suit] < other.SUIT_RANKS[other.suit]

        return self.RANK_RANKS[self.rank] < other.RANK_RANKS[other.rank]

    def __eq__(self, other):
        return str(self) == str(other)


class Deck:
    RANKS = [*range(2, 11), 'Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

    def __init__(self):
        self._reset()

    def _reset(self):
        self._deck = [Card(rank, suit)
                    for rank in self.RANKS
                    for suit in self.SUITS]

        random.shuffle(self._deck)

    def draw(self):
        if not self._deck:
            self._reset()

        return self._deck.pop()

    def __str__(self):
        return '\n'.join(str(card) for card in self._deck)


class PokerHand:
    def __init__(self, deck):
        self._hand = [deck.draw() for _ in range(5)]
        self._hand_ranks = [card.rank for card in self._hand]

    def print(self):
        for card in self._hand:
            print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
            return "High card"

    def _is_royal_flush(self):
        if all(card.suit == self._hand[-1].suit for card in self._hand):
            if (all(card.rank in
                Deck.RANKS[Deck.RANKS.index(10):Deck.RANKS.index('Ace') + 1]
                for card in self._hand)):
                return True

        return False

    def _is_straight_flush(self):
        if all(card.suit == self._hand[-1].suit for card in self._hand):
            sorted_ranks = (sorted(
                            self._hand_ranks,
                            key=lambda rank: Deck.RANKS.index(rank),
                            reverse=True))

            for i in range(len(sorted_ranks) - 1):
                if (Card.RANK_RANKS[sorted_ranks[i]] -
                    Card.RANK_RANKS[sorted_ranks[i + 1]]
                    != 1):
                    return False

            return True

        return False

    def _is_four_of_a_kind(self):
        return (any(self._hand_ranks.count(card.rank) == 4
                for card in self._hand))

    def _is_full_house(self):
        return (set(
                [self._hand_ranks.count(rank) for rank in self._hand_ranks])
                == {2, 3})

    def _is_flush(self):
        return all(card.suit == self._hand[0].suit for card in self._hand)

    def _is_straight(self):
        sorted_ranks = (sorted(self._hand_ranks,
                        key=lambda rank: Deck.RANKS.index(rank),
                        reverse=True))
        for i in range(len(sorted_ranks) - 1):
            if (Card.RANK_RANKS[sorted_ranks[i]] -
                Card.RANK_RANKS[sorted_ranks[i + 1]]
                != 1):
                return False

        return True

    def _is_three_of_a_kind(self):
        return (any(self._hand_ranks.count(card.rank) == 3
                for card in self._hand))

    def _is_two_pair(self):
        return ([self._hand_ranks.count(rank)
                for rank in set(self._hand_ranks)].count(2)
                == 2)

    def _is_pair(self):
        return ([self._hand_ranks.count(rank)
                for rank in set(self._hand_ranks)].count(2)
                == 1)


hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")