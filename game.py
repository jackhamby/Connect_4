from easter_egg import easter_egg
from fonts import winner_text, border_text

BOARD_WIDTH = 7
BOARD_HEIGHT = 6
WINNING_LENGTH = 4

class Player:
    def __init__(self, name, icon, session, is_human_player=True):
        self.name = name
        self.icon = icon
        self.session = session
        self.is_human_player = is_human_player

    def take_turn(self):
        move = input("> ")
        if (self.session.validate_move(move)):
            self.session.last_move_location = session.board.update(int(move))
            if (self.session.last_move_location):
                return True
        return False
        

class Board:

    def __init__(self, width, height, session):
        self.width = width
        self.height = height
        self.session = session
        self.current_state = [['-' for x in range(0, self.width)] for x in range(0, self.height)]

    def render(self):
        print('##=====================================##')
        print('##=====================================##')
        print('\n')
        print("    ", end="")
        for index in range(0, self.width):
            print(index, end="   ")
        print ('\n')
        for i, row in enumerate(self.current_state):
            print(i, end="   ")
            for item in row:
                print(item, end="   ")
            print('\n')
    
        print('\n')
        print('##=====================================##')
        print('##=====================================##')

    def update(self, move):
        for i in range(self.height - 1, -1, -1):
            if (self.current_state[i][move] == '-'):
                self.current_state[i][move] = session.going_player.icon
                return (move, i)
        return False


class GameSession:

    def __init__(self, 
                player_1_name="player_1",
                player_2_name="player_2",
                player_1_icon="X",
                player_2_icon="O",
                is_single_player=False):
        self.winning_length = WINNING_LENGTH
        self.board = Board(BOARD_WIDTH, BOARD_HEIGHT, self)
        self.player_1 = Player(player_1_name, player_1_icon, self)
        self.player_2 = Player(player_2_name, player_2_icon, self)
        self.is_single_player = is_single_player
        self.going_player = self.player_1
        self.last_move_location = False
        self.running = True

    def start(self):
        print('starting the game')
        self.render()
        while(self.running):
            self.display_prompt()
            if (self.going_player.take_turn()):
                self.render()
                if (self.check_for_winner()):
                    self.end()
                self.going_player = self.player_1 if self.going_player.name == self.player_2.name else self.player_2
            else:
                self.display_error()

    def display_prompt(self):
        print(f'{self.going_player.name} please take your turn')
    
    def display_error(self):
        print('INVALID move')

    def display_win(self):
        print(border_text)
        print(winner_text)
        print(border_text)
        print(f'Congrats {self.going_player.name} on winning the game!')

    def validate_move(self, move):
        if (self.check_if_command(move)):
            return False
        try:
            move = int(move)
        except ValueError:
            return False
        if ( 0 <= move <= 6 ):
            return True
        return False

    def check_for_winner(self):
        print(self.last_move_location)
        if (self.propagate(self.last_move_location, -1,-1, 1)
            or self.propagate(self.last_move_location, 1,1, 1)
            or self.propagate(self.last_move_location, -1,1, 1)
            or self.propagate(self.last_move_location, 1,-1, 1)
            or self.propagate(self.last_move_location, 0,1, 1)
            or self.propagate(self.last_move_location, 1,0, 1)
            or self.propagate(self.last_move_location, -1,0, 1)
            or self.propagate(self.last_move_location, 0,-1, 1)):
            # player wins
            return True
        return False
        # no one has won

    def check_if_command(self, player_input):
        if (player_input == 'exit' or player_input == 'quit'):
            print('Thanks for playing')
            self.running = False
            return True
        elif (player_input == 'help' or player_input == '?' or player_input == "?help"):
            print('nothing to help you with')
            return True
        elif (player_input == 'jack rulez'):
            print(easter_egg)
            return True
        return False

    def propagate(self, location, x_dir, y_dir, count):
        if (0 <= location[0] + x_dir < self.board.width and
            0 <= location[1] + y_dir < self.board.height):
            # If find match
            if (self.board.current_state[location[1] + y_dir][location[0] + x_dir] == self.going_player.icon):
                count = count + 1
                if (count == self.winning_length):
                    return True
                return self.propagate(
                        (location[0] + x_dir, location[1] + y_dir),
                        x_dir,
                        y_dir,
                        count 
                )
        return False
        
    def end(self):
        self.running = False
        self.display_win()

    def render(self):
        self.board.render()

        
        
        
        
        
       
# Create Game
session = GameSession()

# Start the game
session.start()

















