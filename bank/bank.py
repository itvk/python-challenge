import csv

file_to_load = r"C:\Users\kevin\Documents\GitHub\python-challenge\bank\budget_data.csv"
file_to_output = r"C:\Users\kevin\Documents\GitHub\python-challenge\bank\budget.txt"
total_months = 0
revenue = 0
monthchange = []
revenue_changed = []
greatest = ["", 0]
greatestdecrease = ["", float('inf')]
total_revenue = 0

with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)
    print(reader.fieldnames)
    for row in reader:
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])  # Update this line
        revenue_change = int(row["Profit/Losses"]) - revenue  # Update this line
        revenue = int(row["Profit/Losses"])  # Update this line
        revenue_changed = revenue_changed + [revenue_change]
        if revenue_change > greatest[1]:
            greatest[0] = row["Date"]
            greatest[1] = revenue_change
        if revenue_change < greatestdecrease[1]:
            greatestdecrease[0] = row["Date"]
            greatestdecrease[1] = revenue_change

revenue_avg = sum(revenue_changed) / len(revenue_changed)
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Profit/Loss: ${revenue}\n"
    f"Average Profit/Loss: {revenue_avg}\n"
    f"Greatest Profit: {greatest[0]} (${greatest[1]})\n"
    f"Greatest Loss: {greatestdecrease[0]} (${greatestdecrease[1]})"
)

print(output)
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
