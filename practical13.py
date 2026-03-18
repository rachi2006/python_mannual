count = 0
with open("practical1.py", "r") as file:
    data = file.read()
    lines = data.split()
    count = len(lines)
print("Number of words in the file:", count)