import random

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

    def mark_square(self, key, marker):
        self.squares[key] = marker


class Row:
    def __init__(self):
        pass


class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self._marker = marker

    def __str__(self):
        return self._marker


class Marker:
    def __init__(self):
        pass


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
    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()


    def play(self):
        self.welcome_player()

        while True:
            self.board.display()
            self.human_turn()

            if self.is_game_over():
                break

            self.computer_turn()

            if self.is_game_over():
                break

            break

        self.board.display()
        self.announce_result()
        self.display_goodbye_message()

    def welcome_player(self):
        print("Welcome to Tic Tac Toe!")

    def display_goodbye_message(self):
        print("Thanks for playing!")

    def human_turn(self):
        choice = None

        while True:
            try:
                choice = int(input("Please, choose a square (1-9): "))
                if 1 <= choice <= 9:
                    break
            except ValueError:
                pass

            print("That\'s not a valid square.")

        self.board.mark_square(choice, self.human.marker)

    def computer_turn(self):
        choice = random.randint(1, 9)

        self.board.mark_square(choice, self.computer.marker)

    def is_game_over(self):
        pass

    def announce_result(self):
        pass



game = TTTGame()
game.play()