# 1. Write a program that outputs all even numbers from 2 to 20.
for i in range(2,21,2):
    print (i)


print ( 'drugoi method: ')
for i in range (2,21):
    if i % 2 == 0:
        print (i, end = ' ')

print()
# 2. Write a program that counts the sum of all the numbers from 1 to 50 that are divisible by 3.
answer = 0
for i in range (1, 51):
    if i % 3 == 0:
        answer +=i
print('sum = ', answer)

# 3. Ask the user for the password until they enter admin123.
while True:
    password = input("Введите пароль: ")
    if password == "admin123":
        print("pass")
        break  # выйти из цикла
    else:
        print("Неверный пароль.")
