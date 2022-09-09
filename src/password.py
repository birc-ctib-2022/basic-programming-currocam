import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
it_has_lower, it_has_upper, it_has_number, it_has_special_char = False, False, False, False
# Do all the requirement checks here.
for c in password:
    if not it_has_lower: it_has_lower = c.islower()
    if not it_has_upper: it_has_upper = c.isupper()
    if not it_has_number: it_has_number = c.isnumeric()
    if not it_has_special_char: it_has_special_char = c in ["$", "#", "@"]

is_valid = all([it_has_lower, it_has_upper, it_has_number, it_has_special_char])
print(is_valid)
