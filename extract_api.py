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
        
        # Write the metadata (base and date) as the first row
        writer.writerow(['Base Currency', data['base']])
        writer.writerow(['Date', data['date']])
        writer.writerow([])  # Empty row for separation
        
        # Write the header for the rates
        writer.writerow(['Currency', 'Rate'])
        
        # Iterate over the rates dictionary and write each row
        for currency, rate in data['rates'].items():
            writer.writerow([currency, rate])

    print(f"Data successfully written to {csv_file}")
else:
    print(f"Error: {response.status_code}")