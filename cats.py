from cat import Cat

cats = [
    {
     "name": "\nСэм",
     "gender": "мальчик",
     "age": 2,
    },
    {
     "name": "\nНюша",
     "gender": "девочка",
     "age": 7,
    },
{
     "name": "\nКеша",
     "gender": "мальчик",
     "age": 10,
    },
]

for cat in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(cat)
    print(cat_obj.name, cat_obj.gender, cat_obj.age)
    # print(cat_obj.name)
    # print(cat_obj.gender)
    # print(cat_obj.age)
