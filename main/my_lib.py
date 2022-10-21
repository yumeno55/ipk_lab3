# Функция определения n чисел Фибоначчи
# Принимает n
# Возвращает список чисел Фибонначи до n-ого
# Пример: 5 -> 1, 1, 2, 3, 5
def fib(n):
    n1 = 1
    n2 = 1
    arr = [1, 1]
    if n == 1:
        arr.pop(0)
    if n <= 0:
        arr.pop(0)
        arr.pop(0)
    i = 0
    while i < n - 2:
        sum = n1 + n2
        n1 = n2
        n2 = sum
        arr.append(n2)
        i += 1
    return arr

# Функция сортировки пузырьком
# Принимает список чисел
# Возвращает отсортированный список
# Пример: [5, 2, 4] -> [2, 4, 5]
def puzirek(a):
    N = len(a)
    i = 0
    while i < N - 1:
        j = 0
        while j < N - 1 - i:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            j += 1
        i += 1
    return a

# Калуькулятор
# Принимает 3 аргумента: число 1, число 2 и знак действия (+, -, *, /)
# Возвращает результат операции над числами
# Пример: 5, 7, '+' -> 12
def calc(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2