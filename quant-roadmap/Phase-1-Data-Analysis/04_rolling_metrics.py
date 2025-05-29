import pandas as pd
import matplotlib.pyplot as plt

def plot_rolling_metrics(filepath):
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    returns = df.pct_change().dropna()
    rolling_vol = returns.rolling(window=60).std() * (252 ** 0.5)
    rolling_sharpe = (returns.mean() / returns.std()) * (252 ** 0.5)

    rolling_vol.plot(figsize=(10, 6))
    plt.title("60-Day Rolling Volatility")
    plt.savefig("rolling_volatility.png")
    plt.show()

    print("Annualized Sharpe Ratios:")
    print(rolling_sharpe)

if __name__ == "__main__":
    plot_rolling_metrics("clean_prices.csv")