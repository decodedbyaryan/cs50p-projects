import sys

if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("file doesn't end in .py")

lines = 0


try:
    with open(f"{sys.argv[1]}", "r") as file:
        for line in file:
            if line.strip() == "":
                continue

            elif line.strip().startswith("#"):
                continue

            else:
                lines += 1




except FileNotFoundError:
    sys.exit("file does not exist")

print(f"total lines of code in program {lines}")