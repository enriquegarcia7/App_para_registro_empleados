import os
import numpy as np #para ponerle alias a numpy como np

#--------------- VARIABLES ----------------

opcion_menu=""
tamaño = 3 # --> cantidad maxima de registros
nombres = np.empty(tamaño, dtype = object)   #arreglo con numpy
edades = np.empty(tamaño, dtype = int)
sexos = np.empty(tamaño, dtype = object)
sueldos = np.empty(tamaño, dtype= int)

#--------------- CODIGO  ----------------
os.system("cls")
while True:
    opcion_menu = str(input(''' 
        ================MENU===============                    
        1.- Cargar Datos
        2.- Listar Todos los registros
        3.- Ver estadisticas
        4.- Salir

    Elija una opcion:   '''))
    if opcion_menu == "1":
        os.system("cls")
        os.system("pause")
        
        for k in range (tamaño):
            os.system("cls")
            nombres[k]= str(input("Ingrese nombre:  ")).strip().capitalize()
            while not len(nombres[k])>0:
                print("Error... no puede estar vacio")
                nombres[k]= str(input("Ingrese nombre:  ")).strip().capitalize()

            edades[k]= int(input("Ingrese Edad:  "))
            while not (edades[k])>=18:
                print("Error... la edad debe ser mayor o igual a 18 ")
                edades[k]= int(input("Ingrese Edad:  "))
        
            sexos[k]= str(input("Ingrese el sexo (F o M):  ")).upper()
            while not (sexos[k]=="M" or sexos[k]=="F"):
                print("Error... debe ser F o M ")
                sexos[k]= str(input("Ingrese el sexo (F o M):  ")).upper()
        
            sueldos[k]= int(input("Ingrese Sueldo:  "))
            while not (sueldos[k])>=0:
                print("Error... debe ser mayor a cero ")
                sueldos[k]= int(input("Ingrese Sueldo:  "))
            print(f'''  

            Carga correcta:
    
            Nombre: \t     {nombres[k]}
            Edad:   \t     {edades[k]}
            Sexo:   \t     {sexos[k]}
            Sueldo: \t    ${sueldos[k]}   
            ''')

            os.system("pause")
                
    if opcion_menu == "2":
        os.system("cls")
        print("opcion 2")
        for k in range(tamaño):
            os.system("cls")
            print(f'''  
            
            Mostrando registro {k+1}
            
            Nombre: \t     {nombres[k]}
            Edad:   \t     {edades[k]}
            Sexo:   \t     {sexos[k]}
            Sueldo: \t    ${sueldos[k]}   ''')
            
            os.system("pause")
            
    if opcion_menu == "3":
        os.system("cls")
        max_sueldo=sueldos.max()
        for k in range (tamaño):
            if sueldos[k] == max_sueldo:
                print(f'''
                El sueldo mas alto corresponde a:
                Nombre: {nombres[k]} \t Sueldo: {sueldos[k]} 
                ''')
        os.system("pause")
        
    if opcion_menu == "4":
        os.system("cls")
        salir = str(input("Seguro que desea salir diguite S o N:  ")).strip().upper()
        if salir == "S":
            break
        else:
            continue 