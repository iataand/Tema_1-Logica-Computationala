print('Pentru rezolvarea problemei am atribuit fiecarei operatie un corespondent care poate fi accesat usor de la tastatura astfel: ')
print('si -> "&"')
print('sau -> "|"')
print('implicatie -> ">"')
print('echivalent -> "="')
print('negatie -> "!"')

formula = input(
    'Introduceti o propozitie folosind simbolurile echivalente enumerate mai sus (Ex: "((A&B)|C)=D)" ): ')


def rezolvare(formula):
    operatii = ['&', '|', '>', '=']
    paranteze = []
    contorParanteze = 0
    contorOperatii = 0

    for i in range(len(formula) - 1):

        carNext = formula[i + 1]
        carCurent = formula[i]

        if carCurent == '(':
            contorParanteze = contorParanteze + 1
            paranteze.append('(')

            if carNext in operatii or carNext == ')':
                return(f'Nu este corect deoarece avem {carCurent} urmat de {carNext}.')

        if carCurent == ')':
            contorParanteze += 1

            if paranteze == []:
                return('Nu este corect deoarece nu corespund parantezele.')
            paranteze.pop()

            if carNext.isalpha() or carNext == '!' or carNext == '(':
                return(f'Nu este corect deoarece avem {carCurent} urmat de {carNext}.')

        if carCurent.isalpha():  # daca caracterul curent este atom
            if carNext.isalpha() or carNext == '!' or carNext == '(':
                return(f'Nu este corect deoarece avem {carCurent} urmat de {carNext}.')

        if carCurent in operatii:  # daca caracterul curent este o operatie
            contorOperatii += 1

            if carNext == ')' or carNext in operatii or carNext == '!':
                return(f'Nu este corect deoarece avem {carCurent} urmat de {carNext}.')

        if carCurent == '!':
            contorOperatii += 1

            if carNext == ')' or carNext in operatii or carNext == '!':
                return(f'Nu este corect deoarece avem {carCurent} urmat de {carNext}.')

    if paranteze == ['('] and (contorParanteze + 1) / 2 == contorOperatii:
        return('Este propozitie.')
    else:
        return('Nu este corect deoarece nu corespund parantezele.')


print(rezolvare(formula))
