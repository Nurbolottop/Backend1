            #Типы данных " TURPLE - Кортежи "
# Отличия LIST от Turple: 
##1name.append("Nurbolot")     #Не можем добавить на Turple  
##name.append["Nurbolot"]      #Можем добавить на List


            #Пример 1.1 на "turple"

# name = ('Kurmanbek', 'Adilet')
# print(name)  



            #Пример 1.2 на "turple"

# names =('Kurmanbek', 'Nurtilek', "Nurbolot")
# print(name[1:2])

    

            # Пример 1.3 (Создать калькулятор с помощю if-else)
# a = int(input("Выберите первую цифру: "))
# v = input("Что хотите сделать:    +, -, *, /,")
# b = int(input("Выберите вторую цифру: "))
# if v == "+":
#     print(a + b)
# elif  v == "-":
#     print(a - b)
# elif v == "*":
#     print(a * b)
# elif  v == "/":
#     print(a / b)
# else:
#     print("EROR")

            # Пример 1.4 (Мини игра - Угадай цифру)
# import random

# ran = random.randint(1, 5)
# user = int(input("Угадайте цифру: "))
# if ran == user:
#     print("Вы выиграли")
#     print("Рандомное число было 2:", ran)
# else:
#     print("Вы проиграли")
#     print("Рандомное число было :", ran)


        # Пример 1.5 (Контакты 1.1)
        
contac = {'Kurmanbek': '0777876543', 'Adilet': '0556764543', 'Aibala': '0555837938'}
com = input("Меню: 1- Добавить, 2 - Удалить контакт, 3 - Посмотреть контак!")
if com == "1":
    name =  input("Введите контакт: ")
    if name in contac:
        print('Такое имя уже есть!')
    else:
        contac.append(name)
        print("Контакт",  name, "успешо добавлен!")
     
elif com == "2":
    print("Ваши контакты: ",contac)
    del1 = input("Введите имя контакта которую хотите удалить! ")
    print
    if del1 in contac:
        contac.remove(del1)
        print("Контакт", del1, "успешо удлаен.")
        
    else:
        print("Такого контакта нет!")
        print(contac)
elif com == "3":
    print(contac)
else:
    print("EROR")    


       























































































































































































