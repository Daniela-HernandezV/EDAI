'''
Facultad de Ingeniería, UNAM
Estructura de Datos y Algoritmos I, Python
Diagnóstico preventivo Python 
Autor: Daniela Hernández Vázquez. 
Versión 2.0
'''

'''
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
'''
# Explicación del programa
'''
Este prorgrama muestra un menú con 3 opciones. 
La primer opción indica el color de semáforo epidemiológico COVID de la CDMX con referencia a una base de datos de personas contagiadas.
La segunda opción nos muestra un sistema el cual pregunta al usuario los síntomas que tiene y le dá un diagnóstico en base a sus síntomas 
    registrando el caso en otra base de datos mientra el ciclo se repite hasta que se decida salir.
La tercera opción sale del programa     
'''

# Importamos la librería pandas y sus derivados, esta nos ayudará a leer archivos de tipo .xlsx y .csv
import os
os.system("cls")        # Limpiar pantalla
import pandas as pd
import numpy as np

print("\n\tBienvenido a mi programa :)\t")

op = '0'
df = pd.read_csv('bd.csv')        # Creamos un DataFrame(estructura bidimensional)

while(op != '3'):
    print("\n1) Semáforo COVID \n2) Diagnóstico Preventivo \n3) Salir")
    op = input("\nElige la opción que desees realizar: ")
    if op == '1':
        
        print("\n\tElegiste la opción Semáforo COVID")
        
        # Para facilitar el proceso nosotros ya tenemos una base de datos precreada
        # Leeremos nuestra base de datos identificada como bd.csv
        df = pd.read_csv('bd.csv')

        # Crearemos una lista con los datos que tenemos en la columna seleccionada (indicador)
        condiciones = [(df['Indicador']<0.8),(df['Indicador']>=0.8)]
        caso = ['Negativo','Positivo']

        # Creamos una columna nueva que indique si el paciente tiene o no covid
        df['Resultado'] = np.select(condiciones,caso)
        semC = len(df[df['Resultado'] == 'Positivo'])   #Definimos una nueva variable 

        # Condiciona el color del semáforo
        if semC == 0:
            print("\nTe informo que el color del semáforo epidemiológico de la CDMX es Verde.")
        elif int(semC) > 0 and int(semC) <= 30:
            print("\nTe informo que el color del semáforo epidemiológico de la CDMX es Amarillo.")
        elif int(semC) > 30 and int(semC) <= 70:
            print("\nTe informo que el color del semáforo epidemiológico de la CDMX es Naranja.")
        elif int(semC) > 70 and int(semC) <= 100:
            print("\nTe informo que el color del semáforo epidemiológico de la CDMX es Rojo.")
        else:
            print("\nOpción no válida")
        print("Toma tus precauciones, No bajes la guardia ;)")

        # La siguiente linea calculará el promedio de la edad 
        print("\nEl promedio de edad de los casos positivos es",df['Edad'].mean().round(0)) 

    elif op == '2':
    
        print("\n\tElegiste la opción Diagnóstico Preventivo")

        op = '0'
        datos = []
        while(op != '2'):
            print("\n 1) Llenar cuestionario\n 2) Volver al menú principal")
            op = input("\nElige la opción que desees realizar: ")
            
            if op == '1':
                p_nombre = input("\nNombre del paciente: ")
                print(p_nombre+" responde con un 1 si has presentado alguno de los siguientes síntomas o con 0 en el caso de que no")
                
                """
                Pregunta al usuario si padece del síntoma especificado en la variable 'sintoma', siendo 1 sí y 0 no. Cualquier
                otra respuesta numérica hace que se vuelva a hacer la pregunta.
                Regresa Regresa True si el paciente presenta el síntoma y False si no lo presenta. Booleano
                """
                def sintomasPresentes(sintoma):                # Definimos una función que dará valor a los síntomas
                    sintom = int(input(sintoma + ": "))
                    while sintom != 0 and sintom != 1:
                        print("Respuesta no válida, recuerda 1 es sí, 0 es no.")
                        sintom = int(input(sintoma + ": "))
                    if sintom == 0:
                        return False
                    return True

                # Damos un diagnóstico al paciente según sus síntomas
                def Diagnostico(tos, ojos_rojos, catarro, ronquera, estornudos, dolor_garganta, fiebre, congestion_nasal, 
                                dolor_muscular, dolor_cabeza, malestar_general, dificultad_respirar):
                    # Si tiene tos, fiebre y/o dolor de cabeza Y está acompañado de dolor de garganta, ojos rojos y/o malestar general
                    if (tos or fiebre or dolor_cabeza or dolor_garganta) and ( estornudos or catarro or ojos_rojos or dolor_muscular) and (ronquera or congestion_nasal or malestar_general):
                        # Y además tiene dificultad para respirar
                        if dificultad_respirar:
                            # Entonces es un caso grave (lo representamos con el número dos)
                            return " Caso grave"
                        # Sino, entonces es un caso de contagio leve
                        return " Caso leve"
                    # Si no presentaba esa combinación de síntomas y signos,entonces no estaba contagiado
                    return " Sin contagio"
                        
                # Preguntamos los síntomss llamando la función def sintomasPresentes(sintoma) y se sustituyen los parámetros 
                # Almacenamos las variables
                p_tos = sintomasPresentes("Tos")
                p_ojos_rojos = sintomasPresentes("Ojos rojos o conjuntivitis")
                p_catarro = sintomasPresentes("Catarro")
                p_ronquera = sintomasPresentes("Ronquera")
                p_estornudos = sintomasPresentes("Estornudos")
                p_dolor_garganta = sintomasPresentes("Dolor o ardor de garganta")
                p_fiebre = sintomasPresentes("Fiebre mayor a 38.5°C")
                p_congestion_nasal = sintomasPresentes("Congestión nasal")
                p_dolor_muscular = sintomasPresentes("Dolor muscular")
                p_dolor_cabeza = sintomasPresentes("Dolor de cabeza")
                p_malestar_general = sintomasPresentes("Malestar general")
                p_dificultad_respirar = sintomasPresentes("Dificultad para respirar")
           
                #utilizamos la función diagnóstico
                p_diagnostico = Diagnostico(p_tos, p_ojos_rojos, p_catarro, p_ronquera, p_estornudos, p_dolor_garganta, p_fiebre, p_congestion_nasal, 
                                            p_dolor_muscular, p_dolor_cabeza, p_malestar_general, p_dificultad_respirar)
                                            
                if p_diagnostico == " Sin contagio":
                    print("\n" + p_nombre + ", es probable que no tengas COVID-19, tus síntomas podrían corresponder a otro padecimiento.")
                    print("Sin embargo, sigue al pendiente de tu estado de salud, y si presentas compliaciones ponte en contacto con el sector salud.")
                elif p_diagnostico == " Caso leve":
                    print("\n" + p_nombre + ", es posible que tengas COVID-19. Por favor ponte en contacto con el sector salud para notificar sobre tu caso.")
                elif p_diagnostico == " Caso grave":
                    print("\n" + p_nombre + ", padeces de COVID-19 en un estado grave.")
                    print("Es necesario que te dirigas a una institución de salud de forma inmediata.")

                registro = p_nombre +',' +p_diagnostico
                datos.append(registro)
                
            elif op=='2':
                print("Gracias por elegir esta opción. Recuerda, en caso de que presentes algun malestar consulta a tu médico y dá aviso a las autoridades.")
            else:
                print("\nOpción no válida :c")
        print(datos)
        
        # Captura de datos
        a=open("diagnóstico.csv","a")
        a.write(datos)
        a.close()

    elif op=='3':
        print("\nGracias por usar mi programa. Cuidate, no bajes la guarrdia. :)\n")
    else:
        print("Opción no válida")
        
