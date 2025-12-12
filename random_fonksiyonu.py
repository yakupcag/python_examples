import random

from matplotlib.pylab import rand

zar=[1,2,3,4,5,6]

print("Zar atılıyor.....\n")
print(random.choice(zar))

# rastgele iki veri getir
print(random.sample(zar,k=2))