
# Print the numbers described in the exercise
numbers = [str(n) for n in range(1, 11)]
for i, v in enumerate(numbers):
    print(*numbers[0:i+1])
# Just one loop
# numbers = list()
# for n in enumerate(range(1, 11)):
#     numbers.append(n)
#     print(*numbers[0:i+1])
