for x in range(567890,568301):  # Перебираем числа в нашем диапазоне.
    sq = int(x ** 0.5)  # Целая часть квадратного корня числа
    d = set()  # Множество, куда мы будем забивать делители. Множество потому-что в нем не может быть повторений.
    for i in range(2, sq + 1):  # Перебираем делители.
        if x % i == 0:  # Если мы нашли таковые, то добавляем 2 числа. Само i и x // i в пару.
            d.add(i)
            d.add(x // i)
    d = sum(sorted(d)) #преобразую множество d в число m, суммируя все его элементы
    if d%100==0: #т.к я не могу делить на 0, я пропускаю числа, которые в конце имеют 00
        continue
    if x%(d%100)==0 and x%10!=0: #если наше число делится на 2 последние цифры числа m и не оканчивается нулем,
        print(x, d)              #к количеству прибавляю единичку
