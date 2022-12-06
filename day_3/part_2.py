def find_priority(line_1, line_2, line_3):
    for letter in line_1:
        if letter in line_2 and letter in line_3:
            if letter.isupper():
                return ord(letter) - 38
            else:
                return ord(letter) - 96


with open("input.txt") as f:
    i = 0
    total = 0
    lines = f.readlines()
    length = len(lines)
    while i < length:
        total += find_priority(lines[i], lines[i + 1], lines[i + 2])
        i += 3
    print("Your total priority is " + str(total) + "!")

