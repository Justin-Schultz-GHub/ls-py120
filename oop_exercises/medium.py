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


# Number Guesser Part 2
import random
import math

class GuessingGame:
    MESSAGES = {
        'win': 'That\'s the number! You win!',
        'loss': 'You\'re out of guesses!\nThe number was {number}!',
        'high': 'Your guess is too high!',
        'low': 'Your guess is too low!',
        'input_prompt': (
            'Enter a number from {low} to {high} (including {high}): '
            ),
        'out_of_range': 'Invalid guess: Must be between {low} and {high}',
        'not_a_number': 'Invalid guess: Must be a number',
        'high_is_low': (
            'Invalid maximum (must be higher than the minimum ({minimum}))'
            ),
        'remaining_guesses': 'You have {guesses} guesses remaining.',
        'enter_min': 'Enter a minimum value: ',
        'enter_max': 'Enter a maximum value: ',

    }

    def play(self):
        low, high = self.get_range()
        rand_num = random.randint(low, high)
        guesses = int(math.log2(high - low + 1)) + 1

        while guesses:
            self.guesses_remaining(guesses)
            guess = self.get_guess(low, high)
            result = self.check_guess(guess, rand_num)

            if result == 'Winner':
                self.announce_win()
                break
            else:
                self.announce_result(result)
                guesses -= 1

        else:
            self.announce_loss(rand_num)

    def get_range(self):
        low = None

        while low is None:
            low = input(self.MESSAGES['enter_min'])
            low = self.valid_min_value(low)

        high = None

        while high is None:
            high = input(self.MESSAGES['enter_max'])
            high = self.valid_max_value(low, high)

        return low, high

    def valid_min_value(self, value):
        try:
            int(value)
        except ValueError:
            print(f"{self.MESSAGES['not_a_number']}")
            return None

        return int(value)

    def valid_max_value(self, value, high):
        try:
            int(high)
        except ValueError:
            print(f"{self.MESSAGES['not_a_number']}")
            return None

        if int(high) <= value:
            print(f"{self.MESSAGES['high_is_low'].format(minimum=value)}")
            return None

        return int(high)

    def guesses_remaining(self, guesses):
        print(self.MESSAGES['remaining_guesses'].format(guesses=guesses))

    def get_guess(self, low, high):
        guess = None

        while guess is None:
            user_input = input(
                f"{self.MESSAGES['input_prompt'].format(low=low, high=high)}"
                )
            guess = self.valid_guess(user_input, low, high)

        return guess

    def valid_guess(self, guess, low, high):
        try:
            guess = int(guess)
        except ValueError:
            print(f"{self.MESSAGES['not_a_number']}")
            return None

        if low <= guess <= high:
            return guess
        else:
            print(
                f"{self.MESSAGES['out_of_range'].format(low=low, high=high)}"
                )
            return None

    def check_guess(self, guess, rand_num):
        if guess == rand_num:
            return 'Winner'
        elif guess > rand_num:
            return 'High'
        else:
            return 'Low'

    def announce_win(self):
        print(self.MESSAGES['win'])

    def announce_result(self, result):
        if result == 'High':
            print(self.MESSAGES['high'])
        elif result == 'Low':
            print(self.MESSAGES['low'])
        print('')

    def announce_loss(self, number):
        print(self.MESSAGES['loss'].format(number=number))


game = GuessingGame()
game.play()
