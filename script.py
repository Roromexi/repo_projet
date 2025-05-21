import numpy as np
import matplotlib.pyplot as plt

# Temps total jusqu'à l'arrêt complet
t = np.linspace(0, 18, 1000)

# Définition des valeurs de vitesse
def v(t):
    if t <= 5:
        return 250
    elif t <= 10:
        return 250 - 10 * (t - 5)
    elif t <= 15:
        return 200 + 10 * (t - 10)
    elif t <= 50/3:
        return 250 - 150 * (t - 15)
    else:
        return 0

# Vectorisation
v_vec = np.vectorize(v)
v = v_vec(t)


# Tracé de la vitesse
plt.plot(t, v, label="v(t) : vitesse de la F1", color="red", linewidth=2)
plt.axvline(5, linestyle="--", color="gray", alpha=0.5, label="Début virage 1")
plt.axvline(10, linestyle="--", color="gray", alpha=0.5)
plt.axvline(15, linestyle="--", color="black", alpha=0.5, label="Crash")
plt.title("Vitesse d'une Formule 1 sur Spa-Francorchamps")
plt.xlabel("Temps (s)")
plt.ylabel("Vitesse (km/h)")
plt.grid(True)
plt.legend()

#définition de l'accéleration exacte
def a(t):
    if t <= 5:
        return 0
    elif t <= 10:
        return -10
    elif t <= 15:
        return 10
    elif t <= 50/3:
        return -150
    else:
        return 0
    
a_vec=np.vectorize(a)
a=a_vec(t)

plt.plot(t,a)
plt.show()
