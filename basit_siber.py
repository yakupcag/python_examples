
veritabani = {
    "192.168.1.1": "Modem",
    "8.8.8.8": "Google DNS",
    "10.0.0.1": "Router"
}

print("\n--- IP İSTİHBARAT SİSTEMİ ---\n")

while True:
    print("-" * 30)
    print("1) IP Listele")
    print("2) IP Sorgula")
    print("X) Çıkış")

    secim = input("\nSeçiminiz: ").upper() 

    if secim == "1":
        print("\n--- KAYITLI CİHAZLAR ---")

        for ip, isim in veritabani.items():
            print(f"IP: {ip}  -->  Cihaz: {isim}")

    elif secim == "2":
        sorgu_ip = input("Aranacak IP: ")
        

        if sorgu_ip in veritabani:
            print(f"✅ BULUNDU! Bu IP şuna ait: {veritabani[sorgu_ip]}")
        else:
            print("❌ Bu IP kayıtlı değil.")
            ekle = input("Eklemek ister misiniz? (E/H): ").lower()
            if ekle == "e":
                yeni_isim = input("Cihazın adı nedir?: ")
                veritabani[sorgu_ip] = yeni_isim
                print("✅ Kayıt Başarılı!")

    elif secim == "X":
        print("Sistemden çıkılıyor...")
        break
    else:
        print("Hatalı seçim!")