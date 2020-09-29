def cash():
    '''функция генерации чисел от 45 до 54'''
    import random
    num=int(input("enter a number:"))
    cash_list=[]
    for i in range(num):
        cash_list.append(random.randint(45, 55))
    return cash_list



def bank(limit, cash):
    """функция отбора чисел из листа более указанного limit"""
    raise_list=[]
    for i in cash:
        if i>limit:
            raise_list.append(i-limit)

    return cash, raise_list, sum(raise_list)

limit=50

print(bank(limit,cash()))
