with open("input.txt") as f:
    all_counts = []
    current_count = 0
    lines = f.readlines()
    for line in lines:
        if line == "\n":
            all_counts.append(current_count)
            current_count = 0
        else:
            current_count += int(line)
    all_counts.sort(reverse=True)
        
    print("The elves with the top three calorie counts are carrying a total of " + str(all_counts[0] + all_counts[1] + all_counts[2]))