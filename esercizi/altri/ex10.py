# Scrivi una funzione che, data una lista di numeri, fornisce in output un istogramma basato su questi numeri, usando matplotlib per disegnarlo.
import matplotlib.pyplot as plt
figura, grafico = plt.subplots()
# eta = {**dict(giovanni=52), **dict(silvia=40)}
eta = {'giovanni': 50, 'silvia': 47}

plt.bar(range(len(eta)), eta.values(), align='center')
plt.xticks(range(len(eta)), list(eta.keys()))
plt.show()
