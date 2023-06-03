def calculateAverage(numbersList):
    total = 0.0
    for number in numbersList:
        total = total + number 
        nElements = len(numbersList) 
        average = total / nElements 
        return average