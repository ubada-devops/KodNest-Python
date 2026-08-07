# Problem 2: Even Sum

# Read the limit
limit = int(input())

# Initialize the loop variable and total
number = 1
total = 0

# Examine every number from 1 to limit
while number <= limit:
    if number % 2 == 0:
        total = total + number
    number = number + 1

# Display the result
print("Even Sum:", total)
