import pandas as pd

df = pd.read_csv('finaldata.csv')

# Değişen index'leri oku
with open('indices_to_change.txt', 'r') as f:
    indices = [int(line.strip()) for line in f.readlines()]

print('Verification of label changes:')
print('Index | Date       | Open     | Close    | Price Change% | Compound | Positive | Label')
print('-' * 90)

for i, idx in enumerate(indices[:10]):
    row = df.loc[idx]
    price_change_pct = ((row['Close'] - row['Open']) / row['Open']) * 100
    print(f'{idx:5d} | {row["Date"]:10s} | {row["Open"]:8.2f} | {row["Close"]:8.2f} | {price_change_pct:11.2f} | {row["Compound"]:8.4f} | {row["Positive"]:8.3f} | {row["label"]:5d}')

print(f'\nTotal changes made: {len(indices)}')
print(f'New distribution: 0={(df["label"]==0).sum()}, 1={(df["label"]==1).sum()}')
print(f'Percentage of class 1: {((df["label"]==1).sum() / len(df) * 100):.1f}%')

print('\nSummary of changed examples (all should have positive price change and good sentiment):')
changed_data = df.loc[indices]
print(f'Average price change: {((changed_data["Close"] - changed_data["Open"]) / changed_data["Open"] * 100).mean():.2f}%')
print(f'Average Compound sentiment: {changed_data["Compound"].mean():.4f}')
print(f'Average Positive sentiment: {changed_data["Positive"].mean():.4f}')
