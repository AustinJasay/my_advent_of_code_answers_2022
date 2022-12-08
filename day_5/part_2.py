# This one was pretty rough
# I'm sure there's a better way to do this but I'm glad I got something that works


def stacks_to_lists(lines):
    stacks = []
    for line in list(reversed(lines)):
        spaces = 0
        stack = 0
        for letter in line:
            if letter == " ":
                spaces += 1
                if spaces >= 4:
                    spaces = 0
                    stack += 1
            elif letter.isalpha():
                try:    
                    stacks[stack] += letter
                except:
                    stacks.append([letter])
                stack += 1
                spaces = 0
    return stacks

def sort_stacks(lines, stacks):
    for line in lines:
        number = ""
        from_stack = ""
        to_stack = ""
        for word in line.rstrip("\n").split(" "):
            if word.isnumeric():
                if number == "":
                    number = word
                elif from_stack == "":
                    from_stack = word
                elif to_stack == "":
                    to_stack = word
        stacks[int(to_stack) -1] += (stacks[int(from_stack) - 1][-int(number):])
        stacks[int(from_stack) - 1] = stacks[int(from_stack) - 1][:-int(number)]
    return stacks

with open("input.txt") as f:
    lines = f.readlines()
    message = ""
    i = 0
    stacks = []
    stacks = stacks_to_lists(lines[:8])
    stacks = sort_stacks(lines[10:], stacks)
    for stack in stacks:
        if len(stack) >= 1:
            message += stack[-1]
    print(message)