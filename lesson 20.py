import random
b=random.randint (1,100)
a=int(input("угадайте число"))
while b!=a:
    if b>a:
        print("мое число больше")
    else:
        print("мое число меньше")
    a=int(input("угадайте число"))
else:
    print("молодец, угадал!")
