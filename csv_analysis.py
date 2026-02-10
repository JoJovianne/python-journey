import csv

file_path = "csv_data/sales.csv"

#Read CSV data
with open(file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    #Clean colum names (removespaces before/after)
    reader.fieldnames = [name.strip() for name in reader.fieldnames]
    data = list(reader)

print(reader.fieldnames)
    
#Print Row Data and Column Data
print(f"Total row: {len(data)}")
print(F"Columns: {reader.fieldnames}")

#Print for the first 5 rows
print("\nFirst 5 rows:")

for row in data[:5]:
    print(row)
    
#Basic Statistic: Total Sales Revenue for each product
sales_summary = {}
for row in data:
    product = row["Product"].strip()
    quantity = int(row["Quantity"].strip())
    price = float(row["Price"].strip())
    total = quantity * price
    if product in sales_summary:
        sales_summary[product] += total
    else:
        sales_summary[product] = total
        
print("\nSales summary per product:")
for product, total in sales_summary.items():
    print(f"{product}: ${total:.2f}")
    