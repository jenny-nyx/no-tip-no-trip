import requests
# API KEY 4qjDGR77OEQgq8Yhdf9qgdP9bOuSowLLDjiVXqcj

def calculate( dictData ):
    orderPrice = float( dictData["orderPrice"] )
    miles = int( dictData["miles"] )
    returnTrip = False
    costOfOwnership = int( dictData["costOfOwnership"] )
    gasPerG = float( dictData["gasPrice"] )

    totalMilesPerYear = 50000

    costPerMile = costOfOwnership / totalMilesPerYear

    coverCostNoReturn = miles * costPerMile
    coverCostWithReturn = ( miles * 2 ) * costPerMile
    profitNoReturn = orderPrice - coverCostNoReturn
    profitWithReturn = orderPrice - coverCostWithReturn

    retVal = [costPerMile, coverCostNoReturn, coverCostWithReturn, profitNoReturn, profitWithReturn] 

    print ("printing from calculator.main(): ", retVal)
    return retVal
