#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


from datetime import date
from datetime import datetime
import pandas as pd
import openpyxl
import random
from getpass import getpass


path = R"D:\Chuandi1\Documents Master\Clases\Python\Tarea\estadisticas.xlsx"
estadisicas = openpyxl.load_workbook(path)
solitary_game = estadisicas["Hoja1"]
group_game = estadisicas["Hoja2"]


solitary_game["A1"] = "Nombre"
solitary_game["B1"] = "Intentos"
solitary_game["C1"] = "Fecha"
solitary_game["D1"] = "Dificultad"
solitary_game["E1"] = "Numero"
group_game["A1"] = "Nombre"
group_game["B1"] = "Intentos"
group_game["C1"] = "Fecha"
group_game["D1"] = "Dificultad"
group_game["E1"] = "Numero"

def Menu():
    print("\nBienvenido al juego ADIVINA EL NUMERO!!\n")
    print("MENU PRINCIPAL\n")
    print("1. Partida modo solitario")
    print("2. Partida 2 Jugadores")
    print("3. Estadística")
    print("4. Salir")
    

def Num_generator():
    
    num = random.randint(1, 1000)
    return num
    
def Escoger_diff():
    
    print("1. Fácil (20 intentos)")
    print("2. Medio (12 intentos)")
    print("3. Difícil (5 intentos)")
    
    
def Juego(diff, num, opt):
    contador = 1
    ganar = 0 
    while contador < diff and ganar == 0 :
        try:

            valor = int(input("\nEscoge tu numero y veamos que tan cerca estas del numero que yo pienso: "))
            if valor > num:
                print("\nel numero que estas buscando es menor, te quedan ", diff - (contador), " intentos")
                contador += 1
            elif valor < num:
                print("\nel numero que estas buscando es mayor, te quedan ", diff - (contador), " intentos")
                contador += 1
            else:
                ganar = 1
        except ValueError:
            print("debes escoger un numero valido, intenta de nuevo!!")
        
    if ganar == 1:
        if opt == 1:
            
            print("\nfelicitaciones el numero que estabas buscando es el: ", num, " y lo adivinaste en ", contador, " intentos")
            nombre = input("escribre tu nombre")
            solitary_game.append([nombre, contador, datetime.now(),diff, num ])
            
            estadisicas.save(R"D:\Chuandi1\Documents Master\Clases\Python\Tarea\estadisticas.xlsx")
        else:
            print("\nfelicitaciones el numero que estabas buscando es el: ", num, " y lo adivinaste en ", contador, " intentos")
            nombre = input("escribre tu nombre")
            group_game.append([nombre, contador, datetime.now(), diff, num ])
            
            estadisicas.save(R"D:\Chuandi1\Documents Master\Clases\Python\Tarea\estadisticas.xlsx")
        
    else:
        print("\nlo siento mucho, el numero que debiste adivinar es: ", num)
    
    


def Menus():
    while True:

        option_menu = 0
        num = Num_generator()

        while not 1 <= option_menu <= 4:
            try:
                print("Bienvenido al juego ADIVINA EL NUMERO dle 1 al 1000!!")
                print("MENU PRINCIPAL")
                print("1. Partida modo solitario")
                print("2. Partida 2 Jugadores")
                print("3. Estadística")
                print("4. Salir")
                option_menu = int(input("\nEscoge una de las opciones para continuar: \n"))
            except ValueError:
                print("debes escoger un numero valido, intenta de nuevo!!")

        if option_menu == 1:
            diff = 0

            while not 1 <= diff <= 3:
                try:
                    print("1. Fácil (20 intentos)")
                    print("2. Medio (12 intentos)")
                    print("3. Difícil (5 intentos)")
                    diff = int(input("\nEscoge la dificultad para continuar: \n"))
                    if diff == 1:
                        Juego(20,  num, 1)
                    elif diff == 2:
                        Juego(12,  num, 1)
                    elif diff == 3:
                        Juego(5,  num, 1)
                except ValueError:
                    print("debes escoger un numero valido, intenta de nuevo!!")
                
        
        elif option_menu == 2:
            num = 0
            diff = 0
            while not 1 <= num <= 1000:
                num = int(getpass("el jugar 1 escoge un numero entre el 1 y el 1000: "))
                
            while not 1 <= diff <= 3:
                print("1. Fácil (20 intentos)")
                print("2. Medio (12 intentos)")
                print("3. Difícil (5 intentos)")
                diff = int(input("\nEscoge la dificultad para continuar: \n"))
                if diff == 1:
                    Juego(20,  num, 2)
                elif diff == 2:
                    Juego(12,  num, 2)
                elif diff == 3:
                    Juego(5,  num, 2)
                           
                           

        elif option_menu == 3:
            
            

            print("\nestas son las estadistiacas de los 10 mejores juegos en SOLITARIO!")
            
            df1 = pd.read_excel(path, sheet_name = "Hoja1")
            print(df1.sort_values(by=["Dificultad","Intentos"]).head(10))
                
            print("\n\nestas son las estadistiacas de los 10 mejores juegos en PAREJAS!\n\n")
            
            df2 = pd.read_excel(path, sheet_name = "Hoja2")
            print(df2.sort_values(by=["Dificultad","Intentos"]).head(10))
            
            print("\n")

        elif option_menu == 4:

            print(4)
            return False

    
Menus()

    #   


    


# In[1]:


273


# In[ ]:




