#importations bibliothèques et définition de la position initiale

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
x0=0


# Charger le fichier CSV
data = pd.read_csv("vitesse1.csv")  # Remplace par le nom réel du fichier
temps = np.array(data["Time (s)"])
vitesse_m_s = np.array(data["Speed (m/s)"])
vitesse_km_h = 3.6*vitesse_m_s #conversion en km/h pour le tracé de vitesse


#calcul de l'accélération (dérivée (euler progressive))
acc=np.zeros(len(vitesse_m_s))
for i in range(len(temps)-1):
    acc[i]=(vitesse_m_s[i+1]-vitesse_m_s[i])/(temps[i+1]-temps[i])


#calcul de la position (intégrale par méthode trapèze)
distance = np.zeros(len(temps)-1)  
distance[0]=x0

for i in range(len(temps)-1):
    dt = temps[i+1] - temps[i]
    dv = (vitesse_m_s[i] + vitesse_m_s[i+1]) / 2
    dx = dv * dt
    distance[i]=distance[i-1] + dx
temps_pos=[]
for i in range(len(temps)-1):
    temps_pos.append(temps[i])



#réponse aux questions

#recherche pic accélération
acc_max=0
temps_acc_max=0
for i in range(len(acc)):
    if acc[i]>acc_max:
        acc_max=acc[i]
        temps_acc_max=temps[i]
print('')
print(f"la valeur d'accélération maximale est de {acc_max:.3f}m/s², on atteint cette valeur à {temps_acc_max:.3f}s")


#recherche distance parcourue totale
dist=distance[-1]
temps_final=temps[-1]
print("")
print(f"La distance totale qu'on a parcourue en {temps_final:.3f}s est de {dist:.3f}m")

# Tracés

#vitesse
plt.plot(temps, vitesse_km_h,label='vitesse(km/h)')
plt.xlabel("temps(s)")
plt.ylabel("vitesse(km/h)")
plt.title("Tracé de la vitesse en fonction du temps")
plt.grid(True)
plt.legend()
plt.show()

#accélération
plt.plot(temps, acc,label='accélération(m/s²)')
plt.grid()
plt.title("tracé de l'accélération en fonction du temps")
plt.xlabel("temps(s)")
plt.ylabel(r"accélération (m/s$^2$)")
plt.scatter(temps_acc_max,acc_max,color='red',marker='+',zorder=10,s=100,label='accélération max')
plt.legend()
plt.show()

#position
plt.plot(temps_pos,distance,label='distance parcourue (m)')
plt.grid()
plt.title("tracé de la position en fonction du temps")
plt.xlabel('temps(s)')
plt.ylabel('position(m)')
plt.legend()
plt.show()