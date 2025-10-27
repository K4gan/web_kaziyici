# 🕸️ Basit Web Kazıyıcı ve CSV Kaydedici (Web Scraper)

Bu proje, Python'ın güçlü kütüphaneleri olan **`requests`** ve **`BeautifulSoup4`** kullanılarak geliştirilmiş temel bir web kazıma (web scraping) aracıdır. Belirlenen bir web sayfasından yapılandırılmış veriyi çeker ve sonuçları komut satırına yazdırdıktan sonra, yerleşik **`csv`** modülü ile kalıcı bir `.csv` dosyasına kaydeder.

Bu proje, veri çekme, HTML ayrıştırma ve veri depolama konusundaki yetkinliğimi gösterir.

## 🛠️ Kullanılan Teknolojiler

* **Python 3.x**
* **Requests:** HTTP istekleri yapmak ve web sayfalarının içeriğini indirmek için.
* **BeautifulSoup4 (bs4):** İndirilen HTML/XML içeriğini ayrıştırmak ve veriyi seçmek için.
* **csv (Yerleşik Modül):** Kazınan veriyi standart bir CSV formatında kaydetmek için.

## 🚀 Kurulum ve Çalıştırma

1.  **Gerekli Kütüphaneleri Kurun:**
    ```bash
    pip install requests beautifulsoup4
    ```

2.  **Betiki Çalıştırın:**
    ```bash
    python web_kaziyici.py
    ```

3.  **Çıktıyı Kontrol Edin:**
    * Komut satırında kazınan verileri göreceksiniz.
    * Projenin bulunduğu dizinde, kazınan verileri içeren `kitap_listesi.csv` dosyası oluşacaktır.

## ⚠️ Önemli Not

* Lütfen kazıma (scraping) yapmadan önce hedef web sitesinin **`robots.txt`** dosyasını ve kullanım şartlarını kontrol edin. Etik kurallara uyun.
* Örnekteki `HEDEF_URL` ve HTML sınıfları (`kitap-karti`, `kitap-baslik`, vb.) kurgusaldır. Gerçek bir web sitesiyle deneme yaparken bu değerleri güncellemeyi unutmayın.

## 💡 Geliştirme Önerileri

* Kullanıcıdan kazınacak URL'yi ve aranacak HTML sınıflarını komut satırında girmesini isteme.
* Veri çekilirken gecikme ekleyerek (rate limiting) siteye aşırı yüklenmeyi önleme.
* Hata işleme mekanizmasını (örneğin, bulunamayan öğeler için) daha da iyileştirme.
