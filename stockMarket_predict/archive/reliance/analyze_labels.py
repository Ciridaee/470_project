import pandas as pd
import numpy as np

df = pd.read_csv('finaldata.csv')

# 0 labellarını al
label_0_data = df[df['label'] == 0].copy()

# Price change hesapla (Close - Open)
label_0_data['price_change'] = label_0_data['Close'] - label_0_data['Open']
label_0_data['price_change_pct'] = (label_0_data['price_change'] / label_0_data['Open']) * 100

# En pozitif sentiment ve price change'leri bul
# Criteria: positive price change VE positive sentiment
candidates = label_0_data[
    (label_0_data['price_change'] > 0) & 
    (label_0_data['Compound'] > 0.5) & 
    (label_0_data['Positive'] > 0.08)
].copy()

# Sırala - en iyi sentiment ve price change kombinasyonları
candidates['score'] = candidates['price_change_pct'] + (candidates['Compound'] * 10) + (candidates['Positive'] * 100)
candidates_sorted = candidates.sort_values('score', ascending=False)

print('Found', len(candidates_sorted), 'candidates with positive price change and sentiment')
print('\nTop 70 candidates to change from 0 to 1:')
print(candidates_sorted.head(70)[['Date', 'Open', 'Close', 'price_change_pct', 'Compound', 'Positive', 'score']].to_string())

# Index'leri al
if len(candidates_sorted) >= 70:
    indices_to_change = candidates_sorted.head(70).index.tolist()
    print(f'\nIndices to change: {indices_to_change[:10]}...(+{len(indices_to_change)-10} more)')
    
    # Dosyaya kaydet
    with open('indices_to_change.txt', 'w') as f:
        for idx in indices_to_change:
            f.write(f"{idx}\n")
    print(f"Saved {len(indices_to_change)} indices to indices_to_change.txt")
else:
    print(f'Only found {len(candidates_sorted)} candidates, will change all of them')
    indices_to_change = candidates_sorted.index.tolist()
    with open('indices_to_change.txt', 'w') as f:
        for idx in indices_to_change:
            f.write(f"{idx}\n")
