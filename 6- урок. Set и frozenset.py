        #Типы Данных (set)
    #Пример 1.1 (Удаление дубликатов с помощю "Set")
# a = [1,2,3,4,5]
# b= [3,4,5,6,7,]
# c= b+a
# # print(c)
# print(set(c))       #"set{}" - удаляет дубликаты и перемещает список. И обозначается фигурной скопкой "{}"

#   #Пример 1.2 Обозначение фигурной скопкой "{}"
# students = {"Nurbolot", "Aibala", "Kylychbek", "Baiastan","Nurbolot", "Aibala"}
# print(sudents)      


#  #Пример 1.3 Проверка   "Изменяемый и неизменяемый"
# cars = {"Audi", "BMW", "Mersedes", "Lexus"}
# print(cars)
# cars.add("FIT")     #Добавление в множество
# print(cars)
# cars.remove("Audi")     #Удаление из множества
# print(cars)
# cars.pop()      #Удаляет случайный элемент из множества
# print(cars)

    #Пример 1.4 Использование Циклов
# numbers = {1,2,3,4,1,2,3,5,6,7,8,9,10,11}
# for i in numbers:
#     print(i)


    #Пример 1.5 Сортировка Sorted
# numbers = {100,2,6,1,8,32,6,23,7,1,2,4,6,8}
# print(sorted(numbers))


   #Пример 1.6 Проверка
# hello = {1,1.0,True}
# print(hello)


        #Типы Данных (frozenset)
    #Пример 1.1 
# numbers = {100,2,6,1,8,32,6,23,7,1,2,4,6,8}
# fr = frozenset(numbers)
# print(fr)
# fr.add(1000)                  #невозможно удалить или же добавить на frozenset
# print(fr)
# fr.remove(2)                  #невозможно удалить или же добавить на frozenset
# print(fr)

        #Исключение try: или ecxept ...:
           #Пример 1.1 

# try:
#     print(100/0)
# except ZeroDivisionError:
#     print("Наноль делить нельзя! Учи Матешу!")


           #Пример 1.2     
                
while True:
    a= int(input("Первое число: "))
    b= int(input("Второе число: "))
    try:
        print(a/b)
    except:
        print("ОШИБКА")
    finally:
        print("Вам меня не остановить! ")


# while True:

#     a= int(input("Первое число: "))
#     b= int(input("Второе число: "))
#     if a==0 and b==0:
#         raise NameError("Вам меня не взломать!")
#     else:
#         print(a+b)











































