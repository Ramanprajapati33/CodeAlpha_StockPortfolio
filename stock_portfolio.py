import csv

# Sample prices only; these are not live stock-market prices.
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 175.00,
    "AMZN": 190.00,
}


def get_positive_quantity(prompt):
    while True:
        value = input(prompt).strip()
        try:
            quantity = int(value)
            if quantity <= 0:
                print("Quantity must be a positive whole number.")
                continue
            return quantity
        except ValueError:
            print("Please enter a valid whole number.")


def main():
    print("=== Stock Portfolio Tracker ===")
    print("Available sample stocks and prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price:.2f} per share")

    portfolio = {}
    while True:
        symbol = input("\nEnter stock symbol (or DONE to finish): ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("Unknown symbol. Choose one from the list above.")
            continue

        quantity = get_positive_quantity(f"Quantity of {symbol}: ")
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    if not portfolio:
        print("No stocks entered. Nothing to calculate.")
        return

    print("\n=== Portfolio Summary ===")
    total = 0.0
    rows = []
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total += value
        print(f"{symbol}: {quantity} shares x ${price:.2f} = ${value:.2f}")
        rows.append([symbol, quantity, f"{price:.2f}", f"{value:.2f}"])

    print(f"Total investment value: ${total:.2f}")
    save = input("Save summary to portfolio.csv? (y/n): ").strip().lower()
    if save == "y":
        with open("portfolio.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Symbol", "Quantity", "Sample Price USD", "Investment Value USD"])
            writer.writerows(rows)
            writer.writerow(["TOTAL", "", "", f"{total:.2f}"])
        print("Saved as portfolio.csv")


if __name__ == "__main__":
    main()
