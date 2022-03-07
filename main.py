from colorama import Fore, Style
import random
import unidecode
from words import selected_words, all_words


class Game:

    def __init__(self):
        self.word = random.choice(selected_words)
        self.words = all_words

    def show_match(self, word, patt):

        print()
        for l, p in zip(word, patt):
            if p == 1:
                print(Fore.GREEN + f'{l}', end=" ")
            elif p == 2:
                print(Fore.YELLOW + f'{l}', end=" ")
            else:
                print(f'{l}', end=" ")
            print(Style.RESET_ALL, end="")
        print("\n")

    def match(self, guess):

        len_word = self.word.__len__()

        # Remove accents
        d_word = unidecode.unidecode(self.word)

        cp_word = list(d_word)

        # Remove accents
        d_guess = unidecode.unidecode(guess)

        # Pattern
        # 0 -> not in word
        # 1 -> right letter, right spot (green)
        # 2 -> right letter, wrong spot (yellow)
        patt = [0] * len_word

        att = {l: [] for l in d_word}

        for i, (l_word, l_guess) in enumerate(zip(d_word, d_guess)):

            # Letter is not in the word
            if l_guess not in cp_word:
                continue

            # Right letter in right spot
            if l_guess == l_word:
                patt[i] = 1

                if len(att[l_guess]) >= cp_word.count(l_guess):
                    patt[att[l_guess].pop()] = 0

                cp_word.remove(l_guess)

            # Letter in wrong spot
            else:
                if len(att[l_guess]) < cp_word.count(l_guess):
                    patt[i] = 2

                else:
                    patt[i] = 0

                att[l_guess].append(i)

        self.show_match(guess, patt)

        return patt

    def check(self, pattern):
        return not (0 in pattern or 2 in pattern)

    def loop(self):
        correct = False
        count = 1
        guess = ""

        while (not correct) and (guess != "0") and (count < 7):
            guess = input(f"{count}ª tentativa: ").upper()

            if len(guess) != 5:
                print("Insira uma palavra de 5 letras\n")
                continue

            if guess not in self.words:
                print("Palavra inválida\n")
                continue

            patt = game.match(guess)
            correct = game.check(patt)
            count += 1

        if count == 7:
            print(f"Palavra correta era: {self.word}")


if __name__ == "__main__":
    game = Game()
    game.loop()
