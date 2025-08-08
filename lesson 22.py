import random
k=0
oshibka=0
vopros=1
while vopros<11:
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    popitka = 1
    print("Вопрос номер ",vopros," Попытка номер ",popitka)
    print("Сколько будет ", a , "*" , b ,"?")
    c=input()
    while not c.isnumeric():
        c=input("Вводите только числа")
    c=int(c)
    while c!=a*b:
        popitka+=1
        print("Неверно, попробуйте еще раз ")
        oshibka+=1
        print("Вопрос номер ", vopros, "Попытка номер ", popitka)
        print("Сколько будет ", a, "*", b, "?")
        c = input()
        while not c.isnumeric():
            c= input("Вводите только числа")
        c= int(c)
    else:print("Правильно")

    vopros+=1
    k+=popitka
else:print("Вы ответили на 10 вопросов за ",k, " попыток,", "ошибок сделано ", oshibka)
