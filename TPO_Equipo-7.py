def CargarArchivo(ubic_archivo, filtro_pais=""):
    """ carga el archivo seleccionado y filtra los datos elejidos previamente por el usuario """ 
    resultado = []
    archivo = open(ubic_archivo, "rt")
    for linea in archivo:
        try:
            linea = linea.rstrip("\n")
            csv = linea.split(";")
            ubic_csv = csv[3].split(",")
        except:
            print("ERROR! Ignorando una línea porque no contiene el formato especificado.")
            continue
        
        try:
            datos = {
                "IATA": csv[0].strip(),
                "ICAO": csv[1].strip(),
                "NOMBRE_AEROPUERTO": csv[2].strip(),
                "UBICACION": {
                    "LOCALIDAD": "",
                    "REGION": "",
                    "PAIS": ""
                }
            }

            if len(ubic_csv) == 3:
                datos["UBICACION"]["LOCALIDAD"] = ubic_csv[0].strip()
                datos["UBICACION"]["REGION"] = ubic_csv[1].strip()
                datos["UBICACION"]["PAIS"] = ubic_csv[2].strip()
            elif len(ubic_csv) == 2:
                datos["UBICACION"]["REGION"] = ubic_csv[0].strip()
                datos["UBICACION"]["PAIS"] = ubic_csv[1].strip()
            else:
                datos["UBICACION"]["PAIS"] = ubic_csv[0].strip()

            ## hacer algo con los datos cargados
            if filtro_pais.lower() in datos["UBICACION"]["PAIS"].lower():
                resultado.append(datos)
            ## fin de hacer algo con los datos cargados            

        except Exception as e:
            print(f"ERROR! {e}")
            print(f"Línea: '{linea}'")
    archivo.close()
    return resultado
  
def imprimirDatos(datos):
    """ Imprime de manera prolija los datos solicitados """
    print(f'IATA |  ICAO  |  {"AEROPUERTO":^100}  |  {"UBICACION":^40}')
    print("-"*180)
    for dato in datos:
        if dato["UBICACION"]["LOCALIDAD"] == "":
            print(f'{dato["IATA"]:^3}  |  {dato["ICAO"]:^4}  |  {dato["NOMBRE_AEROPUERTO"]:<100}  |  {dato["UBICACION"]["REGION"]}, {dato["UBICACION"]["PAIS"]}.')
        else:
            print(f'{dato["IATA"]:^3}  |  {dato["ICAO"]:^4}  |  {dato["NOMBRE_AEROPUERTO"]:<100}  |  {dato["UBICACION"]["LOCALIDAD"]}, {dato["UBICACION"]["REGION"]}, {dato["UBICACION"]["PAIS"]}.')

def ordenarDatos(listado):
    """ Ordena el listado por región/provincia y localidad """ 
    datos_ordenados = sorted(listado, key=lambda x: (x["UBICACION"]["REGION"], x["UBICACION"]["LOCALIDAD"]))
    return datos_ordenados

def menu():
    """ permite al usuario seleccionar los datos que desea visualizar en pantalla """
    while True:
        try:
            print('1- Filtrar por Pais. ')
            print('2- Salir. ')
            ch = int(input('Ingrese numero: '))
            while ch not in [1, 2]:
                print('Opcion incorrecta, ingrese numero nuevamente: ')
                ch = int(input('Ingrese numero: '))
            if ch == 2:
                print('Ciao. ')
            else:
                pais_s = input('Ingrese el pais que desea buscar: ')     
                resultado = CargarArchivo(ubicacion_archivo, pais_s)
                ordenar = ordenarDatos(resultado)
                imprimirDatos(ordenar)
                break
        except ValueError:
            print("Debe elegir entre 1 (Filtrar) o 2 (Salir)")

#inicializar programa
ubicacion_archivo = "aeropuertos.txt"
menu()