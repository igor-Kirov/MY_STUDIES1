my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
nom = int(-1)
while nom < len(my_list):
    nom += 1
    if my_list[nom] < 0:
        break
    elif my_list[nom] == 0:
        continue
    else:
        print(my_list[nom])
