class TicTacToeImage(object):
    _gameboard_pic_template = "\
╔═══╦═══╦═══╗\n\
║ . ║ . ║ . ║\n\
╠═══╬═══╬═══╣\n\
║ . ║ . ║ . ║\n\
╠═══╬═══╬═══╣\n\
║ . ║ . ║ . ║\n\
╚═══╩═══╩═══╝\n".replace('.', '{}')
    
    def __new__(self, gameboard:list[list[str]], message:str, turn:str):
        self.message = self._get_window(message)
        self.gameboard = self._gameboard_pic_template.format(*[gameboard[i2][i1] for i2 in range(3) for i1 in range(3)])
        self.turn = '\n'.join(self._get_window(turn, 13))
        return self._add_message_window(self) + self.turn

    @staticmethod
    def _get_window(text:str, center:int=0):
        if not text:
            return ''
        lines_window = ['', '' ,'']
        lines_window[0] = '╔{}╗'.format('═' * (len(text)+2))
        lines_window[1] = '║ {} ║'.format(text)
        lines_window[2] = '╚{}╝'.format('═' * (len(text)+2))
        return [line.center(center) for line in lines_window]
    
    def _add_message_window(self):
        if not self.message:
            return self.gameboard
        list_image = self.gameboard.split('\n')
        for index in range(3):
            list_image[index+2] += ' ' + self.message[index]
        return '\n'.join(list_image)