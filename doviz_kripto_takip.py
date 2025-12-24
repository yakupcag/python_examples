import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd,try"

cevap=requests.get(url)
veri_cek=cevap.json()

for coin_adi,detaylar in veri_cek.items():
    dolar_fiyat=detaylar['usd']
    tl_fiyat=detaylar['try']
    print(f"{coin_adi.upper()} = {dolar_fiyat} Dolar | {tl_fiyat} TL")