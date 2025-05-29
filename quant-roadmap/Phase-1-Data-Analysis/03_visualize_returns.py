import pandas as pd
import matplotlib.pyplot as plt

def plot_daily_returns(filepath):
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    returns = df.pct_change().dropna()
    returns.plot(figsize=(10, 6))
    plt.title("Daily Returns")
    plt.savefig("daily_returns.png")
    plt.show()

if __name__ == "__main__":
    plot_daily_returns("clean_prices.csv")