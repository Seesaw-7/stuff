import sys

line = sys.stdin.readline().strip()
print(line)

lines = sys.stdin.read()
print(lines)

while True:
    line = sys.stdin.readline()
    if not line:  # Break on EOF (empty string)
        break
    print(f"Line: {line.strip()}")