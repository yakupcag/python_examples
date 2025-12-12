
print("---Sezar Şifreleme Sistemine Hoşgeldiniz---")

alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

cumle=input("Lütfen şifrelenecek metni girin : ").lower()
oteleme=int(input("Lütfen ötelenecek sayıyı girin : "))

if len(cumle)>0 :

    yenicumle=""

    for harf in cumle:

        if harf in alfabe:

            indexbul=alfabe.index(harf)
            yeniharf=(indexbul+oteleme)%29
            yenicumle+=alfabe[yeniharf]
        else:
            yenicumle+=harf
    
    print(f"Yeni Cümle : {yenicumle}")
    eskicumle=""

    for harf in yenicumle:

        if harf in alfabe:
            indexbul=alfabe.index(harf)
            eskiharf=indexbul-oteleme
            eskicumle+=alfabe[eskiharf]

        else:
            eskicumle+=harf
    
    print(f"Eski Cümle : {eskicumle}")
    
else:
    print("Lütfen değer girin")