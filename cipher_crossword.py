# https://py.checkio.org/ru/mission/cipher-crossword/
"""
Все мы пробовали решить кроссворд (ну или хоть видели его). Давайте добавим криптографии. 
В криптокроссворде вместо подсказок на линию используются подсказки на клетки. 
Клетки имеют номера от 1 до 26. Каждое число соответствует какой то букве (и только одно) английского алфавита. 
Также вам известны слова для кроссворда и ваша задача корректно его заполнить.

Дан пустой кроссворд, как 2-ух мерный массив с числами, где 0 - это пустая клетка, а остальные числа соответствуют зашифрованным буквам. 
Также дан список слов для кроссворда. Вы должны заполнить кроссворд и вернуть решенный кроссворд, как 2-ух мерный массив с буквами. 
Пустые клетки замените пробелами (0 => " ").

Слова размещаются в строках и столбцах, но не в диагоналях. Кроссворд состоит из 6 слов, каждое из 5 букв.

Открой картинку:
https://d17mnqrx9pmt3e.cloudfront.net/media/missions/media/e84d70d41ea74bc4998db2b2b83f3536/cipher-crossword.png
"""

from itertools import chain, permutations


class CipherCrossword:
    def __init__(self, crossword, words: list):
        self.crossword = crossword
        self.words = words
        self._cross_keys = {}  # Набор ключей который формируется в _is_cross_keys() и  _find_letters_cods() используется в _decoder()
        self._t_crossword = list(zip(*self.crossword))

    def _reset_cross_keys(self):
        self._cross_keys = {0: ' '}

    def _find_letters_cods(self, crosswod_rows, _words):
        for nuber, symbol in zip(chain(*crosswod_rows), chain(*_words)):
            if nuber in self._cross_keys and self._cross_keys[nuber] != symbol:
                return False
            self._cross_keys[nuber] = symbol
        return True

    def _is_cross_keys(self, combo_words):
        self._reset_cross_keys()
        if not self._find_letters_cods(self.crossword[::2], combo_words[:3]):
            return False
        if not self._find_letters_cods(self._t_crossword[::2], combo_words[3:]):
            return False
        return True

    def _decoder(self):
        return [[self._cross_keys[item] for item in row] for row in self.crossword]

    def decipher_crossword(self):
        for combo_words in permutations(self.words, 6):
            if self._is_cross_keys(combo_words):
                return self._decoder()


def checkio(crossword, words):
    ciphercrossword = CipherCrossword(crossword, words)
    return ciphercrossword.decipher_crossword()


if __name__ == "__main__":
    assert checkio(
        [
            [21, 6, 25, 25, 17],
            [14, 0, 6, 0, 2],
            [1, 11, 16, 1, 17],
            [11, 0, 16, 0, 5],
            [26, 3, 14, 20, 6],
        ],
        ["hello", "habit", "lemma", "ozone", "bimbo", "trace"],
        # ["hello", "bimbo", "trace", "habit", "lemma", "ozone"],
    ) == [
               ["h", "e", "l", "l", "o"],
               ["a", " ", "e", " ", "z"],
               ["b", "i", "m", "b", "o"],
               ["i", " ", "m", " ", "n"],
               ["t", "r", "a", "c", "e"],
           ]
