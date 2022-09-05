
# Print the numbers described in the exercise
numbers = [str(n) for n in range(1, 11)]
for i, v in enumerate(numbers):
    print(" ".join(numbers[0:i+1]))