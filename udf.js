function transform(line) {
    // Split the line into values using comma as the delimiter
    var values = line.split(',');

    // Create an object to hold the transformed data
    var obj = {
        base: values[0],       // Base currency (e.g., "EUR")
        currency: values[1],   // Currency code (e.g., "USD")
        rate: parseFloat(values[2]), // Exchange rate (converted to float)
        date: values[3]        // Date (e.g., "2019-10-17")
    };

    // Convert the object to a JSON string
    var jsonString = JSON.stringify(obj);
    return jsonString;
}
// var csvLine = "EUR,USD,1.112473,2019-10-17"; // Example CSV line
// var jsonOutput = transform(csvLine);
// console.log(jsonOutput); // {"base":"EUR","currency":"USD","rate":1.112473,"date":"2019-10-17"}