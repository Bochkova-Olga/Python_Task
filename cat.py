<<<<<<< HEAD
class Cat:
    def __init__(self, name='', gender='', age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def init_from_dict(self, cat_dict):
        self.name = cat_dict.get("name")
        self.gender = cat_dict.get("gender")
        self.age = cat_dict.get("age")

# cat = Cat(name='Сэм', gender='мальчик', age='2')
# print("имя:", cat.name)
# print("пол:", cat.gender)
=======
class Cat:
    def __init__(self, name='', gender='', age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def init_from_dict(self, cat_dict):
        self.name = cat_dict.get("name")
        self.gender = cat_dict.get("gender")
        self.age = cat_dict.get("age")

# cat = Cat(name='Сэм', gender='мальчик', age='2')
# print("имя:", cat.name)
# print("пол:", cat.gender)
>>>>>>> 93a14e9b1156d537ac9f4c870d81e5ae14463e7a
# print("возраст:", cat.age)