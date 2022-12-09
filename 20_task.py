# def sum(a, b):
#     # return a + b
# print(a + b)
#
# def say_hello(name):
#     return f"Hello {name}"
#
# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"
#
# def greet_bob(greeter_func):
#     return greeter_func("Bob")


# def parent():
#     print("Printing from the parent() function")
#
#     def first_child():
#         print("Printing from the first_child() function")
#
#     def second_child():
#         print("Printing from the second_child() function")
#
#     second_child()
#     first_child()
# parent()

# Printing from the parent() function
# Printing from the second_child() function
# Printing from the first_child() function


# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
#
# # Printing from the parent() function
# # Printing from the second_child() function
# # Printing from the first_child() function



# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     if num == 1:
#         return (first_child)
#     else:
#         return (second_child)
#
# # /PS D:\Цифровые профессии\Модуль 11\11_Module_Python\PetFriendsApiTests> cd 20_modul
# # PS D:\Цифровые профессии\Модуль 11\11_Module_Python\PetFriendsApiTests\20_modul>
# # python3 -m pytest 20_1_task.py

# def custom_func(num):
#     print("Calling function")

#
# def parent():
#     print("Printing from the parent() function")
#
#     def first_child():
#         print("Printing from the first_child() function")
#
#     def second_child():
#         print("Printing from the second_child() function")
#
#     second_child()
#     first_child()


# def my_decorator(func):
#     def wrapper():
#         print("Начало выполнения функции.")
#         func()
#         print("Конец выполнения функции.")
#
#     return wrapper


# def my_first_decorator():
# 	print("Это мой первый декоратор!")
#
# my_first_decorator = my_decorator(my_first_decorator)

# def working_hours(func):
#     def wrapper():
#         if 9 <= datetime.now().hour < 18:
#             func()
#         else:
#             pass  # Нерабочее время, выходим
#     return wrapper
#
# def writing_tests():
#     print("Я пишу тесты на python!")
#
# writing_tests = working_hours(writing_tests)

from decorators import do_twice

@do_twice
def test_twise():
        print("Это вызов функции test_twise!")
