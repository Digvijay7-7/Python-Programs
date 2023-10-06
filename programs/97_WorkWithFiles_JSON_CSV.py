'''
The following dictionary:
stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

save to stocks.json using the json package. Set the indent to 4.

File stocks.json after saving:
{
    "PLW": [
        "Playway",
        350
    ],
    "BBT": [
        "Boombit",
        22
    ]
}
'''
import json

stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}
with open('programs/stocks.json', 'w') as file:
    json.dump(stocks, file, indent=4)