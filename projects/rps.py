import random
import os

class Player:
    CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock')

    def __init__(self):
        self.move = None
        self.move_history = None


class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = 'Please choose rock, paper, scissors, lizard, or spock: \n'

        while True:
            choice = input(prompt).lower()

            if choice in Player.CHOICES:
                break

            print(f'Invalid choice: {choice}')

        self.move = choice
        self.move_history.append(self.move)


class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES)
        self.move_history.append(self.move)


class RPSGame:
    WIN_CONDITIONS = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock'],
    }

    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self._human_score = 0
        self._computer_score = 0

    def _display_welcome_message(self):
        print("Welcome to Rock Paper Scissors Lizard Spock Best of 5!")

    def _display_goodbye_message(self):
        print("Thanks for playing!")

    def _human_round_win(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return computer_move in self.WIN_CONDITIONS[human_move]

    def _computer_round_win(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return human_move in self.WIN_CONDITIONS[computer_move]

    def _display_round_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_round_win():
            print(f'{self._human.move} beats {self._computer.move}!')
            print('You win the round!')
        elif self._computer_round_win():
            print(f'{self._computer.move} beats {self._human.move}!')
            print('The computer wins the round!')
        else:
            print('It\'s a tie!')

    def _update_score(self):
        if self._human_round_win():
            self._human_score += 1
        elif self._computer_round_win():
            self._computer_score += 1

    def _display_score(self):
        print(f'The current score is - Player: {self._human_score} '
              f'Computer: {self._computer_score}')

    def _is_winner(self):
        return max(self._human_score, self._computer_score) == 5

    def _announce_winner(self):
        human_score = self._human_score

        if human_score == 5:
            print('The player has 5 points! The player wins!')
        else:
            print('The computer has 5 points! The computer wins!')

    def _display_move_history(self):
        player_title = 'Player moves '
        computer_title = ' Computer moves'

        print(f'{player_title}|{computer_title}')
        for idx, move in enumerate(self._human.move_history):
            move_number = idx + 1
            human_text = f'{move_number:>2}. {move}'
            computer_text = (f'{move_number:>2}. '
                             f'{self._computer.move_history[idx]}')
            space_pad = (len(player_title) - len(human_text)) * ' '
            print(f'{human_text}{space_pad}| {computer_text}')

        print()

    def _play_again(self):
        answer = input('Play again? (y/n): ')
        return answer.lower().startswith('y')

    def play(self):
        os.system('clear')
        self._display_welcome_message()

        while True:
            self._human_score = 0
            self._computer_score = 0
            self._human.move_history = []
            self._computer.move_history = []

            while max(self._human_score, self._computer_score) < 5:
                if self._human_score or self._computer_score:
                    self._display_score()
                if self._human.move_history:
                    self._display_move_history()
                self._human.choose()
                self._computer.choose()
                self._update_score()
                if self._is_winner():
                    self._display_round_winner()
                    self._announce_winner()
                else:
                    self._display_round_winner()
                    print()
            if not self._play_again():
                break

            os.system('clear')

        self._display_goodbye_message()


RPSGame().play()
