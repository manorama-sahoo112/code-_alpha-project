# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 180,
    "MSFT": 420
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")

# Number of stocks
n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock = input("\nEnter stock name (e.g., AAPL): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        price = stock_prices[stock]
        investment = price * quantity

        print("Stock Price:", price)
        print("Investment:", investment)

        total_investment += investment
    else:
        print("Stock not available in the price list.")

# Display total
print("\n==============================")
print("Total Investment =", total_investment)
print("==============================")

# Optional: save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Tracker\n")
    file.write("-----------------------\n")
    file.write("Total Investment = " + str(total_investment))

print("\nResult saved to portfolio.txt")