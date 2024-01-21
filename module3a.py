import csv

# Function to analyze financial data
def analyze_financial_data(csv_path, output_file):
    # Initialize variables
    total_months = 0
    net_total = 0
    previous_profit_loss = 0
    total_change = 0
    greatest_increase = {"date": "", "amount": float("-inf")}
    greatest_decrease = {"date": "", "amount": float("inf")}
    
    # Read the CSV file
    with open(csv_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Skip header row

        # Loop through rows in the dataset
        for row in csvreader:
            # Extract date and profit/loss from the row
            date = row[0]
            profit_loss = int(row[1])

            # Update total months and net total
            total_months += 1
            net_total += profit_loss

            # Calculate change in profit/loss
            change = profit_loss - previous_profit_loss
            total_change += change

            # Update greatest increase and decrease
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change

            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

            # Update previous profit/loss for the next iteration
            previous_profit_loss = profit_loss

    # Calculate average change
    average_change = total_change / (total_months - 1)

    # Print the financial analysis results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
    print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

    # Write results to a text file in the same directory as the script
    with open(output_file, 'w') as outfile:
        outfile.write("Financial Analysis\n")
        outfile.write("----------------------------\n")
        outfile.write(f"Total Months: {total_months}\n")
        outfile.write(f"Total: ${net_total}\n")
        outfile.write(f"Average Change: ${average_change:.2f}\n")
        outfile.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
        outfile.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

# Provide the path to your budget_data.csv file
csv_path = r"C:\Users\adamf\OneDrive\Desktop\Starter_Code\PyBank\Resources\budget_data.csv"

# Specify the output file path with the same directory as the script
output_file = "financial_analysis.txt"

# Call the function to analyze the financial data
analyze_financial_data(csv_path, output_file)