num = int (input("Ingresa un Numero: "))
new_list = range (1, num + 1)

for i in new_list:
    if num % i == 0:
        print(i)
