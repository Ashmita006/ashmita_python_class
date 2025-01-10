import csv
# File path for the sales tracker
file_path = "sales_tracker.csv"
# Create a new CSV file with headers
def create_csv():
    headers = ["Date", "Product", "Quantity", "Price per unit", "Total"]
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("Sales tracker created.")
# Add a new sale record to the CSV file
def add_sale(date, product, quantity, price_per_unit):
    total = quantity * price_per_unit
    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, product, quantity, price_per_unit, total])
    print("Sale record added.")
# Calculate total sales from the CSV file
def calculate_total_sales():
    total_sales = 0
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_sales += float(row["Total"])
    print(f"Total Sales: ${total_sales:.2f}")
# Example usage
create_csv()
add_sale("2025-01-08", "Laptop", 2, 1200.50)
add_sale("2025-01-09", "Mouse", 5, 25.99)
calculate_total_sales()

#
import csv
#File path for the sales tracker
file_path = "sales_tracker.csv"
#Function to create a new CSV file with heafers
def create_csv():
    headers = ["Date","Product","Quantity","Price per unit","Total"]
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("Sales tracker created successfully.")
#Function to add a new sales record to the CSV file
def add_sale(date, product, quantity, price_per_unit):
    total = quantity * price_per_unit
    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, product, price_per_unit, total])
    print(f"Sale record for {product} added.")
#function to calculate the total sale from the CSV file
def calculate_total_sales():
    total_sales = 0
    with open(file_path, mode="r") as file:
         reader = csv.DictReader(file)
         for row in reader:
                total_sales += float(row["Total"])
    print(f"Total Sales: ${total_sales:.2f}")
#Example Usage
if __name__ == "__main__":
    create_csv
    add_sale("2025-01-08", "Laptop", 2, 1200.50)
    add_sale("2025-01-09", "Mouse", 5, 25.99)   
    calculate_total_sales() 

#
import csv
import random

sales_data_path = "sales_data.csv"
summary_data_path = "sales_summary.csv"

def create_csv():
    headers = ["Product", "Region", "Sale", "Price", "Total"]
    with open(sales_data_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("Sales tracker created.")

def add_sale(product, region, sale, price):
    total = sale * price
    with open(sales_data_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([product, region, sale, price, total])
    print("Sale record added.")

def generate_random_sales_data(num_records):
    products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Mouse"]
    regions = ["Pokhara", "Kathmandu", "Birgunj", "Illam"]

    for _ in range(num_records):
        product = random.choice(products)
        region = random.choice(regions)
        sales = random.randint(10, 500)  # Random units sold
        price = round(random.uniform(10.0, 2000.0), 2)  # Random price
        add_sale(product, region, sales, price)

    print(f"Generated {num_records} random sales records.")

def analyze_sales_data():
    sales_data = []
    # Read data from the sales CSV
    with open(sales_data_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Sale"] = int(row["Sale"])
            row["Price"] = float(row["Price"])
            row["Total"] = float(row["Total"])
            sales_data.append(row)

    # Calculate metrics using NumPy
    revenue = np.array([row["Total"] for row in sales_data])
    average_revenue = np.mean(revenue)
    product_revenue_map = {}
    region_revenue_map = {}

    for row in sales_data:
        product = row["Product"]
        region = row["Region"]
        product_revenue_map[product] = product_revenue_map.get(product, 0) + row["Total"]
        region_revenue_map[region] = region_revenue_map.get(region, 0) + row["Total"]

    product_with_highest_revenue = max(product_revenue_map, key=product_revenue_map.get)

    # Write the summary to a new CSV
    with open(summary_data_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Product", "Total Revenue", "Region"])
        for row in sales_data:
            writer.writerow([row["Product"], row["Total"], row["Region"]])

    # Output results
    print("\nAnalysis Summary:")
    print(f"Average Revenue: ${average_revenue:.2f}")
    print(f"Product with Highest Revenue: {product_with_highest_revenue} (${product_revenue_map[product_with_highest_revenue]:.2f})")
    print("Total Revenue by Region:")
    for region, revenue in region_revenue_map.items():
        print(f" - {region}: ${revenue:.2f}")

# Create the CSV file and add random sales data
create_csv()
generate_random_sales_data(1000)

# Analyze the sales data
analyze_sales_data()
