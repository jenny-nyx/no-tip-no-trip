import requests

def main():
    response = requests.get("https://api.eia.gov/v2/petroleum/pri/gnd/data/?api_key=4qjDGR77OEQgq8Yhdf9qgdP9bOuSowLLDjiVXqcj/?frequency=annual&data[0]=value&facets[product][]=EPMR&facets[duoarea][]=NUS&start=2021&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000")
    print( response.json() )