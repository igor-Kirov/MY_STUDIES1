class House:
    def __init__(self, name, nomber_floor):
        self.name = name
        self.nomber_of_floor = nomber_floor

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.nomber_of_floor:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor+1):
                print(i)
    def __len__(self):
        return self.nomber_of_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.nomber_of_floor}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))