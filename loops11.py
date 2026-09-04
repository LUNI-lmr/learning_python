text = str(input("Type a sentence: ").lower())

vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"The sentence has {count} vowels.")
