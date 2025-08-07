class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

class Cat(Animal):
    def __init__(self, name, habitat, food):
        super().__init__(name, habitat)
        self.food = food

    def __str__(self):
        return "namanya " + self.name + " habitatnya di " + self.habitat + " makanannya adalah " + self.food

cat = Cat("Oyen", "darat", "ikan")
print(cat)
