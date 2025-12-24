import matplotlib.pyplot as plt

# 1. Veriler
gunler = ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"]
btc_fiyat = [95000, 96200, 94500, 97000, 98500, 93000, 99000]
eth_fiyat = [3000, 3100, 3050, 3200, 3300, 3150, 3400]

# 2. Grafik Boyutunu Ayarla (İsteğe bağlı ama şık durur)
plt.figure(figsize=(10, 6)) # 10 inç genişlik, 6 inç yükseklik

# 3. Çizimler (Layer Mantığı: Üst üste binerler)
# label paramtresi LEJANT için gereklidir!
plt.plot(gunler, btc_fiyat, color='orange', marker='o', label="Bitcoin (BTC)")
plt.plot(gunler, eth_fiyat, color='blue', marker='s', linestyle='--', label="Ethereum (ETH)")

# 4. Süslemeler
plt.title("Kripto Para Haftalık Analiz")
plt.xlabel("Günler")
plt.ylabel("Fiyat ($)")
plt.grid(True, alpha=0.3) # alpha: çizgi şeffaflığı (0.3 silik yapar)

# 5. KUTUCUĞU GÖSTER (Lejant)
plt.legend() 

# 6. Ekrana Bas
plt.show()