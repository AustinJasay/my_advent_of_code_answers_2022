def find_priority(line):
    length = int(len(line) / 2)
    part_1 = line[:length]
    part_2 = line[length:]

    for letter in part_1:
        if letter in part_2:
            if letter.isupper():
                return ord(letter) - 38
            else:
                return ord(letter) - 96


with open("input.txt") as f:
    total = 0
    lines = f.readlines()
    for line in lines:
        total += find_priority(line.rstrip("\n"))
    print("Your total priority is " + str(total) + "!")

