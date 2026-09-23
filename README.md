# barcode-nutrition-lookup

A Python command-line tool that looks up a food product by its barcode and returns the product name, brand, and calories, using the free [Open Food Facts](https://world.openfoodfacts.org/) API.

## Features

- **REST API integration** with the Open Food Facts v2 product endpoint
- **Custom User-Agent header**, following Open Food Facts' API guidelines
- **Resilient parsing:** the database is crowdsourced, so records are often incomplete. The tool falls back to the French product name when the English one is missing, and handles missing brand or calorie data
- **Error handling:** request timeout, HTTP error checking, and clear messages for network failures or unknown barcodes

## Setup and run

```
pip3 install -r requirements.txt
python3 foodAPI.py
```

## Example

```
Enter product barcode: 3017620422003

Found: Ferrero Hazelnut Chocolate Spread(Nutella)
Calories per 100g: 539 kcal
```

## Next steps

- Show more nutrients (protein, fat, sugar)
- Accept barcodes as command-line arguments
- Scan barcodes from a webcam image
