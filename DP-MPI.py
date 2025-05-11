from itertools import product
import time

start = time.time()

def citire_din_fisier(fisier='data.txt'):
    clauze = []
    variabile_folosite = set()
    with open(fisier, 'r') as f:
        for linie in f:
            if not linie.strip():
                continue
            tokens = linie.strip().split()
            clauza = []
            for tok in tokens:
                clauza.append(int(tok))
                variabile_folosite.add(abs(int(tok)))
            clauze.append(clauza)
    if variabile_folosite:
        nr_variabile = max(variabile_folosite)
    else:
        nr_variabile = 0
    return nr_variabile, clauze

#verifica daca o atribuire satisfice clauzele
def verifica_formula(atribuire, clauze):
    for clauza in clauze:
        gasit_adevarat = False
        for literal in clauza:
            idx = abs(literal) - 1
            val = atribuire[idx]
            if literal > 0 and val == 1:
                gasit_adevarat = True
                break
            if literal < 0 and val == 0:
                gasit_adevarat = True
                break
        if not gasit_adevarat:
            return False
    return True

#rezolva SAT prin brute-force cu numarare de pasi
def rezolva_sat_dp(nr_variabile, clauze):
    step_count = 0
    for atribuire in product([0, 1], repeat=nr_variabile):
        step_count += 1
        if verifica_formula(atribuire, clauze):
            return True, atribuire, step_count
    return False, None, step_count

if __name__ == '__main__':
    nr_variabile, clauze = citire_din_fisier()
    satisfiabil, solutie, pasi = rezolva_sat_dp(nr_variabile, clauze)
    end = time.time()

    if satisfiabil:
        print('SAT')
    else:
        print('NESAT')
    print(f'Timp executie: {end - start:.6f} secunde')
    print(f'Numar de pasi: {pasi}')
