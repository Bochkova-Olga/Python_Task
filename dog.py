<<<<<<< HEAD
class Dog:
    def __init__(self, name="", gender="", age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def init_from_dict(self, dog_dict):
        self.name = dog_dict.get("name")
        self.gender = dog_dict.get("gender")
        self.age = dog_dict.get("age")

# dog = Dog(name='Феликс', gender='мальчик', age='2')
# print("\nДанные питомца\n")
# print("Имя:", dog.name)
# print("Пол:", dog.gender)
# print("Возраст:", dog.age)
#
=======
class Dog:
    def __init__(self, name="", gender="", age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def init_from_dict(self, dog_dict):
        self.name = dog_dict.get("name")
        self.gender = dog_dict.get("gender")
        self.age = dog_dict.get("age")

# dog = Dog(name='Феликс', gender='мальчик', age='2')
# print("\nДанные питомца\n")
# print("Имя:", dog.name)
# print("Пол:", dog.gender)
# print("Возраст:", dog.age)
#
>>>>>>> 93a14e9b1156d537ac9f4c870d81e5ae14463e7a
