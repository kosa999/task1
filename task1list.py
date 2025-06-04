numbers = [1, 2, 3, 4 ,5]
total = 0
max = -99999999999
min = 99999999999
for i in numbers:
    total+=i
    if(i<min):
        min=i
    if(i>max):
        max=i

print (total)
print (f"max value is {max} and min value is {min}")

words = ["first", "second", "third", "fourth"]
words[1] = "updated" 
print("Обновлённый список:", words)

names = ["Alizhan", "Baurzhan", "Anastasia", "Misha", "Adil"]

for name in names:
    if name.startswith("A"):
        print(name)