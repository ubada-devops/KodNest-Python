# Read the number and word
n = int(input())
word = input().strip()

# Print the number sequence
print("Numbers:")
for i in range(1, n + 1):
    print(i)

# Print the characters
print("Characters:")
for character in word:
    print(character)
