import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
it_has_lower, it_has_upper, it_has_number, it_has_special_char = False, False, False, False
# Do all the requirement checks here.
for c in password:
    if (not it_has_lower) and (c.islower()):
        it_has_lower = True
    if (not it_has_upper) and (c.isupper()):
        it_has_upper = True
    if (not it_has_number) and (c.isnumeric()):
        it_has_number = True
    if (not it_has_number) and (c in ["$", "#", "@"]):
        it_has_number = True

is_valid = all([it_has_lower, it_has_upper, it_has_number, it_has_special_char])
print(is_valid)
