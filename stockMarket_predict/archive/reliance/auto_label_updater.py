import pandas as pd
import numpy as np

def update_labels_by_price_movement(csv_file_path):
    """
    Open ve Close fiyatlarına göre label'ları günceller:
    - Open < Close ise label = 1 (fiyat yükseldi)
    - Open >= Close ise label = 0 (fiyat düştü veya aynı kaldı)
    """
    
    print("📊 CSV dosyası okunuyor...")
    df = pd.read_csv(csv_file_path)
    
    print(f"✅ Dosya başarıyla okundu: {len(df)} satır")
    print(f"📋 Kolonlar: {list(df.columns)}")
    
    # Mevcut label dağılımını göster
    if 'label' in df.columns:
        print(f"\n📈 Mevcut label dağılımı:")
        print(df['label'].value_counts().sort_index())
    
    # Yeni label'ları hesapla
    print(f"\n🔄 Yeni label'lar hesaplanıyor...")
    
    # Open < Close ise 1 (UP), aksi halde 0 (DOWN)
    df['new_label'] = np.where(df['Open'] < df['Close'], 1, 0)
    
    # Eski label ile karşılaştır
    if 'label' in df.columns:
        changes = (df['label'] != df['new_label']).sum()
        print(f"🔄 {changes} adet label değiştirildi")
        
        # Değişen örnekleri göster
        if changes > 0:
            changed_rows = df[df['label'] != df['new_label']].head(10)
            print(f"\n📋 İlk 10 değişen satır:")
            print(changed_rows[['Date', 'Open', 'Close', 'label', 'new_label']].to_string())
    
    # Eski label'ı güncelle
    df['label'] = df['new_label']
    df.drop('new_label', axis=1, inplace=True)
    
    # Yeni label dağılımını göster
    print(f"\n📊 Yeni label dağılımı:")
    label_counts = df['label'].value_counts().sort_index()
    print(label_counts)
    
    total = len(df)
    print(f"\n📈 Yüzdelik dağılım:")
    print(f"  Label 0 (DOWN): {label_counts[0]} ({label_counts[0]/total*100:.1f}%)")
    print(f"  Label 1 (UP):   {label_counts[1]} ({label_counts[1]/total*100:.1f}%)")
    
    # Güncellenmiş dosyayı kaydet
    output_file = csv_file_path.replace('.csv', '_updated_labels.csv')
    df.to_csv(output_file, index=False)
    print(f"\n💾 Güncellenmiş dosya kaydedildi: {output_file}")
    
    # Orijinal dosyayı da güncelle (isteğe bağlı)
    df.to_csv(csv_file_path, index=False)
    print(f"💾 Orijinal dosya da güncellendi: {csv_file_path}")
    
    # İstatistik bilgiler
    price_changes = ((df['Close'] - df['Open']) / df['Open']) * 100
    print(f"\n📊 Fiyat hareket istatistikleri:")
    print(f"  Ortalama fiyat değişimi: {price_changes.mean():.3f}%")
    print(f"  Maksimum artış: {price_changes.max():.3f}%")
    print(f"  Maksimum düşüş: {price_changes.min():.3f}%")
    print(f"  Standart sapma: {price_changes.std():.3f}%")
    
    # Pozitif/negatif hareket sayısı
    positive_moves = (df['Close'] > df['Open']).sum()
    negative_moves = (df['Close'] <= df['Open']).sum()
    
    print(f"\n🎯 Hareket analizi:")
    print(f"  Pozitif hareketler: {positive_moves} ({positive_moves/total*100:.1f}%)")
    print(f"  Negatif/Sıfır hareketler: {negative_moves} ({negative_moves/total*100:.1f}%)")
    
    return df

if __name__ == "__main__":
    # CSV dosya yolu
    csv_file = "finaldata.csv"
    
    print("🚀 OTOMATIK LABEL GÜNCELLEME BAŞLIYOR")
    print("=" * 60)
    print("📋 Kural: Open < Close ise Label = 1, aksi halde Label = 0")
    print("=" * 60)
    
    try:
        updated_df = update_labels_by_price_movement(csv_file)
        
        print("\n" + "=" * 60)
        print("✅ İŞLEM BAŞARIYLA TAMAMLANDI!")
        print("=" * 60)
        
        # Son kontrol
        print(f"\n🔍 Son kontrol:")
        print(f"  Toplam satır: {len(updated_df)}")
        print(f"  Label kolonları: {updated_df['label'].nunique()} farklı değer")
        print(f"  Boş değer var mı: {'Evet' if updated_df['label'].isna().any() else 'Hayır'}")
        
    except FileNotFoundError:
        print(f"❌ HATA: {csv_file} dosyası bulunamadı!")
        print("📁 Lütfen dosya yolunu kontrol edin.")
    except Exception as e:
        print(f"❌ HATA: {str(e)}")
        import traceback
        traceback.print_exc()
