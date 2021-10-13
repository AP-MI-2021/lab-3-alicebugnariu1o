def get_longest_all_even(lst: list[int]):
    lg = len(lst)
    secvmax, start, end = 0, 0, 0

    for i in range(0, lg):
        if lst[i] % 2 == 0:
            st = i
            dr = i
            for j in range(i, lg):
                if lst[j] % 2 == 0:
                    dr = j
                    if dr - st + 1 > secvmax:
                        secvmax = dr - st + 1
                        start = st
                        end = dr
                else:
                    break
    listnrpare = lst[start: end + 1]
    return listnrpare


def test_get_longest_all_even():
    assert get_longest_all_even([1, 2, 4, 6, 7, 8, 9]) == [2, 4, 6]
    assert get_longest_all_even([1, 2, 3, 4, 6, 8]) == [4, 6, 8]
    assert get_longest_all_even([1, 3, 4, 5]) == [4]


test_get_longest_all_even()


def solve1():
    n = int(input("Dati nr elemente din lista: "))
    lst = []
    for i in range(0, n):
        x = int(input(f"Dati elementul de pe pozitia {i}:  "))
        lst.append(x)
    print(f"cea mai lunga secventa care are toate elementele nr pare este: {get_longest_all_even(lst)}")


def nrdivizori(n: int):
    nrdiv = 1
    for d in range(2, n + 1):
        if n % d == 0:
            nrdiv = nrdiv + 1
    return nrdiv


def get_longest_same_div_count(lst: list[int]):
    lg = len(lst)
    secvmax, start, end = 0, 0, 0

    for i in range(0, lg):
        st = i
        dr = i
        nrdivi = nrdivizori(lst[i])
        for j in range(i, lg):
            nrdivj = nrdivizori(lst[j])
            if nrdivi == nrdivj:
                dr = j
                if dr - st + 1 > secvmax:
                    secvmax = dr - st + 1
                    start = st
                    end = dr
            else:
                break
    listnrdivegali = lst[start: end + 1]
    return listnrdivegali


def test_get_longest_same_div_count():
    assert get_longest_same_div_count([10, 8, 20, 15]) == [10, 8]
    assert get_longest_same_div_count([5, 7, 11, 4]) == [5, 7, 11]
    assert get_longest_same_div_count([1, 2, 3, 4, 5]) == [2, 3]


test_get_longest_same_div_count()


def solve2():
    n = int(input("Dati nr elemente din lista: "))
    lst = []
    for i in range(0, n):
        x = int(input(f"Dati elementul de pe pozitia {i}:  "))
        lst.append(x)
    print(
        f"cea mai lunga secventa in care toate elementele au acelasi nr de divizori este: {get_longest_same_div_count(lst)}")


def get_longest_product_is_odd(lst: list[int]):
    lg = len(lst)
    secvmax, start, end = 0, 0, 0
    for i in range(0, lg):
        st = i
        dr = i
        produs = lst[i]
        for j in range(i, lg):
            produs = produs * lst[j]
            if produs % 2 == 1:
                dr = j
                if dr - st + 1 > secvmax:
                    secvmax = dr - st + 1
                    start = st
                    end = dr

    listprodusimpar = lst[start: end + 1]
    return listprodusimpar


def test_get_longest_product_is_odd():
    assert get_longest_product_is_odd([1, 2, 3, 4, 5]) == [1]
    assert get_longest_product_is_odd([1, 6, 7, 9]) == [7, 9]
    assert get_longest_product_is_odd([11, 22, 16]) == [11]


def solve3():
    n = int(input("Dati nr elemente din lista: "))
    lst = []
    for i in range(0, n):
        x = int(input(f"Dati elementul de pe pozitia {i}:  "))
        lst.append(x)
    print(
        f"cea mai lunga secventa in care toate elementele au acelasi nr de divizori este: {get_longest_product_is_odd(lst)}")


def main():
    shouldRun = True
    while shouldRun:
        nr = input("Alegeti problema pe care vreti sa o rezolvati: ")
        if nr == "1":
            print("Rezolvati problema 1: Cea mai lunga secventa de numere pare dintr o lista: \n")
            solve1()
        elif nr == "2":
            print("Rezolvati problema 2: Cea mai lunga secventa de elemente care au acelasi nr de divizori: ")
            solve2()
        elif nr == "3":
            print("Rezolvi problema 3: cea mai lunga secventa care are produsul elementelor nr.impar: ")
            solve3()
        elif nr == "x":
            shouldRun = False
        else:
            print("Ati ales optiunea gresita! Reincercati! ")


if __name__ == "_main_" :
    main()