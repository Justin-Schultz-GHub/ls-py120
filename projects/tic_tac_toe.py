import random
import os

def clear_screen():
    os.system('clear')

class Board:
    def __init__(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")
        print()

    def display_clear(self):
        # clear_screen()
        print("\n")
        self.display()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)


class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

    def __str__(self):
        return self.marker


class Player:
    def __init__(self, marker):
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker


class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)


class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)


class TTTGame:
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    )

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()

    def play(self):
        self.welcome_player()

        while True:
            self.board.display()

            while True:
                self.human_turn()

                if self.is_game_over():
                    break

                self.computer_turn()

                if self.is_game_over():
                    break

                self.board.display_clear()

            self.board.display_clear()
            self.announce_result()

            if not self.play_again():
                break

            self.reset_game()

        self.display_goodbye_message()


    def welcome_player(self):
        clear_screen()
        print("Welcome to Tic Tac Toe!")

    def display_goodbye_message(self):
        print("Thanks for playing!")

    @staticmethod
    def _join_or(choices, separator=", ", conjuction="or"):
        if len(choices) > 1:
            last_value = choices.pop()
            choices_str = (f"{separator.join(choices)}"
                      f"{separator}{conjuction} {last_value}")

            return choices_str

        return str(choices[0])

    def human_turn(self):
        valid_choices = self.board.unused_squares()

        while True:
            choices_list = [str(choice) for choice in valid_choices]
            choices_str = TTTGame._join_or(choices_list)
            prompt = f"Choose a square ({choices_str}): "

            try:
                choice = int(input(prompt))
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("That\'s not a valid square.")

        self.board.mark_square_at(choice, self.human.marker)

    def computer_turn(self):
        valid_choices = self.board.unused_squares()
        choice = self.find_vulnerable_square()
        if choice is None:
            choice = random.choice(valid_choices)
        self.board.mark_square_at(choice, self.computer.marker)

    def find_vulnerable_square(self):
        ODDS = [1, 3, 5, 7, 9]
        EVENS = [2, 4, 6, 8]

        # Priority 1: Check for empty middle square
        if self.board.squares[5].is_unused():
            return 5

        for line in self.POSSIBLE_WINNING_ROWS:
            sq1, sq2, sq3 = line

            markers = [self.board.squares[sq1].marker,
                       self.board.squares[sq2].marker,
                       self.board.squares[sq3].marker
                       ]

            # Priority 2: Check for computer win
            if (
                markers.count(Square.COMPUTER_MARKER) == 2
                and markers.count(Square.INITIAL_MARKER) == 1
            ):
                return line[markers.index(Square.INITIAL_MARKER)]

            # Priority 3: Human block check
            if (
                markers.count(Square.HUMAN_MARKER) == 2
                and markers.count(Square.INITIAL_MARKER) == 1
            ):
                return line[markers.index(Square.INITIAL_MARKER)]

            #Prio 4: Check double intercardinals, and block cardinal
            print(self.board.squares[sq1].marker == Square.HUMAN_MARKER)
            if (
                self.board.squares[sq1].marker == Square.HUMAN_MARKER
                and self.board.squares[sq3].marker == Square.HUMAN_MARKER
                and sq1 + sq3 == 10
                and sq1 % 2 == 1
            ):
                return random.choice(EVENS)

        for line in self.POSSIBLE_WINNING_ROWS:
            sq1, sq2, sq3 = line

            markers = [self.board.squares[sq1].marker,
                       self.board.squares[sq2].marker,
                       self.board.squares[sq3].marker
                       ]

            # Priority 5: Take advantage line, prioritize corners
            if (
                markers.count(Square.COMPUTER_MARKER) >= 1
                and markers.count(Square.HUMAN_MARKER) == 0
            ):
                for num in ODDS:
                    if self.board.squares[num].is_unused():
                        return num
                return line[markers.index(Square.INITIAL_MARKER)]

            # Priority 6: Take corner
            for num in ODDS:
                if self.board.squares[num].is_unused():
                    return num

            # Priority 7: Fallback marker
            if (
                markers.count(Square.COMPUTER_MARKER) == 2
                and markers.count(Square.HUMAN_MARKER) == 0
            ):
                return line[markers.index(Square.INITIAL_MARKER)]

        # Return none and choose random square
        return None

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def someone_won(self):
        return self.is_winner(self.human) or self.is_winner(self.computer)

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False

    def announce_result(self):
        if self.is_winner(self.human):
            print("You win! Congratz!")
        elif self.is_winner(self.computer):
            print("The computer wins!")
        else:
            print("Game over! It\'s a tie!")

    def play_again(self):
        prompt = input('Play again? (y/n): ').lower()
        while prompt[0] not in ['y', 'n']:
            prompt = input('Please enter a valid input (y/n): ').lower()

        return prompt[0] == 'y'

    def reset_game(self):
        for num in range(1, 10):
            self.board.mark_square_at(num, Square.INITIAL_MARKER)

        clear_screen()


game = TTTGame()
game.play()
