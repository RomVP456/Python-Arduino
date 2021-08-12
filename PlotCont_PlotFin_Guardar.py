#Ubicacion→ C:\Users\moman\Documents\Python\TechWeek
#Ejecutar→ python PlotCont_PlotFin_Guardar.py 
import serial #requiere pip install pySerial
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from pathlib import Path

#Funcion para actualizar los datos
def getSerialData(self,Samples,SerialConection,lines,lineValueText, lineLabel):
	value = float(serialConnection.readline().strip())
	data.append(value)
	lines.set_data(range(Samples),data)
	lineValueText.set_text(lineLabel+' = '+str(round(value,2)))
	AllData.append(value)

try:
	serialConnection = serial.Serial('COM3', 9600)
except:
	print("no se pudo realizar la conexion")

Samples = 100
data = collections.deque([0] * Samples, maxlen=Samples)
AllData = collections.deque([0])
sampleTime = 100


#Limites de los ejes
xmin = 0
xmax = 120
ymin = 0
ymax = 1024

#Crear la ventana de plot
fig = plt.figure(figsize=(13,6))
ax = plt.axes(xlim=(xmin,xmax),ylim=(ymin,ymax))
plt.title("Ploteo como monitor Serial")
ax.set_xlabel("muestras")
ax.set_ylabel("voltaje del adc")

#Poner nombres
lineLabel = "voltaje"
lines = ax.plot([],[], label=lineLabel)[0]
lineValueText = ax.text(0.85, 0.95, '', transform=ax.transAxes)


#Reiniciar arduino para que los datos sean desde que inicia el probrama
serialConnection.setDTR(False)
serialConnection.flushInput()
serialConnection.setDTR(True)

anim = animation.FuncAnimation(fig,getSerialData,fargs=(Samples,serialConnection,lines,lineValueText, lineLabel),interval=sampleTime)
plt.show()
#Terminar conexion con arduino
serialConnection.close()

final = plt.figure(figsize=(13,6))
figura1 = plt.subplot(2,2,1)
#plt.hist(data, color='#ECEB05')
plt.hist(AllData, color='olive')
figura2 = plt.subplot(2,2,2)
plt.plot(AllData)
figura3 = plt.subplot(2,2,3)
plt.scatter(range(len(AllData)),AllData)
figura3 = plt.subplot(2,2,4)
plt.boxplot(AllData)
plt.show()

p = Path('Datos.txt')
archivo=open('Datos.txt','w')
for i in range(len(AllData)):
	archivo.write(str(AllData[i])+'\n')
archivo.close()
