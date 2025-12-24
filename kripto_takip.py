import time
import requests

# Renk Kodları (Hacker Modu)
KIRMIZI = "\033[91m"
YESIL = "\033[92m"
SARI = "\033[93m"
RESET = "\033[0m"

hedef = int(input("Bitcoin kaç doların altına düşerse haber vereyim? : "))
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,try"

print(f"\n{SARI}--- TAKİP BAŞLADI (Hedef: {hedef} $) ---{RESET}\n")

while True:
    try:
        cevap = requests.get(url)
        gelen_veri = cevap.json()
        
        # Güncel fiyatı çekiyoruz
        guncel_fiyat = gelen_veri['bitcoin']['usd']

        # Eşittir (==) yerine Küçük Eşittir (<=) kullandık!
        if guncel_fiyat <= hedef:
            print(f"{KIRMIZI}🚨 ALARM! FİYAT DÜŞTÜ! 🚨")
            print(f"GÜNCEL FİYAT: {guncel_fiyat} $ {RESET}")
            # Fiyat düşünce döngüden çıkalım mı? Yoksa sürekli ötsün mü? 
            # Şimdilik sürekli ötsün.
            
        else:
            print(f"{YESIL}✅ Durum Stabil... Güncel: {guncel_fiyat} ${RESET}")

        # Bekleme süresi
        time.sleep(10)

    except Exception as e:
        # İnternet koparsa program çökmesin diye
        print(f"{KIRMIZI}HATA OLUŞTU (İnternet kopmuş olabilir): {e}{RESET}")
        time.sleep(10) # Hata olunca da bekle ki işlemciyi yormasın