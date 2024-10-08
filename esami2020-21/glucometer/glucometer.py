import operator

'''
struttura dati: dizionario, key = codice paziente
value = codice paziente, numero superamenti, lista superamenti (lista di stringhe ora+valore)
il numero di superamenti serve per ordinare in maniera semplice (usando key di sorted)
il codice in value serve per gestire in maniera semplice la stampa
'''


def leggi_dati(file):
    SOGLIA = 200

    pazienti = {}
    for line in file:
        parti = line.strip().split()
        codice = parti[0]
        ora = parti[1]
        valore = int(parti[2])

        if valore >= SOGLIA:
            if codice not in pazienti:
                pazienti[codice] = {'cod': codice, 'n_sup': 1, 'sup': [ora + ' ' + str(valore)]}
            else:
                pazienti[codice]['n_sup'] += 1
                pazienti[codice]['sup'].append(ora + ' ' + str(valore))

    return pazienti


def main():
    file = open('glucometers.txt', 'r')
    pazienti = leggi_dati(file)
    file.close()

    lista = sorted(pazienti.values(), key=operator.itemgetter('n_sup'), reverse=True)
    for paziente in lista:
        for value in paziente['sup']:
            print(paziente['cod'], value)
        print()


main()
