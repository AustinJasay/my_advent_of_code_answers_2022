def calculate_points(opponent, player):
    points = 0
    if player == "X":
        points += 1
        if opponent == "A":
            points += 3
        elif opponent == "C":
            points += 6            
    elif player == "Y":
        points += 2
        if opponent == "A":
            points += 6
        elif opponent == "B":
            points += 3
    else:
        points += 3
        if opponent == "B":
            points += 6
        elif opponent == "C":
            points += 3
    return points

with open("input.txt") as f:
    total = 0
    lines = f.readlines()
    for line in lines:
        total += calculate_points(line[0], line[2])
    print("Following this playbook will end with you having " + str(total) + " points")
