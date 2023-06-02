def CargarArchivo(ubic_archivo, filtro_pais=""):
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

def ordenarDatos(datos):
    pass
    
def imprimirDatos(datos):
    """ Imprime de manera prolija los datos solicitados """
    print(f'IATA |  ICAO  |  {"AEREOPUERTO":^65}  |  {"UBICACION":^40}')
    print("-"*140)
    for dato in datos:
        print(f'{dato["IATA"]:^3}  |  {dato["ICAO"]:^4}  |  {dato["NOMBRE_AEROPUERTO"]:^65}  |  {dato["UBICACION"]["LOCALIDAD"]}, {dato["UBICACION"]["REGION"]}, {dato["UBICACION"]["PAIS"]}.')
        
        
resultado = CargarArchivo("aeropuertos.txt", "fRAnCe")
imprimir = imprimirDatos(resultado)
