
# Print the pattern
from itertools import chain
ranges = chain(range(1, 6), range(4, 0, -1))
for i in ranges:
    print(*list("*"*i))
