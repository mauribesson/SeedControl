#TEST


#IMPORT
from Configuration import Global
from Entity import Seed
from Control import ControlSeed
import Interface
import os


#configuration
globalConf = Global.Global()


controlSeed = ControlSeed.ControlSeed()


if globalConf.getOS() == "w":
    os.system("cls")

print("TEST APP")
    

print("Progarma Principal")

if globalConf.getDebugMode():
    print("DEBUGGER MODE!!")

key = "s"
while key == "s":
    #Nueva semilla
    seed = Seed.Seed()
    #cargo formulario
    seed.set_name(input("Nombre de la semilla:"))
    seed.set_type(input("Tipo de semilla:"))
    seed.set_time(input("Tiempo de crecimiento la semilla (dias):"))
    seed.set_earth(input("Tierra de la semilla:"))
    seed.set_water(input("Agua de la semilla:"))
    seed.set_nutrients(input("Nutrientes de la semilla:"))
    seed.set_chemical_fertilizer(input("Quimicos de la semilla:"))
    #Agrego la nueva semilla
    controlSeed.save_seed(seed)
    key = input("Agregar otra semilla? s/n ")


print("Listado de Semillas:")
controlSeed.list_seeds()

seed = controlSeed.search_seed(input("Buscar semilla por nombre:"))

if seed is not None:
    controlSeed.show_seed(seed)

input("Precione una tecla para salir....")
