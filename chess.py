class Piece:
    def __init__(self, color):
        self.color = color

    def get_moves(self, board, x, y):
        pass

class Pawn(Piece):
    def get_moves(self, board, x, y):
        direction = 1 if self.color == 'white' else -1
        moves = []
        if board[y + direction][x] is None:
            moves.append((x, y + direction))
        return moves

class Knight(Piece):
    def get_moves(self, board, x, y):
        moves = []
        for dx, dy in [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]:
            if 0 <= x + dx < 8 and 0 <= y + dy < 8:
                moves.append((x + dx, y + dy))
        return moves

# Other piece classes like Rook, Bishop, Queen, and King can be added similarly.

class Board:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        for i in range(8):
            self.board[1][i] = Pawn('white')
            self.board[6][i] = Pawn('black')
        self.board[0][1] = self.board[0][6] = Knight('white')
        self.board[7][1] = self.board[7][6] = Knight('black')

    def print_board(self):
        for row in self.board:
            print(' '.join(['.' if piece is None else piece.__class__.__name__[0] for piece in row]))
        print()

    def move_piece(self, start_x, start_y, end_x, end_y):
        piece = self.board[start_y][start_x]
        self.board[end_y][end_x] = piece
        self.board[start_y][start_x] = None

### Step 2: Define the Game Logic

class Game:
    def __init__(self):
        self.board = Board()
        self.current_turn = 'white'

    def play(self):
        while True:
            self.board.print_board()
            if self.current_turn == 'white':
                self.player_move()
            else:
                self.bot_move()
            self.current_turn = 'black' if self.current_turn == 'white' else 'white'

    def player_move(self):
        start_x, start_y, end_x, end_y = map(int, input("Enter your move (start_x start_y end_x end_y): ").split())
        self.board.move_piece(start_x, start_y, end_x, end_y)

    def bot_move(self):
        for y in range(8):
            for x in range(8):
                piece = self.board.board[y][x]
                if piece and piece.color == 'black':
                    moves = piece.get_moves(self.board.board, x, y)
                    if moves:
                        end_x, end_y = moves[0]
                        self.board.move_piece(x, y, end_x, end_y)
                        return

game = Game()
game.play()