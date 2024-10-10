
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = ['False', 34.56, (3, 2, 1)]
values_dist = {'a': 35, 'b': 'Банан', 'c': False}
print_params(*values_list)
print_params(**values_dist)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)