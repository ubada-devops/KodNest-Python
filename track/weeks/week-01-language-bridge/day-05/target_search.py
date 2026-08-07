# Problem 1: Target Search & Count Multiples of 3

limit = int(input())
target = int(input())

count = 0
total = 0
found = False

# Examine every number from 1 to the limit
for number in range(1, limit + 1):
    if number % 3 == 0:
        count += 1
        total += number
    if number == target:
        found = True

print("Count:", count)
print("Sum:", total)

# Display the count, total and search result
if found:
    print("Target Found: Yes")
else:
    print("Target Found: No")
