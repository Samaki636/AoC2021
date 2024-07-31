with open("input02.txt", "r") as infile:
    oxygenRate = ""
    co2Rate = ""
    report = [line.strip() for line in infile]
    reportCopy = report.copy()
    lineLength = len(report[0])
    average = 0
    averageCopy = 0

    for i in range(lineLength):
        nLines = len(report)
        nLinesCopy = len(reportCopy)
        colSum = 0
        colSumCopy = 0
        for line in report:
            colSum += int(line[i])
        for line in reportCopy:
            colSumCopy += int(line[i])
        average = colSum / nLines
        averageCopy = colSumCopy / nLinesCopy

        if average >= 0.5:
            for j in range(len(report)-1, -1, -1):
                if (report[j][i] == "0") and len(report) > 1:
                    del report[j]
                if len(report) == 1:
                    oxygenRate = int(report[0], 2)
        else:
            for j in range(len(report)-1, -1, -1):
                if (report[j][i] == "1") and len(report) > 1:
                    del report[j]
                if len(report) == 1:
                    oxygenRate = int(report[0], 2)

        if averageCopy >= 0.5:
            for j in range(len(reportCopy)-1, -1, -1):
                if (reportCopy[j][i] == "1") and len(reportCopy) > 1:
                    del reportCopy[j]
                if len(reportCopy) == 1:
                    co2Rate = int(reportCopy[0], 2)
        else:
            for j in range(len(reportCopy)-1, -1, -1):
                if (reportCopy[j][i] == "0") and len(reportCopy) > 1:
                    del reportCopy[j]
                if len(reportCopy) == 1:
                    co2Rate = int(reportCopy[0], 2)

    print(oxygenRate * co2Rate)
