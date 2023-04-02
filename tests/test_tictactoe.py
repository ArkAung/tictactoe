import unittest
from tictactoe.tictactoe import TicTacToeLogic

class TestTicTacToeLogic(unittest.TestCase):
    def test_check_winner(self):
        game = TicTacToeLogic()

        # Test rows
        game.board = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
        self.assertEqual(game.check_winner("X"), "X")

        game.board = [[" ", " ", " "], ["O", "O", "O"], [" ", " ", " "]]
        self.assertEqual(game.check_winner("O"), "O")

        # Test columns
        game.board = [["X", " ", " "], ["X", " ", " "], ["X", " ", " "]]
        self.assertEqual(game.check_winner("X"), "X")

        game.board = [[" ", "O", " "], [" ", "O", " "], [" ", "O", " "]]
        self.assertEqual(game.check_winner("O"), "O")

        # Test diagonals
        game.board = [["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]]
        self.assertEqual(game.check_winner("X"), "X")

        game.board = [[" ", " ", "O"], [" ", "O", " "], ["O", " ", " "]]
        self.assertEqual(game.check_winner("O"), "O")

        # Test no winner
        game.board = [["X", "O", "X"], ["X", "X", "O"], ["O", "X", "O"]]
        self.assertIsNone(game.check_winner("X"))
        self.assertIsNone(game.check_winner("O"))

    def test_make_move(self):
        game = TicTacToeLogic()

        # Test making valid moves
        game.make_move(0, 0)
        self.assertEqual(game.board[0][0], "X")

        game.make_move(1, 1)
        self.assertEqual(game.board[1][1], "O")

        # Test making invalid moves (overwriting existing move)
        game.make_move(0, 0)
        self.assertEqual(game.board[0][0], "X")

    def test_reset_board(self):
        game = TicTacToeLogic()

        game.board = [["X", "O", "X"], ["X", "X", "O"], ["O", "X", "O"]]
        game.current_player = "O"

        game.reset_board()

        for row in game.board:
            for cell in row:
                self.assertEqual(cell, " ")
        self.assertEqual(game.current_player, "X")

if __name__ == '__main__':
    unittest.main()
