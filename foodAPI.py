import requests

def lookup_food(barcode):
	url = f"https://world.openfoodfacts.net/api/v2/product/{barcode}.json"

	headers = {
		"User-Agent": "PythonPracticeApp - Educational Project - Version 1.0"
	}

	try:
		response = requests.get(url, headers=headers, timeout=5)
		response.raise_for_status()
		data = response.json()

		if "product" in data and data["product"]:
			product = data["product"]

			name = product.get("product_name" or product.get("product_name_fr") or  "Unknown Product")
			brand = product.get("brands", "Unknown Brand")

			nutrients = product.get("nutriments", {})
			calories = nutrients.get("energy-kcal_100g", nutrients.get("energy-kcal", "N/A"))

			print(f"\nFound: {name} ({brand})")
			print(f"Calories per 100g: {calories} kcal")

		else:
			print("\nProduct not found in the database. Check the barcode.")

	except requests.exceptions.RequestException as e:
		print(f"\nNetwork error: {e}\n")

if __name__ == "__main__":
	code = input("Enter product barcode: ").strip()
	lookup_food(code)
