import pandas as pd

def clean_data(filepath):
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    df = df.fillna(method="ffill")
    df = df.dropna()
    df.to_csv("clean_prices.csv")
    return df

if __name__ == "__main__":
    df = clean_data("raw_prices.csv")
    print(df.head())