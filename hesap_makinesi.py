
def topla(x,y):
    return x+y
def cikar(x,y):
    return x-y
def carp(x,y):
    return x*y
def bol(x,y):
    if y == 0:
        return None
    else:
        return x/y
    


print("\n---Hesap Makinesine Hoşgeldiniz---\n")

while True:
    try:
        sayi1=int(input("Birinci sayıyı girin : "))
        sayi2=int(input("İkinci sayıyı girin : "))

        print()
        print("Toplama için +")
        print("Çıkarma için -")
        print("Çarpma için *")
        print("Bölme için /")
        print("Çıkış için 0")


        secim=input("Lütfen seçiminizi yapın : ")
        if secim=="+":
            sonuc=topla(sayi1,sayi2)
            print(f"Sonuc = {sonuc}")

        elif secim=="-":
            sonuc=cikar(sayi1,sayi2)
            print(f"Sonuc = {sonuc}")

        elif secim=="*":
            sonuc=carp(sayi1,sayi2)
            print(f"Sonuc = {sonuc}")

        elif secim=="/":
            sonuc=bol(sayi1,sayi2)
            if sonuc is None:
                print("HATA!!! Sıfıra bölme işlemi yapılamaz")
            else:
                print(f"Sonuc = {sonuc}")

        elif secim=="0":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Yanlış seçim!!!")

    except ValueError:
        print("\n!!! Lütfen sayı girin !!!\n")