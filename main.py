import itertools
import math
from scipy.misc import derivative

# Funkcja
def f(x):
    return math.atan(math.log(x**5 + 3) - 7)


# Pochodna funkcji
def d(x):
    return derivative(f, x, dx=1e-6)


# Warunki algorytmu newtona-rhapsena
def warunki(a, b):
    fa = f(a)
    fb = f(b)
    da = d(a)
    db = d(b)
    return fa * fb < 0 and da * db > 0


def newton_rhapsen(a, b, e, limit):
    if not warunki(a, b):
        print('Funkcja nie spelnia zalozen!')
        return
    counter = 1
    condition = True
    x0 = a
    lines = []
    lines.append("============== METODA NEWTONA")
    while condition:
        if d(x0) == 0:
            break
        x1 = x0 - f(x0) / d(x0)
        line = f'{counter} - {x1} - {f(x1)}'
        print(line)
        lines.append(line)
        x0 = x1
        condition = math.fabs(f(x1)) > e
        counter += 1
        if counter > limit:
            print('Uzyskano limit petli do wykonania')
            return
    line = f'--------- Wykonano {counter} interacji, Szukany pierwiastek to {x1}'
    print(line)
    lines.append(line)
    return lines


def bisekcja(a, b, e, limit):
    if f(a) * f(b) >= 0:
        print('Funkcja nie spelnia warunku bisekcji')
        return
    # Dzielmy przedzial [a,b] na przedzialy [a, xn], [xn, b]
    an = a
    bn = b
    counter = 1
    condition = True
    lines = []
    lines.append("============== METODA BISEKCJI")
    while condition:
        xn = (an + bn) / 2
        fxn = f(xn)
        if fxn == 0.0:
            line = f'Wykonano {counter} interacji, Szukany pierwiastek to {xn}'
            print(line)
            lines.append(line)
            return lines
        if f(an) * fxn < 0:
            bn = xn
        if f(bn) * fxn < 0:
            an = xn
        line = f'{counter} - {xn} - {f(xn)}'
        print(line)
        lines.append(line)
        counter += 1
        condition = math.fabs(f(xn)) > e
        if counter > limit:
            print('Uzyskano limit petli do wykonania')
            return
    line = f'Wykonano {counter} interacji, Szukany pierwiastek to {xn}'
    print(line)
    lines.append(line)
    return lines


def euler(a, b, e, limit):
    counter = 0
    condition = True
    lines = []
    lines.append("============== METODA EULERA")
    while condition:
        counter += 1
        fa = f(a)
        fb = f(b)
        if fa - fb == 0:
            break
        xn = (fa * b - fb * a) / (fa - fb)
        fxn = f(xn)
        if fxn == 0:
            break
        a = b
        b = xn
        condition = math.fabs(fxn) < e or math.fabs(xn - b) < e
        line = f'{counter} -  {xn} - {f(xn)}'
        print(line)
        lines.append(line)
        if counter > limit:
            print('Uzyskano limit petli do wykonania')
            return
    line = f'Wykonano {counter} interacji, Szukany pierwiastek to {xn}'
    print(line)
    lines.append(line)
    return lines



if __name__ == '__main__':
    a, b, e, limit = 3, 5, 0.0001, 20
    print('============================== Metoda Newtona Rhapsena')
    n = newton_rhapsen(a, b, e, limit)
    print('============================== Metoda Bisekcji')
    bs = bisekcja(a, b, e, limit)
    print('============================== Metoda Eulera')
    eu = euler(a, b, e, limit)
    res = list(itertools.chain(n, bs, eu))
    with open('zadanie1.txt', 'w') as f:
        f.write('\n'.join(res))
