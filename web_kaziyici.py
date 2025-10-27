import requests
from bs4 import BeautifulSoup
import csv
import os

def web_sayfasi_kazima(url):
    """
    Belirtilen URL'den kitap başlıklarını ve yazarlarını kazır (scraping yapar).
    """
    try:
        # 1. Sayfayı Çekme (Requests)
        print(f"Sayfa çekiliyor: {url}")
        response = requests.get(url)
        response.raise_for_status() # Hatalı durum kodları için hata fırlatır
        
        # 2. HTML'i Ayrıştırma (BeautifulSoup)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 3. Verileri Bulma (Kurgusal Sınıflar Kullanıldı)
        kitap_kartlari = soup.find_all('div', class_='kitap-karti') # Tüm kitap kartlarını bul
        
        veri_listesi = []
        
        if not kitap_kartlari:
            print("Uyarı: Sayfada 'kitap-karti' sınıfına sahip öğe bulunamadı.")
            return []

        for kart in kitap_kartlari:
            # Başlık ve yazarı bulmak için alt öğeleri arama
            baslik_elementi = kart.find('h2', class_='kitap-baslik')
            yazar_elementi = kart.find('span', class_='kitap-yazar')
            
            baslik = baslik_elementi.get_text(strip=True) if baslik_elementi else "Başlık Yok"
            yazar = yazar_elementi.get_text(strip=True) if yazar_elementi else "Yazar Yok"
            
            veri_listesi.append({
                'Baslik': baslik,
                'Yazar': yazar
            })
            
        return veri_listesi
        
    except requests.exceptions.RequestException as e:
        print(f"Hata: Sayfaya erişilemedi veya ağ hatası: {e}")
        return []

def csv_kaydet(veri, dosya_adi="kitap_listesi.csv"):
    """
    Kazınan veriyi CSV dosyasına kaydeder.
    """
    if not veri:
        print("Kaydedilecek veri bulunamadı.")
        return

    alan_isimleri = ['Baslik', 'Yazar']
    
    with open(dosya_adi, 'w', newline='', encoding='utf-8') as csvfile:
        yazici = csv.DictWriter(csvfile, fieldnames=alan_isimleri)
        
        yazici.writeheader() # Başlık satırını yazar
        yazici.writerows(veri) # Veri satırlarını yazar
        
    print(f"\n✅ Veriler başarıyla '{dosya_adi}' dosyasına kaydedildi.")

# --- Ana Çalışma Bloğu ---
if __name__ == "__main__":
    # Gerçek bir web sitesi URL'si ile değiştirin (izin verilen bir site kullanın!)
    HEDEF_URL = "https://kurgusal-kitap-listesi.com/listeler" 

    # Not: Gerçek bir sayfadan deneme yapıyorsanız, URL'yi ve HTML sınıflarını güncellemeyi unutmayın!

    kazinan_veri = web_sayfasi_kazima(HEDEF_URL)
    
    if kazinan_veri:
        print("\n--- Kazınan Veriler ---")
        for item in kazinan_veri:
            print(f"Başlık: {item['Baslik']}, Yazar: {item['Yazar']}")
        print("-----------------------\n")
        
        csv_kaydet(kazinan_veri)