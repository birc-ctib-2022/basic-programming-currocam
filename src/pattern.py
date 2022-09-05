
# Print the pattern
from itertools import chain
concatenated = chain(range(1, 6), range(4, 0, -1))
for i in concatenated:
    print("*"*i)
