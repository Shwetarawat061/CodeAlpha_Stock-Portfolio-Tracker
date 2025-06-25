from datetime import datetime

# Pre-defined stock prices dictionary
stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 140, "MSFT": 300}

# Portfolio dictionary to keep track of stocks and quantities
portfolio = {}

print("=== Welcome to the Stock Portfolio Tracker ===")
print("You can enter stock names to add them to your portfolio.")
print("If a stock isn't in the list, you can add it with its current price.")
print("Type 'done' when you are finished entering stocks.\n")

while True:
    # Display current available stocks with prices
    print("Available stocks:")
    for stock, price in stock_prices.items():
        print(f" - {stock}: ₹{price}")
    print()

    stock = input("Enter stock name from above list (or 'done' to finish): ").upper().strip()

    if stock == "DONE":
        print("\nYou have chosen to finish entering stocks.")
        break  # Exit the loop

    # Check if the stock is known
    if stock not in stock_prices:
        print(f"⚠️ Stock '{stock}' not found in the current list.")
        add = input("Would you like to add this new stock? (yes/no): ").lower().strip()

        if add == "yes":
            while True:
                try:
                    price = float(input(f"Enter the current price for {stock} (in ₹): "))
                    if price <= 0:
                        print("❌ Price must be a positive number. Please try again.")
                        continue
                    stock_prices[stock] = price
                    print(f"✅ Stock '{stock}' added with price ₹{price}\n")
                    break
                except ValueError:
                    print("❌ Invalid input. Please enter a numeric value for the price.")
        else:
            print(f"Skipping stock '{stock}'. You can enter another stock.\n")
            continue  # Skip to the next iteration

    # Ask for quantity of the stock to add
    while True:
        try:
            quantity = int(input(f"Enter quantity of shares for {stock}: "))
            if quantity <= 0:
                print("❌ Quantity must be a positive integer. Please try again.")
                continue
            # Add or update quantity in portfolio
            portfolio[stock] = portfolio.get(stock, 0) + quantity
            print(f"✅ Added {quantity} shares of {stock} to your portfolio.\n")
            break
        except ValueError:
            print("❌ Invalid input. Please enter a whole number for quantity.")

# After input loop: calculate total portfolio value
total_value = sum(stock_prices[stock] * qty for stock, qty in portfolio.items())

# Display the portfolio summary
print("\n📈 Your Portfolio Summary:")
print("------------------------------")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    print(f"{stock}: {qty} shares @ ₹{price} each = ₹{value}")
print("------------------------------")
print(f"💰 Total Investment Value: ₹{total_value}")

# Save portfolio details to a text file with timestamp (using UTF-8 encoding)
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
filename = "portfolio.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"# Portfolio as of {now}\n")
    f.write("Stock,Quantity,Value (₹)\n")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        f.write(f"{stock},{qty},{value}\n")
    f.write(f"Total,,{total_value}\n")

print(f"\n✅ Your portfolio has been saved to '{filename}' with the date and time: {now}")
print("Thank you for using the Stock Portfolio Tracker! 📊")
