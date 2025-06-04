for i in range(2,21,2):
    print (i)


print ( 'drugoi method: ')
for i in range (2,21):
    if i % 2 == 0:
        print (i, end = ' ')

print()

answer = 0
for i in range (1, 51):
    if i % 3 == 0:
        answer +=i
print('sum = ', answer)

while True:
    password = input("Введите пароль: ")
    if password == "admin123":
        print("pass")
        break  # выйти из цикла
    else:
        print("Неверный пароль.")
