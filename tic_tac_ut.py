import io
import unittest
import unittest.mock

from tic_tac import TicTac


class TicTacUnitTest(unittest.TestCase):

    def runTest(self, map, excpected):
        with unittest.mock.patch('builtins.input', return_value='exit'), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as out:
            example = TicTac()
            example.map = map
            example.win_check()
            self.assertEqual(out.getvalue(), excpected)

    def tes_wi_ch_O_lines(self):
        self.runTest(['O', 'O', 'O',
                      'X', '5', 'X',
                      '7', 'X', 'X'], 'Нолики победили.')
        self.runTest(['X', 'O', 'X',

                      '7', 'X', 'X'], 'Нолики победили.')
        self.runTest(['O', 'O', 'O',
                      'X', '5', 'X',
                      '7', 'X', 'X'], 'Нолики победили.')

    def tes_wi_ch_X_diag(self):
        self.runTest(['X', 'O', 'O',
                      'X', 'X', 'O',
                      '7', 'O', 'X'], 'Крестики победили.')
        self.runTest(['X', 'O', 'X',
                      'O', 'X', 'O',
                      'X', '8', '9'], 'Крестики победили.')

    def test_draw(self):
        with unittest.mock.patch('builtins.input', return_value = 'exit'), \
                unittest.mock.patch('sys.stdout', new = io.StringIO()) as out:

            example = TicTac()
            example.map = ['X', 'O', '3',
                           'O', '5', 'O',
                           '7', 'X', 'X']
            example.draw_map()
            self.assertEqual(out.getvalue(), '_____________\n'
                                             '| X | O | 3 |\n'
                                             '| O | 5 | O |\n'
                                             '| 7 | X | X |\n'
                                             '‾‾‾‾‾‾‾‾‾‾‾‾‾\n')


    def test_play(self):
        with unittest.mock.patch("sys.stdin", io.StringIO("start\n1\n2\n3\n4\n5\n6\n7\nexit")), \
                unittest.mock.patch('sys.stdout', new = io.StringIO()) as out:

            example = TicTac()
            example.play()
            self.assertNotEqual(out.getvalue().find('Крестики победили'), -1)

    def test_restart(self):
        example = TicTac()
        example.map = ['X', 'O', '3',
                       'O', '5', 'O',
                       '7', 'X', 'X']
        example.restart()
        self.assertEqual(example.map, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    def test_count_pos(self):
        example = TicTac()
        example.map = ['X', 'O', '3',
                       'O', '5', 'O',
                       '7', 'X', 'X']
        example.count_pos()
        self.assertEqual(example.game_pos_X, 2 * 19 * 23)
        self.assertEqual(example.game_pos_O, 3 * 7 * 13)

    def test_new_game(self):
        with unittest.mock.patch("sys.stdin", io.StringIO('tfi76\nnew\n')), \
                unittest.mock.patch('sys.stdout', new = io.StringIO()) as out:

            example = TicTac()
            self.assertEqual(example.new_game(), 0)
            self.assertEqual(out.getvalue(), 'Введите \'new\', чтобы начать новую игру, \'exit\', чтобы выйти:\n'
                                             'Недействительный ввод\n'
                                             'Введите \'new\', чтобы начать новую игру, \'exit\', чтобы выйти:\n')

    def test_crosses(self):
        with unittest.mock.patch("sys.stdin", io.StringIO("67")), \
             unittest.mock.patch('sys.stdout', new = io.StringIO()) as out:

            example = TicTac()
            example.crosses_turn()
            self.assertEqual(out.getvalue(), 'Ход крестиков. Введите поле или \'exit\', чтобы выйти:\n'
                                             'Недействительное поле\n')

    def test_zeros(self):
        with unittest.mock.patch("sys.stdin", io.StringIO("1")), \
             unittest.mock.patch('sys.stdout', new = io.StringIO()) as out:

            example = TicTac()
            example.map = ['X', 'O', '3',
                           'O', '5', 'O',
                           '7', 'X', 'X']
            self.assertEqual(example.zeros_turn(), 1)
            self.assertEqual(out.getvalue(), 'Ход ноликов. Введите поле или \'exit\', чтобы выйти:\n'
                                             'Недействительное поле\n')


if __name__ == '__main__':
    unittest.main()
