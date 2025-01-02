# import des bibliothéques

import numpy as np
import matplotlib.pyplot as plt

# création des fonctions

def perceptron(x, w, active):
    x_aug = np.append(1, x)  # Ajout du biais

    Z = np.dot(w, x_aug)  # produit de 2 vecteurs : calcule de la somme pondérée

    if active == 0:
        y = np.sign(Z)
    elif active == 1:
        y = np.tanh(Z)
    else:
        raise ValueError("active doit être 0 pour sign ou 1 pour tanh")

    return y  # la sortie d'un neurone
