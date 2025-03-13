import yfinance as yf
import pandas as pd

# Define the Portfolio class
class Portfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares, purchase_price):
        if symbol in self.portfolio:
            self.portfolio[symbol]['shares'] += shares
        else:
            self.portfolio[symbol] = {'shares': shares, 'purchase_price': purchase_price}

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if self.portfolio[symbol]['shares'] >= shares:
                self.portfolio[symbol]['shares'] -= shares
                if self.portfolio[symbol]['shares'] == 0:
                    del self.portfolio[symbol]
            else:
                print(f"Error: You don't have enough shares of {symbol} to remove.")
        else:
            print(f"Error: Stock {symbol} not in portfolio.")

    def get_stock_data(self, symbol):
        try:
            stock = yf.Ticker(symbol)
            stock_data = stock.history(period="1d")
            if not stock_data.empty:
                return stock_data['Close'].iloc[0]
            else:
                print(f"Error: No data found for {symbol}.")
                return None
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None

    def track_performance(self):
        total_investment = 0
        total_value = 0
        total_gain_loss = 0

        for symbol, data in self.portfolio.items():
            current_price = self.get_stock_data(symbol)
            if current_price is None:
                continue  # Skip if stock data couldn't be fetched
            
            # Calculate the total investment for the stock
            total_investment_for_stock = data['shares'] * data['purchase_price']
            total_value_for_stock = data['shares'] * current_price
            gain_loss_for_stock = total_value_for_stock - total_investment_for_stock

            # Update total values
            total_investment += total_investment_for_stock
            total_value += total_value_for_stock
            total_gain_loss += gain_loss_for_stock

            print(f"{symbol}:")
            print(f"  Shares: {data['shares']}")
            print(f"  Purchase Price: ${data['purchase_price']:.2f}")
            print(f"  Current Price: ${current_price:.2f}")
            print(f"  Total Investment: ${total_investment_for_stock:.2f}")
            print(f"  Total Value: ${total_value_for_stock:.2f}")
            print(f"  Gain/Loss: ${gain_loss_for_stock:.2f}\n")
        
        print("Portfolio Performance Summary:")
        print(f"  Total Investment: ${total_investment:.2f}")
        print(f"  Total Portfolio Value: ${total_value:.2f}")
        print(f"  Total Gain/Loss: ${total_gain_loss:.2f}\n")

# Function to interact with the user
def portfolio_manager():
    portfolio = Portfolio()
    while True:
        print("Menu:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Track Performance")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL, MSFT, TSLA): ").upper()
            shares = int(input("Enter number of shares: "))
            purchase_price = float(input("Enter purchase price per share: "))
            portfolio.add_stock(symbol, shares, purchase_price)
            print(f"Added {shares} shares of {symbol} at ${purchase_price:.2f} each.\n")
        
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            shares = int(input(f"Enter number of shares of {symbol} to remove: "))
            portfolio.remove_stock(symbol, shares)
        
        elif choice == '3':
            print("\nPortfolio Overview:")
            if portfolio.portfolio:
                for symbol, data in portfolio.portfolio.items():
                    print(f"{symbol}: {data['shares']} shares, purchased at ${data['purchase_price']:.2f}")
            else:
                print("Your portfolio is empty.")
            print()

        elif choice == '4':
            print("\nTracking Performance...")
            portfolio.track_performance()

        elif choice == '5':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice, please try again.\n")

# Run the portfolio manager
if __name__ == "__main__":
    portfolio_manager()
