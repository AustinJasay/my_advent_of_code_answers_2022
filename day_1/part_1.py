with open("input.txt") as f:
    highest_count = 0
    current_count = 0
    lines = f.readlines()
    for line in lines:
        if line == "\n":
            if current_count > highest_count:
                highest_count = current_count
            current_count = 0
        else:
            current_count += int(line)
        
    print("The most calories any elf has is " + str(highest_count))