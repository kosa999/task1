# 1. Create a list of 5 numbers. Output: 1. the sum of all the numbers, 2. maximum and minimum values
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

# 2. A list of strings. Replace the second element with "updated" and display the final list.
words = ["first", "second", "third", "fourth"]
words[1] = "updated" 
print("Обновлённый список:", words)

# 2. A list of strings. Replace the second element with "updated" and display the final list.
names = ["Alizhan", "Baurzhan", "Anastasia", "Misha", "Adil"]

for name in names:
    if name.startswith("A"):
        print(name)