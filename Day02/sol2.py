with open("input02.txt", "r") as infile:
    aim = 0
    x = 0
    y = 0
    for line in infile:
        direction, stepsN = line.split()
        match direction:
            case "forward":
                x += int(stepsN)
                y += aim * int(stepsN)
            case "down":
                aim += int(stepsN)
            case "up":
                aim -= int(stepsN)
    print(x * y)
