'''
Faciltad de Ingeniería, UNAM
Estructura de Datos y Algoritmos I, Python
Semaforo Epidemiológico Python 
Desarollado por Daniela Hernández Vázquez. 
Versión 1.0

Licencia GPL de GNU
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
    Author: Jorge A. Solano

Este prorgrama indica el color de semaforo Epidemiológico COVID de la CDMX.
• Tener una bd.csv con edad, indicador[0-1]
    • Si el indicador es menor que 0.8 no tiene COVID
    • Si el indicador es mayor o igual a 0.8 tiene COVID
    • La muestra será de 100 individuos
• Calcular el color del semáforo COVID en torno a:
    • Verde: 0 individuos con COVID
    • Amarillo: 1-30 individuos con COVID
    • Naranja: 31-70 individuos con COVID
    • Rojo: 71-100 individuos con COVID
• Calcular la edad promedio de las personas con COVID
'''

#importamos la librería panda y sus derivados, esta nos ayudará a leer archivos de tipo .xlsx y .csv
import pandas as pd
import numpy as np

print("\n\tBienvenido\t\n")

#para facilitar el proceso nosotros ya tenemos una base de datos precreada
#leeremos nuestra base de datos identificada como bd.csv
df=pd.read_csv('bd.csv')

#crearemos una lista con los datos que tenemos en la columna seleccionada (indicador)
condiciones=[(df['Indicador']<0.8),(df['Indicador']>=0.8)]
caso=['Negativo','Positivo']

#creamos una columna nueva que indique si el paciente tiene o no covid
df['Resultado']=np.select(condiciones,caso)

semC=len(df[df['Resultado']=='Positivo'])   #Definimos una nueva variable 

#Condiciona el color del semáforo
if semC==0:
    print("Te informo que el color del semáforo epidemiológico de la CDMX es Verde.")
elif int(semC)>0 and int(semC)<=30:
    print("Te informo que el color del semáforo epidemiológico de la CDMX es Amarillo.")
elif int(semC)>30 and int(semC)<=70:
    print("Te informo que el color del semáforo epidemiológico de la CDMX es Naranja.")
elif int(semC)>70 and int(semC)<=100:
    print("Te informo que el color del semáforo epidemiológico de la CDMX es Rojo.")
else:
    print("Opción no válida")
print("Toma tus precauciones. No bajes la guardia ;)")

#la siguiente linea calculará el promedio de la edad 
print("\nEl promedio de edad de los casos positivos es",df['Edad'].mean().round(0),"años.") 
