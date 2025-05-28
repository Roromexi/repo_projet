import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
v0=0
x0=0

# Charger le fichier CSV
data = pd.read_csv("vitesse1.csv")  # Remplace par le nom réel du fichier

#tracé des vitesses
temps = np.array(data["Time (s)"])
vitesse_m_s = np.array(data["Speed (m/s)"])
vitesse_km_h = 3.6*vitesse_m_s


#calcul de l'accélération (dérivée)
acc=np.zeros(len(vitesse_m_s))
for i in range(len(temps)-1):
    acc[i]=(vitesse_m_s[i+1]-vitesse_m_s[i])/temps[i+1]



# Tracer
plt.plot(temps, vitesse_km_h)
plt.xlabel("temps(s)")
plt.ylabel("vitesse(km/h)")
plt.title("Tracé de colonne_y en fonction de colonne_x")
plt.grid(True)
plt.show()
plt.plot(temps, acc)
plt.grid()
plt.xlabel("temps(s)")
plt.ylabel(r"accélération (m/s$^2$)")
plt.show()