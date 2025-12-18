import time

bakiye=1000

def para_cek(miktar):
    global bakiye

    if miktar>bakiye:
        return "Bakiyenizden büyük değer çekemezsiniz!!!"
    elif miktar>0:
        bakiye-=miktar

        return "Paranız başarılı bir şekilde çekilmiştir"
    else:
        return "Yanlış seçim lütfen tekrar deneyin"

def bakiye_sorgula():
    global bakiye
    return bakiye

def para_yatir(miktar):
    global bakiye

    if miktar>0:
        bakiye+=miktar

        return "Paranız başarılı bir şekilde yatırılmıştır"
    else:
        return "Yanlış seçim lütfen tekrar deneyin"



print("---BİNFİNANS'a Hoşgeldiniz---")

while True:
    print("1) Para Çek")
    print("2) Para Yatır")
    print("3) Bakiye Sorgula")
    print("4) Çıkış")

    try:
        secim=int(input("Lütfen yapmak istediğiniz işlemi seçin : "))

        if secim==1:
            try:
                miktar=int(input("Lütfen çekmek istediğiniz tutarı girin : "))
                donut=para_cek(miktar)

                print(donut)

            except ValueError:
                print("Yanlış seçim lütfen tekrar deneyin")

        elif secim==2:
            try:
                miktar=int(input("Lütfen yatırmak istediğiniz tutarı girin : "))
                donut=para_yatir(miktar)

                print(donut)

            except ValueError:
                print("Yanlış seçim lütfen tekrar deneyin")

        elif secim==3:
            para=bakiye_sorgula()
            print(f"Mevcut Bakiyeniz : {para}")

        elif secim==4:
            print("Çıkış yapılıyor lütfen bekleyin...")
            time.sleep(3)
            break

    except ValueError:
        print("Yanlış seçim lütfen tekrar deneyin")