# Функция для сложения двух чисел
def add(a, b):
    return a + b

# Функция для вычитания двух чисел
def subtract(a, b):
    return a - b

# Функция для умножения двух чисел
def multiply(a, b):
    return a * b

# Функция для деления двух чисел
def divide(a, b):
    # Проверка деления на ноль
    if b == 0:
        return "Ошибка: деление на ноль"
    else:
        return a / b

# Функция для вычисления процента от числа
def percentage(number, percent):
    return (number * percent) / 100

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Вычисление процента от числа")

# Ввод операции
choice = input("Введите номер операции (1/2/3/4/5): ")

if choice in ['1', '2', '3', '4']:
    # Ввод двух чисел
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if choice == '1':
        print("Результат сложения:", add(num1, num2))
    elif choice == '2':
        print("Результат вычитания:", subtract(num1, num2))
    elif choice == '3':
        print("Результат умножения:", multiply(num1, num2))
    elif choice == '4':
        print("Результат деления:", divide(num1, num2))
elif choice == '5':
    # Ввод числа и процента
    number = float(input("Введите число: "))
    percent = float(input("Введите процент: "))

    print("Результат вычисления процента:", percentage(number, percent))
else:
    print("Некорректный ввод")
