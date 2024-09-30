first = input("Введите первое число: ")
second = input("Введите второе число: ")
third = input("Введите третье число: ")
# print("Вы ввели числа", first, second, third)

if (first == second) and (second == third) and (first == third):
    print(3)
elif (first == second) or (second == third) or (first == third):
    print(2)
else:
    print(0)