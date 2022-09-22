# Programa para convertir kg a lbs
# May 24, 2021
# se crea una función para convertir kilogramos a libras
def convertidorkg():
    kgs = input("Kilogramo(s): ")
    kgs_a_lbs = round(int(kgs) / 0.453592, 2)
    print(f"{kgs} kilogramo(s) en libra(s) es {kgs_a_lbs}")

# se crea otra función para convertir libras a kilogramos
def convertidorlb():
    lbs = input("Libra(s): ")
    lbs_a_kgs = round(int(lbs) * 0.453592, 2)
    print(f"{lbs} libra(s) en kilogramo(s) es {lbs_a_kgs}")

# se crea otra función para elegir que convertidor se usará
def elegir():
    elegir_el_convertidor = input("¿Convertir kgs o lbs? (kgs o lbs): ")
    if elegir_el_convertidor == "kgs":
        convertidorkg()
    elif elegir_el_convertidor == "lbs":
        convertidorlb()
    else:
        print("Error, elige 'kgs' o 'lbs'")


elegir()
