# 1. Write a for loop that prints squares of numbers from 1 to 10.
for i in range(1, 11):
    print(f"Square of {i} is {i**2}")

print()  
# 2. Create a list of 5 words and output the length of each word.
words = ["house", "kbtu", "dog", "date", "Incomprehensibilities"]
for word in words:
    print(f"The word '{word}' has {len(word)} characters.")

print()  

# 3. Use nested loops to output the multiplication table from 1 to 5.
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()  
