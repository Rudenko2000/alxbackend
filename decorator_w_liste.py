"""dekorator zbierający w listę"""
def main():

    class ListaObiektow:
        def __init__(self):
            self.lista = []

        def dodaj_do_listy(self, funkcja):

            self.lista.append(funkcja)

            return funkcja


    widoki = ListaObiektow()


    @widoki.dodaj_do_listy
    def home(request):
        return "Witaj na stronie"


    @widoki.dodaj_do_listy
    def greet(request):
        return "Witaj, twój request to " + str(request)

    # assert home in widoki.lista
    # assert greet in widoki.lista
    # assert home(None) == "Witaj na stronie"
    # assert greet(1) == "Witaj, twój request to 1"
    print("w liste", widoki.lista[0])
    print("w module", home)
    a=bool(home==widoki.lista[0])
    print(a)
    f=home
    print(f)


if __name__ == '__main__':
    main()