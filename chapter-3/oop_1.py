# class Animal:
#     animal_name = "neko"

# neko = Animal()
# print(neko.animal_name)

class Animal:
    def __init__(animal, animal_name, animal_habitat):
        animal.animal_name = animal_name
        animal.animal_habitat = animal_habitat

    def __str__(animal):
        return animal.animal_name + " " +  animal.animal_habitat

kucing = Animal("oren", "darat")

print(kucing)
