def isprime(x):
    sq = int(x**0.5)  #Стандартная функция для определения простоты числа. У каждого составного числа есть делитель до
    for i in range(2,sq+1):                                                                    #Его квадратного корня.
        if x%i==0:      #Перебираем числа в диапазоне от 2 до целой части квадратного корня. Делаем проверку на делимость
            return False  # Нашли делитель - число не простое.
    return x>1 #Если мы делитель не нашли, то мы проверяем, является ли число единицей. Если является - то число не простое
#------------------------------------------------------------------------------------------------------------------------------
k = 0 #количество чисел
for x in range(500000,650001):  # Перебираем числа в нашем диапазоне.
    sq = int(x ** 0.5)  # Целая часть квадратного корня числа
    d = set()  # Множество, куда мы будем забивать делители. Множество потому-что в нем не может быть повторений.
    if isprime(x):  # В угоду времени пропускаем простые числа.
        continue
    for i in range(2, sq + 1):  # Перебираем делители.
        if x % i == 0:  # Если мы нашли таковые, то добавляем 2 числа. Само i и x // i в пару.
            d.add(i)
            d.add(x // i)
    aa = [x for x in d if isprime(x)] # Распределяю множество d по двум спискам: в первом только простые
    bb = [x for x in d if not isprime(x)] # во втором только составные
    if len(bb) / len(aa) == 12: #Если длина списка составных чисел отличается от длины списка простых чисел в 12 раз
        k+=1                    #То прибавляем к количеству чисел единицу и выводим последний в отсортрованном списке делитель
        print(k,sorted(d)[-1])