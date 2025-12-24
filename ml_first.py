import matplotlib.pyplot as plt

calisma_saati = [1, 2, 3, 4, 5, 6, 7, 8]
sinav_notu = [15, 25, 40, 55, 65, 75, 85, 95]

plt.scatter(calisma_saati,sinav_notu,color="red")

plt.title("Çalışma Başarı Grafiği")
plt.xlabel("Çalışma Saatleri")
plt.ylabel("Sınav Notları")

plt.show()