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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
