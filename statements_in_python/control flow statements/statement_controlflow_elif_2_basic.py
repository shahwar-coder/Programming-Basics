'''
1. Weather Advisor
Task:
Write a function weather_advice(temp: int) -> str that returns advice based on temperature:

temp >= 30 → "It's hot"
temp >= 20 → "It's warm"
temp >= 10 → "It's cool"
else → "It's cold"
'''

def weather_advice(temp: int) -> str:
    "Return, what the weather is"
    if temp>=30:
        return "It's hot"
    elif temp>=20:
        return "It's warm"
    elif temp>=10:
        return "It's cool"
    else:
        return "It's cold"

def main():
    # temp=32
    # temp=28
    temp=4
    print(weather_advice(temp))

if __name__=="__main__":
    main()
