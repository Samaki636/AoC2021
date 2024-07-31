with open("input02.txt", "r") as infile:
    lastNum = int(infile.readline())
    count = 0
    for line in infile:
        currentNum = int(line)
        if currentNum > lastNum:
            count += 1
        lastNum = currentNum
    print(count)
