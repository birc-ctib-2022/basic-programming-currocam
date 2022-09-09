import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]


def encode_string_into_hex(string: str) -> str:
    return "".join(hex(ord(c)) for c in string)


def decode_hex_into_string(string: str) -> str:
    hex_numbers = string.split('0x')
    return "".join(chr(int(n, base=16)) for n in hex_numbers if n)


match command:
    case "encode":
        # Implement the encoding here
        encoding = encode_string_into_hex(x)
        print(encoding)

    case "decode":
        # Implement the decoding here
        decoding = decode_hex_into_string(x)
        print(decoding)
