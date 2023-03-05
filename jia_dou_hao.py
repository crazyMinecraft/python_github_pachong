with open('filename.txt', 'r') as file:
    lines = file.readlines()

with open('filename.txt', 'w') as file:
    for line in lines:
        line = line.strip() + ',\n'
        file.write(line)
