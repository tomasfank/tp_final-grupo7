def CargarArchivo(ubicacion, pais=""):
    archivo = open(ubicacion, "rt")
    for linea in archivo:
        try:
            linea = linea.rstrip("\n")
            csv = linea.split(";")

            datos = {
                "IATA": csv[0],
                "ICAO": csv[1],
                "NOMBRE_AEROPUERTO": csv[2],
                "UBICACION": {
                    "LOCALIDAD": "",
                    "REGION": "",
                    "PAIS": ""
                }
            }
            ubic_csv = csv[3].split(",")
            if len(ubic_csv) == 3:
                datos["UBICACION"]["LOCALIDAD"] = ubic_csv[0]
                datos["UBICACION"]["REGION"] = ubic_csv[1]
                datos["UBICACION"]["PAIS"] = ubic_csv[2]
            elif len(ubic_csv) == 2:
                datos["UBICACION"]["REGION"] = ubic_csv[0]
                datos["UBICACION"]["PAIS"] = ubic_csv[1]
            else:
                datos["UBICACION"]["PAIS"] = ubic_csv[0]

            ## hacer algo con los datos cargados
            if pais in datos["UBICACION"]["PAIS"]:
                print(datos)

            ## fin de hacer algo con los datos cargados            

        except Exception as e:
            print(f"ERROR! {e}")
            print(f"Línea: '{linea}'")
    archivo.close()

CargarArchivo("aeropuertos.txt", "Australia")