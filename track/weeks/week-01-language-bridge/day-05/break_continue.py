# Problem 4: Break and Continue Demo

# Read count of numbers to process
n = int(input())

# Read threshold limit (skip processing if value exceeds threshold using continue, stop entirely if negative using break)
for i in range(n):
    num = int(input())
    if num < 0:
        print("Negative number encountered, breaking loop.")
        break
    if num % 2 != 0:
        print(f"Skipping odd number {num} using continue.")
        continue
    print(f"Processing even number: {num}")
