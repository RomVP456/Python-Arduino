from pathlib import Path
import matplotlib.pyplot as plt
File = open('Datos.txt', 'r')
datos=[]
lineas=File.readlines()
for i in range(len(lineas)):
    datos.append(float(lineas[i].strip('\n')))
print(datos)
plt.hist(datos)
plt.show()
File.close()