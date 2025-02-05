from tkinter.font import names


class  House:
    houses_history = []
    def __new__ (cls,*args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self,name ,floor):
            self.name = name
            self.number_of_floors = floor

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def go_to (self, new_floor):
            if 1 <= new_floor <= self.number_of_floors:
                for floor in range(1, new_floor + 1):
                    print(floor)
            else:
                print("Такого этажа не существует")

    def __len__(self):
            return self.number_of_floors

    def __str__(self):
            return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
            if isinstance(other, House):
                return self.number_of_floors == other.number_of_floors
            elif isinstance(other, int):
                return self.number_of_floors == other

    def __lt__(self, other):
            if isinstance(other, House):
                return self.number_of_floors < other.number_of_floors
            elif isinstance(other, int):
                return self.number_of_floors < other

    def  __le__(self, other):# <=
            return self. __eq__(other)


    def  __gt__(self, other):# >
            return not self.__eq__(other)

    def  __ge__(self, other):# >=
            return self.__eq__(other)

    def  __ne__(self, other):#!=
            return not self. __eq__(other)

    def __add__(self, value):
            if isinstance(value, House):
                self.number_of_floors += value.number_of_floors
            elif isinstance(value, int):
                self.number_of_floors += value
                return self

    def __radd__(self, value):
            return self.__add__(value)

    def __iadd__(self, value):
            return self.__add__(value)

h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 20)

print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)



# Удаление объектов

del h2

del h3



print(House.houses_history)

