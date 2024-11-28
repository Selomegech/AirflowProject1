import requests
import csv

url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/2019-10-17"

querystring = {"from": "USD", "to": "EUR,GBP"}

headers = {
    "x-rapidapi-key": "f364dc4745msheef6c623373cfb8p1223acjsnd545d39b044e",
    "x-rapidapi-host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json()
    csv_file = 'historical_currency.csv'
    
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header for the rates
        # writer.writerow(['Base', 'Currency', 'Rate', 'Date'])
        
        # Iterate over the rates dictionary and write each row
        for currency, rate in data['rates'].items():
            writer.writerow(['EUR', currency, rate, data['date']])

    print(f"Data successfully written to {csv_file}")
else:
    print("Error")