# Stock Market Prediction Project

Bu proje, haber verilerini ve Reddit sentiment analizini kullanarak Dow Jones Industrial Average (DJIA) hisse senedi endeksinin hareketlerini tahmin etmeyi amaçlamaktadır.

##  Proje Genel Bakış

Bu makine öğrenmesi projesi, finansal piyasalardaki haber etkisini analiz ederek borsa tahminleri yapmaya odaklanmaktadır. Proje, çeşitli haber kaynaklarından ve Reddit verilerinden yararlanarak DJIA endeksinin günlük hareketlerini öngörmeye çalışır.

##  Veri Setleri

### 1. Combined_News_DJIA.csv
- DJIA endeks verileri ile haber başlıklarının birleştirilmiş hali
- Tarih, endeks değerleri ve ilgili haber başlıkları içerir

### 2. RedditNews.csv
- Reddit platformundan toplanan haber ve yorum verileri
- Sosyal medya sentiment analizi için kullanılır

### 3. upload_DJIA_table.csv
- DJIA endeksinin geçmiş verileri
- Açılış, kapanış, yüksek, düşük değerleri içerir

## Proje Hedefleri

- Haber başlıklarından sentiment analizi yaparak piyasa yönünü tahmin etme
- Reddit verilerini kullanarak sosyal medya etkisini modelleme
- Makine öğrenmesi algoritmaları ile doğru tahmin modellerı geliştirme
- Finansal piyasalarda haber etkisinin nicel analizini yapma


##  Metodoloji

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

##  Beklenen Sonuçlar

- DJIA endeksinin günlük yön tahmininde başarılı bir model
- Haber etkisinin borsa üzerindeki nicel analizi
- Sosyal medya sentiment'inin piyasa hareketleriyle korelasyonu
- Finansal karar verme süreçleri için kullanılabilir öngörüler
