"""Funkcje i dekoratory (podstawy/zadanie_dekoratory.py)
napisać dekorator liczący czas wywołania funkcji"""
import time

def main():
    #1. dekorator liczący czas
    # w środku rozwiązania znajdzie się:
    def licznik_czasu(funkcja):
        def modofokacja_funkcji(*args,**kwargs):
            time_start = time.perf_counter()
            wynik=funkcja(*args,**kwargs)
            time_end = time.perf_counter()

            print("Wywołanie funkcji zajęło", time_end - time_start)

            return wynik
        return modofokacja_funkcji

    # def potegowanie(liczba,poteng):
    #     wynik = 1
    #     for x in range(poteng):
    #         wynik*=liczba
    #     print(f"{liczba} do potęgi {poteng} = {wynik_potegowania}")
    #     return wynik
    #
    # poteg_z_czasem=licznik_czasu(potegowanie)
    # wynik=poteg_z_czasem(2,3)

    @licznik_czasu
    def potegowanie(liczba, poteg):
        wynik = 1
        for x in range(poteg):
            wynik *= liczba
        print(f"{liczba} do potęgi {poteg} = {wynik}")
        return wynik
    wynik=potegowanie(2,2)



if __name__ == '__main__':
    main()
