import grafo_cat

def leer_linea(archivo):
    linea = archivo.readline()
    return linea.strip().split("\t") if linea else None

def tsv_reader(archivo, grafo, playlists,usuarios):
    tsv = open(archivo)
    linea = leer_linea(tsv)
    while linea:
 
        cancion = [linea[2],linea[3],linea[4]]
        if not linea[1] in grafo.vertices():
            grafo.agregar_vertice(linea[1])
        if not cancion in grafo.vertices():
            grafo.agregar_vertice(cancion)
        if not grafo.estan_unidos(linea[1], cancion):
            grafo.agregar_arista(linea[1], cancion)
        if not playlists[linea[4]]:
            playlists[linea[4]] = []
        if linea[2] not in playlists[linea[4]]:
            playlists[linea[4]].append(linea[2])
        if not usuarios[linea[4]]:
            usuarios[linea[4]] = []
        if linea[1] not in usuarios[linea[4]]:
            usuarios[linea[4]].append(linea[1])
        linea = leer_linea(tsv)
    

def crear_grafo_usuarios(archivo):
    usuarios = Grafo()
    playlists = {}
    usuarios_playlist = {}
    tsv_reader(archivo, usuarios, playlists,usuarios_playlist)
    return usuarios, playlists,usuarios_playlist

def crear_grafo_canciones(playlists):
    canciones = Grafo()

    for playlist in playlists:
        for j in range(len(playlist)-1):
            for i in range(i+1,len(playlist)):
                cancion1 = playlist[i]
                cancion2 = playlist[j]
                if not canciones.validar_vertice(cancion1):
                    canciones.agregar_vertice(cancion1)
                if not canciones.validar_vertice(cancion2):
                    canciones.agregar_vertice(cancion2)
                if not canciones.estan_unidos(cancion1,cancion2):
                    canciones.agregar_arista(cancion1,cancion2)
    return canciones





"""
"USER_ID": linea[1],
"TRACK_NAME": linea[2],
"ARTIST": linea[3],
"PLAYLIST_ID": linea[4],
"PLAYLIST_NAME": linea[5],
"GENRES": linea[6]"""