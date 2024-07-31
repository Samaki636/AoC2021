with open("input02.txt", "r") as infile:
    x = 0
    y = 0
    for line in infile:
        direction, stepsN = line.split()
        match direction:
            case "forward":
                x += int(stepsN)
            case "down":
                y += int(stepsN)
            case "up":
                y -= int(stepsN)
    print(x * y)
