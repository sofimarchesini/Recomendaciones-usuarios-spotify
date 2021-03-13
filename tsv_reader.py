def leer_linea(archivo):
    linea = archivo.readline()
    return linea.strip().split("\t") if linea else None

def tsv_reader(archivo):
    tsv = open(archivo)
    datos= {}
    linea = leer_linea(tsv)
    while linea:
        datos[linea[0]] = {
            "USER_ID": linea[1],
            "TRACK_NAME": linea[2],
            "ARTIST": linea[3],
            "PLAYLIST_ID": linea[4],
            "PLAYLIST_NAME": linea[5],
            "GENRES": linea[6]
        }
        linea = leer_linea(tsv)
    return datos

print(tsv_reader("spotify-mini.tsv"))