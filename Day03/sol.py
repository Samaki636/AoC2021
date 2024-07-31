with open("input02.txt", "r") as infile:
    gammaRate = ""
    epsilonRate = ""
    report = [infile.readline().strip()]
    reportWidth = len(report[0])
    reportLength = 1
    colSums = []
    for _ in range(reportWidth):
        colSums.append(0)
    for line in infile:
        reportLength += 1
        line = line.strip()
        for i in range(reportWidth):
            colSums[i] += int(line[i])
    for colSum in colSums:
        if colSum / reportLength > 0.5:
            gammaRate += "1"
            epsilonRate += "0"
        else:
            gammaRate += "0"
            epsilonRate += "1"
    print(int(gammaRate, 2) * int(epsilonRate, 2))
