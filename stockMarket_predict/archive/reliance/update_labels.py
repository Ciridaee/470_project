import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('finaldata.csv')

# Değiştirilecek index'leri oku
with open('indices_to_change.txt', 'r') as f:
    indices_to_change = [int(line.strip()) for line in f.readlines()]

print(f"Original label distribution:")
print(df['label'].value_counts())
print(f"\nChanging {len(indices_to_change)} labels from 0 to 1...")

# Index'lerde label'ları 0'dan 1'e çevir
for idx in indices_to_change:
    if df.loc[idx, 'label'] == 0:
        df.loc[idx, 'label'] = 1
        
print(f"\nNew label distribution:")
print(df['label'].value_counts())

# Güncellenen dosyayı kaydet
df.to_csv('finaldata.csv', index=False)
print(f"\nSuccessfully updated finaldata.csv!")

# Değişen satırları kontrol et
print("\nSample of changed rows:")
changed_rows = df.loc[indices_to_change[:10]]
print(changed_rows[['Date', 'Open', 'Close', 'Compound', 'Positive', 'label']].to_string())
