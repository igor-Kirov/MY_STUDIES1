


def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            print('Некорректный тип данных для подсчёта суммы - ', i)
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    egr = None
    rez = ()
    if isinstance(numbers, str):
        numbers = [x for x in numbers]
    try:
        rez = personal_sum(numbers)
        sum_num = rez[0]
        kol_num = len(numbers) - rez[1]
        egr = sum_num/kol_num
    except ZeroDivisionError:
        egr = 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
    finally:
        return egr



print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')