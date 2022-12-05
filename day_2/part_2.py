def calculate_points(opponent, player):
    points = 0
    if player == "X":
        if opponent == "A":
            points += 3
        elif opponent == "B":
            points += 1      
        else:
            points += 2      
    elif player == "Y":
        points += 3
        if opponent == "A":
            points += 1
        elif opponent == "B":
            points += 2      
        else:
            points += 3     
    else:
        points += 6
        if opponent == "A":
            points += 2
        elif opponent == "B":
            points += 3      
        else:
            points += 1     
    return points

with open("input.txt") as f:
    total = 0
    lines = f.readlines()
    for line in lines:
        total += calculate_points(line[0], line[2])
    print("Following this playbook will end with you having " + str(total) + " points")
