# Stock Market Prediction Project

Bu proje, haber verilerini ve Reddit sentiment analizini kullanarak Dow Jones Industrial Average (DJIA) hisse senedi endeksinin hareketlerini tahmin etmeyi amaçlamaktadır.

## 📊 Proje Genel Bakış

Bu makine öğrenmesi projesi, finansal piyasalardaki haber etkisini analiz ederek borsa tahminleri yapmaya odaklanmaktadır. Proje, çeşitli haber kaynaklarından ve Reddit verilerinden yararlanarak DJIA endeksinin günlük hareketlerini öngörmeye çalışır.

## 📁 Proje Yapısı

```
470_project/
├── README.md                 # Proje dokümantasyonu
├── ipynb/                   # Jupyter notebook dosyaları
├── stockMarket_predict/     # Ana veri ve modelleme klasörü
│   ├── Combined_News_DJIA.csv    # Birleştirilmiş haber ve DJIA verileri
│   ├── RedditNews.csv            # Reddit haber verileri
│   └── upload_DJIA_table.csv     # DJIA tablo verileri
```

## 📈 Veri Setleri

### 1. Combined_News_DJIA.csv
- DJIA endeks verileri ile haber başlıklarının birleştirilmiş hali
- Tarih, endeks değerleri ve ilgili haber başlıkları içerir

### 2. RedditNews.csv
- Reddit platformundan toplanan haber ve yorum verileri
- Sosyal medya sentiment analizi için kullanılır

### 3. upload_DJIA_table.csv
- DJIA endeksinin geçmiş verileri
- Açılış, kapanış, yüksek, düşük değerleri içerir

## 🎯 Proje Hedefleri

- Haber başlıklarından sentiment analizi yaparak piyasa yönünü tahmin etme
- Reddit verilerini kullanarak sosyal medya etkisini modelleme
- Makine öğrenmesi algoritmaları ile doğru tahmin modellerı geliştirme
- Finansal piyasalarda haber etkisinin nicel analizini yapma

## 🔧 Teknolojiler

- **Python**: Ana programlama dili
- **Pandas**: Veri manipülasyonu ve analizi
- **NumPy**: Sayısal hesaplamalar
- **Scikit-learn**: Makine öğrenmesi modelleri
- **NLTK/spaCy**: Doğal dil işleme ve sentiment analizi
- **Matplotlib/Seaborn**: Veri görselleştirme
- **Jupyter Notebook**: Analiz ve model geliştirme ortamı

## 🚀 Kurulum

1. Repository'yi klonlayın:
```bash
git clone <repository-url>
cd 470_project
```

2. Gerekli Python paketlerini yükleyin:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn nltk jupyter
```

3. Jupyter Notebook'u başlatın:
```bash
jupyter notebook
```

## 📊 Kullanım

1. `ipynb/` klasöründeki notebook dosyalarını açın
2. Veri analizi ve ön işleme adımlarını takip edin
3. Sentiment analizi modellerini çalıştırın
4. Tahmin modellerini eğitin ve test edin
5. Sonuçları değerlendirin ve görselleştirin

## 📋 Metodoloji

### 1. Veri Ön İşleme
- Haber başlıklarının temizlenmesi
- Tarih formatlarının standardizasyonu
- Eksik verilerin işlenmesi

### 2. Sentiment Analizi
- Haber başlıklarından sentiment skorları çıkarma
- Reddit verilerinden toplumsal duygu analizi
- Pozitif/negatif sentiment sınıflandırması

### 3. Feature Engineering
- Teknik göstergeler ekleme
- Lag features oluşturma
- Sentiment skorlarının agregasyonu

### 4. Model Geliştirme
- Çeşitli makine öğrenmesi algoritmalarının test edilmesi
- Cross-validation ile model performansı değerlendirme
- Hiperparametre optimizasyonu

## 📈 Beklenen Sonuçlar

- DJIA endeksinin günlük yön tahmininde başarılı bir model
- Haber etkisinin borsa üzerindeki nicel analizi
- Sosyal medya sentiment'inin piyasa hareketleriyle korelasyonu
- Finansal karar verme süreçleri için kullanılabilir öngörüler

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje [MIT License](LICENSE) altında lisanslanmıştır.

## 📞 İletişim

Proje hakkında sorularınız için lütfen iletişime geçin.

## ⚠️ Uyarı

Bu proje sadece eğitim amaçlıdır. Finansal yatırım kararları alırken bu tahminleri tek başına kullanmayın. Yatırım yapmadan önce mutlaka profesyonel finansal danışmanlık alın.