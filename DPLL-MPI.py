import time
start = time.time()

def citire_clauze(fisier='data.txt'):
    clauze = []
    with open(fisier) as f:
        for linie in f:
            linie = linie.strip()
            if not linie:
                continue
            #fiecare linie are literali separati prin spatiu
            clause = []
            for token in linie.split():
                clause.append(int(token))
            clauze.append(clause)
    return clauze

#elimina clauzele satisfacute si cele falsificate de atribuire
def simplifica(clauze, atribuire):
    nou = []
    for cl in clauze:
        #daca un literal este adevarat, sare peste clauza
        gasit = False
        for lit in cl:
            if lit in atribuire:
                gasit = True
                break
        if gasit:
            continue
        #pastreaza doar literalii care nu sunt falsi
        cl2 = []
        for lit in cl:
            if -lit not in atribuire:
                cl2.append(lit)
        nou.append(cl2)
    return nou

pasi = 0

def dpll(clauze, atribuire):
    global pasi
    pasi += 1
    clauze = simplifica(clauze, atribuire)
    #daca nu mai sunt clauze, e satisfacuta
    if not clauze:
        return True
    #daca exista clauza goala, nu se poate satisface
    for cl in clauze:
        if len(cl) == 0:
            return False

    for cl in clauze:
        if len(cl) == 1:
            lit = cl[0]
            return dpll(clauze, atribuire | {lit})
    literali = set()
    for cl in clauze:
        for lit in cl:
            literali.add(lit)
    for lit in literali:
        if -lit not in literali:
            return dpll(clauze, atribuire | {lit})

    #alege primul literal si incearca ambele valori
    lit = clauze[0][0]
    if dpll(clauze, atribuire | {lit}):
        return True
    if dpll(clauze, atribuire | {-lit}):
        return True
    return False

if __name__ == '__main__':
    clauze = citire_clauze('data.txt')
    satisfiabil = dpll(clauze, set())
    end = time.time()
    if satisfiabil:
        print('SAT')
    else:
        print('NESAT')
    print(f'Timp executie: {end - start:.6f} secunde')
    print(f'Numar de pasi: {pasi}')