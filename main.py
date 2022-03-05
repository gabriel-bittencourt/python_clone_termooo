from colorama import Fore, Style


class Game:

    def __init__(self, word):
        self.word = list(word)

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

        cp_word = self.word[:]

        # Pattern
        # 0 -> not in word
        # 1 -> right letter, right spot
        # 2 -> right letter, wrong spot
        patt = [0] * len_word

        att = {l : [] for l in self.word}


        for i, (l_word, l_guess) in enumerate(zip(self.word, guess)):

            # Letter is not in the word
            if l_guess not in cp_word:
                continue

            # Right letter in right spot
            if l_guess == l_word:
                patt[i] = 1

                if len(att[l_guess]) >= cp_word.count(l_guess):
                    patt[ att[l_guess].pop() ] = 0
                
                cp_word.remove(l_guess)

            # Letter in wrong spot
            else:
                if len(att[l_guess]) < cp_word.count(l_guess) :
                    patt[i] = 2

                else:
                    patt[i] = 0

                att[l_guess].append(i)


        self.show_match(guess, patt)

        return not (0 in patt or 2 in patt)


word = "ACASO"
game = Game(word)

r = False
g = ""
c = 0
while not r and not g == "0":
    g = input("{}ª tentativa: ".format(c+1)).upper()

    if len(g) != 5:
        print("Insira uma palavra de 5 letras\n")
        continue

    r = game.match(g)
    c += 1
