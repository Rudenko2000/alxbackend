# 3. fabryka fukncji-kluczy do sortowania

def main():

    l = ["Ala", "pies", "kot", "i tak dalej", "..."]
    l.sort(key=len)  # to by posortowało po długości
    l.sort(key=lambda x: x[1])  # to by posortowało po drugiej literze

    def fabryka_funkcji_pobierajacych_dana_litere(idx_litery):
        def sort_key(arg):
            if ((idx_litery) <= (len(arg)-1)):
                key = arg[idx_litery]
            else:
                key=arg[-1]
            # lub derugi sposob:
            # try:
            #     key=arg[idx_litery]
            # except:
            #     key=arg[-1]
            return key

        return sort_key


        # zadanie dodatkowe: jeśli jest za mało liter to podać ostatnią
    print(l)
    l.sort(key=fabryka_funkcji_pobierajacych_dana_litere(0))  # ma sortowac po pierszej literze
    print(l)
    l.sort(key=fabryka_funkcji_pobierajacych_dana_litere(5))  # ma sortowac po pierszej literze
    print(l)
    assert fabryka_funkcji_pobierajacych_dana_litere(0)("Abcd") == "A"
    assert fabryka_funkcji_pobierajacych_dana_litere(6)("Abcd") == "d"




if __name__ == '__main__':
    main()