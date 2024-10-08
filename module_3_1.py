calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string='Яблоко'):
    count_calls()
    if string == '':
        exit
    else:
        str_tuple = (len(string), string.upper(), string.lower())
        return str_tuple


#string = 'Груша'
#list_to_search = ['Персик', 'Яблоко', 'Помидор', 'Груша', 'Вруша']
def is_contains(string = '', list_to_search = []):
    count_calls()
    bool_retur = False
    if type(list_to_search) == list:
        up_list = [s.upper() for s in list_to_search]
        sech_str = string.upper()
        # print(up_list)
        for i in up_list:
            if i == sech_str:
                bool_retur = True
                break
    return bool_retur


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)

# print(string_info('Пирожок'))
# print(string_info('Пирожок'))
# print(is_contains(string, list_to_search))
# print(calls)
