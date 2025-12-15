import time
import random

def Tara():
    while True:
        print("\nPortlar taranıyor...\n")
        for port_no, servis_adi in portlar.items():
            print(f"Port: {port_no}, Servis: {servis_adi}")
            acikMi=random.randint(0,1)

            if acikMi == 1:
                print(f"[+] {port_no} portu açık")
            else:
                print(f"[-] {port_no} portu kapalı")

            time.sleep(1)
        
        print("Tarama tamamlandı 10 saniye sonra tekrar tarama yapılacak")
        time.sleep(10)

print("---Port Tarayıcıya Hoşgeldiniz---")

portlar={21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS", 3306: "MySQL"}

Tara()