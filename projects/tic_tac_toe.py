class Board:
    def __init__(self):
        self.squares = {
            1: "X",
            2: " ",
            3: " ",
            4: " ",
            5: "O",
            6: " ",
            7: " ",
            8: "O",
            9: "X",
        }

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |  {self.squares[2]}  |  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |  {self.squares[5]}  |  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |  {self.squares[8]}  |  {self.squares[9]}")
        print("     |     |")
        print()


class Row:
    def __init__(self):
        pass


class Square:
    def __init__(self):
        pass


class Marker:
    def __init__(self):
        pass


class Player:
    def __init__(self):
        pass

    def mark(self):
        pass

    def play(self):
        pass


class Human:
    def __init__(self):
        pass


class Computer:
    def __init__(self):
        pass


class TTTGame:
    def __init__(self):
        self.board = Board()


    def play(self):
        self.welcome_player()

        while True:
            self.board.display()
            self.player_one_turn()

            if self.is_game_over():
                break

            self.player_two_turn()

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

    def player_one_turn(self):
        pass

    def player_two_turn(self):
        pass

    def is_game_over(self):
        pass

    def announce_result(self):
        pass



game = TTTGame()
game.play()