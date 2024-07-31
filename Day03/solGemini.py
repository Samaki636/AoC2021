with open("input01.txt", "r") as infile:
    report = [line.strip() for line in infile]
    reportWidth = len(report[0])
    reportLength = len(report)

    colSums = [sum(int(bit) for bit in col) for col in zip(*report)]

    gammaRate = "".join(["1" if col > reportLength / 2 else "0" for col in colSums])
    epsilonRate = "".join(["0" if bit == "1" else "1" for bit in gammaRate])

    print(int(gammaRate, 2) * int(epsilonRate, 2))
