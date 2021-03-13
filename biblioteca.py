import funciones
import biblioteca
import constantes

def buscar_playlist(cancion,playlists):
    
    """ dic playlists  = {playlist : cancion1,cancion2,cancion3}"""
    for key in playlists.keys():
        for value in playlists.values():
            if value == cancion:
                return key

def buscar_usuario(playlist,usuarios):

    """ dic usuarios = {playlist : usuario}"""
    for key in usuarios.keys():
        if key == playlist:
            return usuarios

def procesar_camino(origen,destino,grafo,playlists,usuarios):
 
    items = playlists.items()
    if not grafo.validar_vertice(origen) or not grafo.validar_vertice(destino):
        print(ERROR_PERTENECE)
        return 
    elif origen not in items or destino not in items:
        print(ERROR_CANCIONES_CAMINO)
        return 
    
    camino = camino_simple(grafo,origen,destino)
    if not camino: print(ERROR_CAMINO)
    else:
        for vertice in camino:
            if vertice in items:
                playlist = buscar_playlist(vertice,playlists)
                print(CANCION_SALIDA.format(vertice,playlist))
            else:
                playlist = buscar_playlist(vertice,usuarios)
                print(USUARIO_SALIDA.format(vertice,playlist)


def mas_importantes(numero_canciones,grafo):
    if numero_canciones == 0:
        print(ERROR_MAS_IMPORTANTES)
    lista  = pagerank(numero_canciones,grafo)
    if lista:
        for i in lista:
            print (f'{i}; ', end="")

def recomendacion(grafo,usuarios_canciones, numero_recomendaciones):
    cant_caminos = 10
    lista = pagerank_random_walks(grafo,numero_recomendaciones, cant_caminos,usuarios_canciones)
    if lista: print(lista)

def ciclo(largo, cancion,grafo):
    if not grafo.validar_vertice(cancion): 
        print(ERROR_PERTENECE)
    lista = devolver_ciclo(largo,cancion,grafo)
    if len(lista) != largo: print(ERROR_CAMINO)
    elif lista:
        for i in lista:
            print(f"{i} --> ", end="")

def rango(saltos, cancion,grafo):
    if not grafo.validar_vertice(cancion): 
        print(ERROR_PERTENECE)
    rango = obtener_rango(grafo,saltos,cancion)
    if rango: print(rango)
    
def coeficiente_clustering(cancion,grafo):   
    if not grafo.validar_vertice(cancion):
        print(ERROR_CLUSTERING)
    else: 
        resultado = obtener_numero_clustering(grafo,cancion)
        if resultado : print(resultado)
