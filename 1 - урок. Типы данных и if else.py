            #1) ФУНКЦИЯ INPUT(Ожидает от пользователя что-то)

                #Пример 1.1
def p1():
        name = input("Your name: ")     #Name = переменная или же сейф!     
        print("Good morning,", name)  
# p1()


        #Пример 1.2

def p2():

        a = input("Введите первую цифру: ")
        b = input("Вветиде второю цифру: ")
        print(a +b)

# p2()          


                # Типы Данных (INT-Целое число, FLOAT- Не целое число , STR-Строка, BOOL-True, False)
                # INT
def int():

        a = int(input("Введите первую цифру: "))
        b = int(input("Вветиде второю цифру: "))
        print(a+b)

# int()

                #Float

def float():    
        a = float(input("Введите первую цифру: "))
        b = float(input("Вветиде второю цифру: "))
        print(a+b)

# float()


                # STR

def str():

        a = str(input("Введите ваше имя:  "))
        b = str(input("Вветиде вашу фамилю: "))
        print("Добро пожаловать",a, b)

# str()

            # Функция "iF-если", "else-Иначе", "elif- или же"!
            # Пример 1.1

def if1():

        a = int(input("Введите первую цифру: "))
        b = int(input("Вветиде второю цифру: "))
        if a > b:
            print(a, "больше чем", b)
        else:
            print(b, "больше чем", a)

# if1()

             # Пример 1.2

def if2():

        a = int(input("Введите число: "))
        if a % 2==0:
            print("Ваша цифра четная")
        else:
            print("Ваша цифра не четная")

# if2()

print("Nurbolot")

















































