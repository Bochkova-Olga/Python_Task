<<<<<<< HEAD
from dog import Dog

dogs = [
    {
        "name": "\nФеликс",
        "gender": "мальчик",
        "age": 2
    },
    {
        "name": "\nМухтар",
        "gender": "мальчик",
        "age": 0
    },
    {
        "name": "\nРичард",
        "gender": "мальчик",
        "age": 1
    },
]
for dog in dogs:
    dog_obj = Dog()
    dog_obj.init_from_dict(dog)
    print(dog_obj.name)
    print(dog_obj.gender)
    print(dog_obj.age)


=======
from dog import Dog

dogs = [
    {
        "name": "\nФеликс",
        "gender": "мальчик",
        "age": 2
    },
    {
        "name": "\nМухтар",
        "gender": "мальчик",
        "age": 0
    },
    {
        "name": "\nРичард",
        "gender": "мальчик",
        "age": 1
    },
]
for dog in dogs:
    dog_obj = Dog()
    dog_obj.init_from_dict(dog)
    print(dog_obj.name)
    print(dog_obj.gender)
    print(dog_obj.age)


>>>>>>> 93a14e9b1156d537ac9f4c870d81e5ae14463e7a
