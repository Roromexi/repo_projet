#importations bibliothèques et définition de la position initiale

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
x0=0


# Charger le fichier CSV
data = pd.read_csv("vitesse1.csv")  
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


#==================================================================================================
# REPONSES AUX QUESTIONS
#==================================================================================================


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



#==================================================================================================
# Tracés
#==================================================================================================


# VITESSE
plt.plot(temps, vitesse_km_h,label='vitesse(km/h)')
plt.xlabel("temps(s)")
plt.ylabel("vitesse(km/h)")
plt.title("Tracé de la vitesse en fonction du temps")
# ticks visibles
plt.xticks(np.arange(0, 51, 1))
plt.yticks(np.arange(0, 61, 1))
# grille principale toutes les 5
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(10))
# grille secondaire toutes les 1
plt.gca().xaxis.set_minor_locator(ticker.MultipleLocator(1))
plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(1))
# tracé des grilles
plt.grid(which='major', linewidth=1, color='black')
plt.grid(which='minor', linestyle='--', linewidth=0.5, color='gray')

plt.tight_layout()
plt.grid(True)
plt.legend()
plt.show()



#ACCELERATION
plt.plot(temps, acc,label='accélération(m/s²)')
plt.grid()
plt.title("tracé de l'accélération en fonction du temps")
plt.xlabel("temps(s)")
plt.ylabel(r"accélération (m/s$^2$)")
plt.scatter(temps_acc_max,acc_max,color='red',marker='+',zorder=10,s=100,label='accélération max')
plt.legend()
plt.show()




#POSITION
plt.plot(temps_pos,distance,label='distance parcourue (m)')
plt.grid()
plt.title("tracé de la position en fonction du temps")
plt.xlabel('temps(s)')
plt.ylabel('position(m)')
plt.legend()
plt.show()