
            #ФУНКЦИЯ len()
# numbers= [1,23,4,5,6,1,23,4,43,2,24,5,6,4,3,2,5,32,42,42]
# print(len(numbers))                   #Cчитает элементы в списке


            #ТИП ДАННЫХ Dick-Словари
    #Пример 1.1

# stud = {'name' : 'Adilet'}
# print(stud)

    
    #Пример 1.2
# stud = {'name' : 'Adilet', 'age': '17'}
# stud['age'] = 18
# stud["course"] = 'Python'           #Обавление в Dict
# print(stud)
# del stud['course']              #Удаление из Dict        
# print(stud)
# stud.setdefault('course', ' JavaScript')      #setdefault- добавление в Dict  
# print(stud)
# stud.pop('name')            #pop- удаление из 
# print(stud)

    #Пример 1.3
# it_run = {'name:' : ' It-run','adress:' : 'Masalieva 38', 'experience:' : '2 years' }
# # print(it_run.keys())        #keys- ключи
# # print(it_run.values())      #values-значение
# print(it_run.items())       #items-оба

# for key, value in it_run.items():
#     if key =='adress' and value =='Masalieva 38':
#         print(key,value)



 # Пример 1.5 (Контакты 1.2)

# contac = {'Kurmanbek': '0777876543', 'Adilet': '0556764543', 'Aibala': '0555837938'}
# while True:
#     com = input("Меню: 1- Добавить, 2 - Удалить контакт, 3 - Обнавить контакт, 4 - Посмотреть контак!")
#     if com =="1":
#         add_name = input("Введите имя контакта: ")
#         add_number = input("Введите номер контакта:")
#         if add_name in contac.keys():
#             print("Такой контакт уже существует!")
#         else:
#             contac.setdefault(add_name, add_number)
#             print("Контакт", add_name, "успешно добавлен!")
#     elif com =="2":
#         del_name = input("Введите имя контакта: ")
#         if del_name in contac.keys():
#             contac.pop(del_name)
#             print("Контакт", del_name, "успешно удален!")
#         else:
#             print("Контакт",del_name," не существует!")
#     elif com == "3":
#         up_name =input("Введите имя: ")
#         if up_name in contac.keys():
#             up_number = input("Введите номер:")
#             contac[up_name] = up_number
#             print("Контакт", up_name, "успешно обнавлен")
#         else:
#             print("Контакт",up_name, "не существует!")
#     elif com =="4":
#         print(contac)
#     elif com =="break":
#         print("Программа успешно остановлена ! ")
#         break
#     else:
#         print("Такая функция не существует!")













































































































































































































