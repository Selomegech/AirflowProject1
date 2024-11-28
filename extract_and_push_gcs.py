import requests
import csv
try:
    from google.cloud import storage
    print("Import successful!")
except ImportError as e:
    print(f"Import failed: {e}")

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
        
       
        # Iterate over the rates dictionary and write each row
        for currency, rate in data['rates'].items():
            writer.writerow(['EUR', currency, rate, data['date']])

    print(f"Data successfully written to {csv_file}")
    # Upload the CSV file to Google Cloud Storage

    client = storage.Client()
    bucket = client.bucket('exchange_rates_bucket-1')
    blob = bucket.blob(csv_file)
    blob.upload_from_filename(csv_file)
    print(f"File {csv_file} uploaded to {bucket.name}.")
else:
    print(f"Failed to retrieve data: {response.status_code}") 