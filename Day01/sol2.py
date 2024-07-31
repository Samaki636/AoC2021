with open("input02.txt", "r") as infile:
    firstNum = int(infile.readline())
    secondNum = int(infile.readline())
    thirdNum = int(infile.readline())
    lastSum = firstNum + secondNum + thirdNum
    count = 0
    for line in infile:
        firstNum = secondNum
        secondNum = thirdNum
        thirdNum = int(line)
        currentSum = firstNum + secondNum + thirdNum
        if currentSum > lastSum:
            count += 1
        lastSum = currentSum
    print(count)
