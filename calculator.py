import requests

def calculator( miles, returnTrip, costOfOwnership, gas, orderPrice ):
    '''
    '''
    totalMilesPerYear = 50000

    costPerMile = costOfOwnership / totalMilesPerYear

    coverCostNoReturn = miles * costPerMile
    coverCostWithReturn = ( miles * 2 ) * costPerMile
    profitNoReturn = coverCostNoReturn - orderPrice
    profitWithReturn = coverCostWithReturn - orderPrice

    retVal = [coverCostNoReturn, coverCostWithReturn, profitNoReturn, profitWithReturn]  
    return retVal

def main():
    miles = 7
    returnTrip = False
    costOfOwnership = 31907
    gasPerG = 3.25
    orderPrice = 10
    result = calculator( miles, returnTrip, costOfOwnership, gasPerG, orderPrice )
    print ("printing from calculator.main(): ", result)
    return result
