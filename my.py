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
    total_sales = 0.0
    try:
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                total_sales += float(row["Total"])
        print(f"Total Sales: ${total_sales:.2f}")
    except FileNotFoundError:
        print("Error: Sales tracker not found. Please create it first.")
    except KeyError:
        print("Error: Missing 'Total' column in the sales tracker file.")
#Example Usage
if __name__ == "__main__":
    create_csv
    add_sale("2025-01-08", "Laptop", 2, 1200.50)
    add_sale("2025-01-09", "Mouse", 5, 25.99)   
    calculate_total_sales()



