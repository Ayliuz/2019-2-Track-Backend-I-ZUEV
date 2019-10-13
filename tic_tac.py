class TicTac():
    mapFactor = (2, 3, 5, 7, 11, 13, 17, 19, 23)
    absWinPos = ((2, 3, 5), (7, 11, 13),
                 (17, 19, 23), (2, 7, 17),
                 (3, 11, 19), (5, 13, 23),
                 (2, 11, 23), (5, 11, 17))

    map = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    turn = 1
    empty = 9
    game_pos_X = 1
    game_pos_O = 1

    def restart(self):
        self.map = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.turn = 1
        self.empty = 9
        self.game_pos_X = 1
        self.game_pos_O = 1

        return

    def count_pos(self):
        self.game_pos_X = 1
        self.game_pos_O = 1

        for i in range(9):
            if self.map[i] == 'X':
                self.game_pos_X *= self.mapFactor[i]

            elif self.map[i] == 'O':
                self.game_pos_O *= self.mapFactor[i]

        return

    def draw_map(self):
        print('_____________')
        print('|', self.map[0], '|', self.map[1], '|', self.map[2], '|')
        print('|', self.map[3], '|', self.map[4], '|', self.map[5], '|')
        print('|', self.map[6], '|', self.map[7], '|', self.map[8], '|')
        print('‾‾‾‾‾‾‾‾‾‾‾‾‾')

        return

    def win_check(self):
        winner = 0
        if self.empty < 1:
            print('Ничья.')
            return self.new_game()

        self.count_pos()
        for tuples in self.absWinPos:
            if self.game_pos_X % tuples[0] == 0 and \
                    self.game_pos_X % tuples[1] == 0 and \
                    self.game_pos_X % tuples[2] == 0:
                winner = 1
                break

            if self.game_pos_O % tuples[0] == 0 and \
                    self.game_pos_O % tuples[1] == 0 and \
                    self.game_pos_O % tuples[2] == 0:
                winner = 2
                break

        if winner == 1:
            self.draw_map()
            print('Крестики победили.')
            return self.new_game()

        elif winner == 2:
            self.draw_map()
            print('Нолики победили.')
            return self.new_game()

        return 0

    def new_game(self):
        while True:
            print('Введите \'new\', чтобы начать новую игру, '
                  '\'exit\', чтобы выйти:')
            inp = input()
            if inp == 'new':
                return 1
            elif inp == 'exit':
                return -1
            else:
                print('Недействительный ввод')
                continue

        return 0

    def crosses_turn(self):
        print('Ход крестиков. Введите поле или \'exit\', чтобы выйти:')
        inp = input()

        if inp == 'exit':
            return -1

        if (not inp.isdigit()) or \
                int(inp) > 9 or \
                int(inp) < 1 or \
                self.map[int(inp) - 1] == 'X' or \
                self.map[int(inp) - 1] == 'O':
            print('Недействительное поле')
            return 1

        self.turn = 2
        self.empty -= 1
        self.map[int(inp) - 1] = 'X'

        return 0

    def zeros_turn(self):
        print('Ход ноликов. Введите поле или \'exit\', чтобы выйти:')
        inp = input()

        if inp == 'exit':
            return -1

        if (not inp.isdigit()) or \
                int(inp) > 9 or \
                int(inp) < 1 or \
                self.map[int(inp) - 1] == 'X' or \
                self.map[int(inp) - 1] == 'O':
            print('Недействительное поле')
            return 1

        self.turn = 1
        self.empty -= 1
        self.map[int(inp) - 1] = 'O'

        return 0

    def play(self):
        print('Приветствую в Крестиках-Ноликах. Введите \'start\', '
              'чтобы начать игру, \'exit\', чтобы выйти:')
        inp = input()

        while inp != 'exit':
            if inp == 'start':
                break
            else:
                print('Недействительный ввод')
                inp = input()

        while inp != 'exit':
            self.draw_map()

            if self.turn == 1:
                turn_res = self.crosses_turn()
                if turn_res == 1:
                    continue
                elif turn_res == -1:
                    break

            else:
                turn_res = self.zeros_turn()
                if turn_res == 1:
                    continue
                elif turn_res == -1:
                    break

            result = self.win_check()
            if result == 1:
                self.restart()
                continue
            elif result == -1:
                break

        return


if __name__ == '__main__':
    tictac = TicTac()
    tictac.play()
