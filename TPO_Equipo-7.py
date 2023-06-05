def LineaADiccionario(linea):
    """Convierte una línea con el formato de 'aeropuertos.txt' en un diccionaro"""
    # Intento convertir la línea, si no puedo devuelvo None.
    try:
        linea = linea.rstrip("\n")
        split_archivo = linea.split(";")
        ubic_split = split_archivo[3].split(",")
    except:
        print("[!] Ignorando una línea porque no contiene el formato especificado.")
        return None
    
    # Convierto todos mis datos en un diccionario
    try:
        datos = {
            "IATA": split_archivo[0].strip(),
            "ICAO": split_archivo[1].strip(),
            "NOMBRE_AEROPUERTO": split_archivo[2].strip(),
            "UBICACION": {
                "LOCALIDAD": "",
                "REGION": "",
                "PROV": "",
                "PAIS": ""
            }
        }
        if len (ubic_split) == 4:
            datos["UBICACION"]["LOCALIDAD"] = ubic_split[0].strip()
            datos["UBICACION"]["REGION"] = ubic_split[1].strip()
            datos["UBICACION"]["PROV"] = ubic_split[2].strip()
            datos["UBICACION"]["PAIS"] = ubic_split[3].strip()
        if len(ubic_split) == 3:
            datos["UBICACION"]["LOCALIDAD"] = ubic_split[0].strip()
            datos["UBICACION"]["REGION"] = ubic_split[1].strip()
            datos["UBICACION"]["PAIS"] = ubic_split[2].strip()
        elif len(ubic_split) == 2:
            datos["UBICACION"]["REGION"] = ubic_split[0].strip()
            datos["UBICACION"]["PAIS"] = ubic_split[1].strip()
        elif len(ubic_split) == 1:
            datos["UBICACION"]["PAIS"] = ubic_split[0].strip()
        else:
            datos["UBICACION"]["PAIS"] = ubic_split[-1].strip()

        return datos
    except:
        return None

def ObtenerPaises(ubic_archivo):
    """Obtenemos la lista de todos los paises del archivo."""
    paises = []
    archivo = open(ubic_archivo, "rt")
    for linea in archivo:
        try:
            datos = LineaADiccionario(linea)

            if datos["UBICACION"]["PAIS"] not in paises:
                paises.append(datos["UBICACION"]["PAIS"].lower().strip())
        except:
            print("[!] Error convirtiendo una línea.")
            
    return paises

def CargarArchivo(ubic_archivo, filtro_pais=""):
    """ carga el archivo seleccionado y filtra los datos elejidos previamente por el usuario """ 
    resultado = []
    archivo = open(ubic_archivo, "rt")
    # Leo línea por línea el archivo, y lo convierto a un diccionario
    for linea in archivo:
        try:
            datos = LineaADiccionario(linea)

            # Si el nombre del país está en el filtro, lo agregamos a la lista de resultados.
            if filtro_pais.lower() in datos["UBICACION"]["PAIS"].lower():
                resultado.append(datos)
        except Exception as err:
            print(f"[!] ERROR! {err}")
            print(f"[!] Línea: '{linea}'")
    archivo.close()
    return resultado
  
def imprimirDatos(datos):
    """ Imprime de manera prolija los datos solicitados """
    print(f'IATA |  ICAO  |  {"AEROPUERTO":^100}  |  {"UBICACION":^40}')
    print("-"*180)
    for dato in datos:
        localidad = [dato["UBICACION"]["LOCALIDAD"], dato["UBICACION"]["REGION"], dato["UBICACION"]["PROV"], dato["UBICACION"]["PAIS"]]
        localidad = list(filter(lambda x: x != "", localidad))
        print(f'{dato["IATA"]:^3}  |  {dato["ICAO"]:^4}  |  {dato["NOMBRE_AEROPUERTO"]:<100}  |  {", ".join(localidad)}.')

def ordenarDatos(listado):
    """ Ordena el listado por región/provincia y localidad """ 
    datos_ordenados = sorted(listado, key=lambda x: (x["UBICACION"]["REGION"], x["UBICACION"]["LOCALIDAD"]))
    return datos_ordenados

def menu(ubicacion_archivo):
    """ permite al usuario seleccionar los datos que desea visualizar en pantalla """
    while True:
        try:
            # Menu principal
            print('1- Filtrar por Pais. ')
            print('2- Salir. ')

            # Ingrese un número, 1 o 2.
            ch = int(input('Ingrese numero: '))
            while ch not in [1, 2]:
                print('Opcion incorrecta, ingrese numero nuevamente: ')
                ch = int(input('Ingrese numero: '))

            # Si la opción es 1,
            if ch == 1:
                lista_paises = ObtenerPaises(ubicacion_archivo)
                interfaceMenu(lista_paises)
                pais_s = input('Ingrese el pais que desea buscar: ')

                # Si el pais tiene menos de 3 letras, o no está en la lista, es incorrecto.
                while (len(pais_s) < 3) or pais_s.lower() not in lista_paises:
                    print("[!] El nombre del pais es incorrecto. Por favor ingreselo nuevamente.")
                    pais_s = input('Ingrese el pais que desea buscar: ')

                # Se obtiene resultado, lo ordeno y lo imprimo.
                resultado = CargarArchivo(ubicacion_archivo, pais_s)
                ordenar = ordenarDatos(resultado)
                imprimirDatos(ordenar)
                break
            # Si la opción es 2, termina el programa.
            else:
                print('Ciao. ')
                break
        except ValueError:
            print("[!] Debe elegir entre 1 (Filtrar) o 2 (Salir)")

def interfaceMenu(paises):
    listaPaises = []
    for pais in paises:
        if pais not in listaPaises:
            listaPaises.append(pais)
    listaPaises.sort()
    print("\n+Lista de paises disponibles en el archivo = \n")
    for x in listaPaises:
        print(x.title(), end=" | ")
    print("\n")


#inicializar programa
menu("aeropuertos.txt")