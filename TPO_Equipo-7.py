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

resultado = CargarArchivo("aeropuertos.txt", "fRAnCe")
for r in resultado:
    print(r)