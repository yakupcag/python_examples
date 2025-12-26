import matplotlib.pyplot as plt
import numpy as np

ev_m2=np.random.randint(50,200,100)
fiyat = (ev_m2 * 1000) + np.random.randint(-20000, 20000, 100)

a,b=np.polyfit(ev_m2,fiyat,1)

endeks=a*ev_m2+b

veri_al=int(input("M2 girin : "))
ev_fiyat=a*veri_al+b

print(f"Tahmini {veri_al} m2 fiyatı : {ev_fiyat}")

plt.scatter(veri_al,ev_fiyat,marker="*",s=200, label="Sizin Ev")

plt.plot(ev_m2,endeks,color="red")

plt.title("Ev-Fiyat Endeksi")
plt.scatter(ev_m2,fiyat,color="green")

plt.xlabel("Ev m2")
plt.ylabel("Fiyat")

plt.show()