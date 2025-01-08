import csv
import numpy as np

# File paths
input_file_path = "sales_tracker.csv"
output_file_path = "sales_summary.csv"

# Function to calculate metrics and write results to a new CSV file
def calculate_and_write_summary():
    try:
        # Load data from the CSV file
        data = []
        with open(input_file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = row["Product"]
                region = row.get("Region", "Unknown")  # Default region if not present
                revenue = float(row["Total"])
                data.append((product, revenue, region))
        
        # Convert data to a structured NumPy array
        structured_data = np.array(data, dtype=[("Product", "U50"), ("Revenue", "f8"), ("Region", "U50")])
        
        # Calculate total revenue for each product
        unique_products = np.unique(structured_data["Product"])
        product_revenue = {product: np.sum(structured_data["Revenue"][structured_data["Product"] == product]) for product in unique_products}
        
        # Calculate the product with the highest revenue
        max_revenue_index = np.argmax(structured_data["Revenue"])
        highest_revenue_product = structured_data[max_revenue_index]
        
        # Calculate total revenue by region
        unique_regions = np.unique(structured_data["Region"])
        revenue_by_region = {region: np.sum(structured_data["Revenue"][structured_data["Region"] == region]) for region in unique_regions}
        
        # Write results to a new CSV file
        with open(output_file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Product", "Total Revenue", "Region"])
            for product, revenue in product_revenue.items():
                for region in unique_regions:
                    region_revenue = np.sum(
                        structured_data["Revenue"][
                            (structured_data["Product"] == product) & (structured_data["Region"] == region)
                        ]
                    )
                    if region_revenue > 0:  # Include only if revenue exists for this region
                        writer.writerow([product, region_revenue, region])
        
        print("Summary written to", output_file_path)
        print(f"Product with the Highest Revenue: {highest_revenue_product['Product']} (${highest_revenue_product['Revenue']:.2f})")
        print("Revenue by Region:", revenue_by_region)
    
    except FileNotFoundError:
        print("Error: Input file not found.")
    except KeyError as e:
        print(f"Error: Missing expected column in input file - {e}")

# Example Usage
if __name__ == "__main__":
    calculate_and_write_summary()
