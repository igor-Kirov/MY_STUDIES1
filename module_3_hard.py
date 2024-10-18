data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


glob_str = []


def to_str(data):
    global glob_str
    #print(type(data))
    if type(data) == list:
        #print(*data)
        glob_str += data
    elif type(data) == dict:
        #print(*data.keys())
        #print(*data.values())
        for key_, value_ in data.items():
            glob_str.append(key_)
            if isinstance(value_, list | tuple | set):
                for i in value_:
                    glob_str.append(i)
            else:
                glob_str.append(value_)
    elif type(data) == tuple:
        #print(*data)
        for z in data:
            glob_str.append(z)
    else:
        #print(data)
        glob_str.append(data)


def exist_dat(data):
    len_ = len(data)
    if len_ > 0:
        for i in range(len(data)):
            if type(data) == dict:
                if i == 0:
                    to_str(data)
            else:
                dat = data[i]
                if type(dat) == dict:
                      to_str(dat)
                elif isinstance(dat, list | tuple | set):
                    for y in dat:
                        if isinstance(y, list | tuple | dict | set):
                            exist_dat(y)
                        else:
                            to_str(y)
                else:
                    to_str(dat)


def sum_do(data_str):
    exist_dat(data_structure)
    sum_str = 0
    sum_s = 0
    sum_n = 0

    for y in data_str:
        if type(y) == int:
            sum_n += y
        elif type(y) == str:
            for z in y:
                if str(z).isnumeric():
                    sum_n += int(z)
            sum_s += len(y)
    sum_str = sum_s + sum_n
#    print(sum_str, '=', sum_s, ' +', sum_n)
    print('Без учета 2 в слове "Urban2":', sum_str-2)
    print('C учета 2 в слове "Urban2":', sum_str)
    return sum_str



#exist_dat(data_structure)
print(sum_do(glob_str))
#print(glob_str)

