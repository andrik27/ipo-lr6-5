import random #модуль рандом
arr = [random.randint(-50,50) for i in range (25)] #список в промежутке от -50 до 50, размером 25 элементами

polozit = 0 #Счетчик
otric = 0 #Счетчик
null = 0 #Счетчик
min = 50 #Минимальное значение
max = -50 #Максимальное значение 

arr_polozit = list() #Создание списка
arr_otric = list() #Создание списка
arr_null = list() #Создание списка

for e in arr: #Цикл
    if e > 0: #Проверка условия
        polozit += 1 #Счетчик
        arr_polozit.append(e) #Добавляет элемент в список
    elif e < 0: #Проверка условия
        otric = 1 #Счетчик
        arr_otric.append(e) #Добавляет элемент в список

    else:
        null += 1 #Счетчик
        arr_null.append(e) #Добавляет элемент в список


print("Количество нулей: ",null, "Процент от общего количества: ",null/25*100) #Вывод на экран
print(arr_null) #Вывод на экран

print("Количество положительных чисел: ",polozit, "Процент от общего количества: ",polozit/25*100) #Вывод на экран
print(arr_polozit) #Вывод на экран

print("Количество отрицательных чисел: ",otric, "Процент от общего количества: ",otric/25*100) #Вывод на экран
print(arr_otric) #Вывод на экран

for i in range(25): #Цикл
    if arr[i] > max: #Проверка условия
        max = arr[i] #Максимальный элемент
    if arr[i] < min: #Проверка условия
        min = arr[i] #Минимальный элемент

print("Минимальный элемент = ",min) #Вывод на экран
print("Максимальный элемент = ",max) #Вывод на экран