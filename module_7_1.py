import os.path

class Product:
    def __init__(self,name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __fale_name = 'products.txt'
    file_support = ''
    def get_products(self):
        if os.path.isfile('products.txt'):
            file = open(self.__fale_name, 'r')
            file_support = file.read()
            file.close()
            return file_support
        else:
            print(f'Нет файла <{self.__fale_name}>, будет создан.')
            file = open(self.__fale_name, 'w')
            file.close()
            file = open(self.__fale_name, 'r')
            file_support = file.read()
            file.close()
            return file_support

    def add_products(self, product):
        if isinstance(product, Product):
            file = open(self.__fale_name, 'a')
            file.write(str(product)+'\n')
            file.close()
        return True

    def add(self, *products):
        shop_support = self.get_products()
        for i in products:
            #print(i)
            if isinstance( i, Product):
                if i.name in shop_support:
                    print(f'Продукт {str(i)} уже есть в магазине')
                else:
                    self.add_products(i)



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

