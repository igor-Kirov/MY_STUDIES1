
def dat_kod(nom):
    list_pas = []
    str_pas = ''
    for i in range(1, nom):
        for y in range(i, nom):
            if i != y and nom % (i + y) == 0:
                str_pas += str(i) + str(y)
                list_pas.append(f'{i} + {y}')
    return str_pas, list_pas



x = int(input('Введите число 3 - 20: '))
if x <3 or x>20:
    print(f'Число {x} за границей')
else:
    x1, x2 = dat_kod(x)
    print(f'Для {x} - {x1}')
