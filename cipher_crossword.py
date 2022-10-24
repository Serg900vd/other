# https://py.checkio.org/ru/mission/cipher-crossword/
from itertools import chain, permutations


class CipherCrossword:
    def __init__(self, crossword, words: list):
        self.crossword = crossword
        self.words = words
        self._cross_keys = {}  # Набор ключей который формируется в _is_cross_keys и  _find_letters_cods
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
