def check_overlap(range_1, range_2):
    if int(range_2[0]) >= int(range_1[0]) and int(range_2[1]) <= int(range_1[1]) :
        return 1
    elif int(range_1[0]) >= int(range_2[0]) and int(range_1[1]) <= int(range_2[1]):
        return 1
    else:
        return 0

with open("input.txt") as f:
    count = 0
    lines = f.readlines()
    for line in lines:
        ranges = line.rstrip("\n").split(",")
        count += check_overlap(ranges[0].split("-"), ranges[1].split("-"))
    print("There are " + str(count) + " pairs with complete overlaps")