# Renk Kodları
YESIL = "\033[92m"
KIRMIZI = "\033[91m"
SARI = "\033[93m"
RESET = "\033[0m"

def sifrekir(sifre):
    şifrebulundu=False
    kirilansifre=int()

    for i in range(10000):
        stri=str(i)
        print(f"{SARI}DENENİYOR {stri.zfill(4)} {RESET}")
        if i==sifre:
            şifrebulundu=True
            kirilansifre=i
            print()
            break

    if şifrebulundu==True:
        return kirilansifre
    else:
        return "Maalesef şifre bulunmadı"


sifre=input("Şifrenizi girin : ")

if len(sifre)==4:

    try :
        sifre=int(sifre)
        bulunansifre=sifrekir(sifre)

        if type(bulunansifre)==int:
            bulunansifre=str(bulunansifre)
            print(f"{YESIL}TEBRİKLER ŞİFRE BULUNDU")
            print(f"ŞİFRE : {bulunansifre.zfill(4)} {RESET}")

        else:
            print(f"{KIRMIZI}MAALESEF ŞİFRE BULUNAMADI {RESET}")

    except ValueError:
        print(KIRMIZI+"Yanlış seçim!!! \nLütfen sayı girin"+RESET)
else:
        print("Lütfen 4 haneli şifre girin")