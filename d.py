Animal = {
    'name': 'Cat',
    'age': 5,
    'food': 'Fish'
}
def get_animal_info():
    return "name: " + Animal['name'] + "\nage: " + str(Animal['age']) + "\nfood: " + Animal['food']
print(get_animal_info())