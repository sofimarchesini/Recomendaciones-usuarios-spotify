import cargar_grafos 
import biblioteca 
import constantes

def comandos(entrada, grafo,playlists,usuarios):
    comando = entrada[0]
    
    if comando == CAMINO:
        if (len(entrada)) != 3:
            print(ERROR_PARAMETROS)   
            return
        procesar_camino(entrada[1], entrada[2],grafo,playlists,usuarios)
    
    elif comando == MAS_IMPORTANTES:
        if len(entrada) != 2 or not entrada[1].isdigit():
            print(ERROR_PARAMETROS) 
            return
        grafo_canciones =  crear_grafo_canciones(playlists)
        mas_importantes(entrada[1],grafo_canciones)
    
    elif comando == RECOMENDACION:
        if entrada[1] != "usuarios" or entrada[1] != "canciones" or not entrada[2].isdigit() or len(entrada) != 3:
            print(ERROR_PARAMETROS)
            return 
        recomendacion(entrada[1], entrada[2])
    
    elif comando == CICLO:
        if not entrada[1].isdigit() or len(entrada) != 3:
            print(ERROR_PARAMETROS)
            return
        grafo_canciones =  crear_grafo_canciones(playlists)
        ciclo(entrada[1], entrada[2],grafo)
    
    elif comando == RANGO:
        if len(entrada) != 3 or not entrada[1].isdigit():
            print(ERROR_PARAMETROS)
            return
        grafo_canciones =  crear_grafo_canciones(playlists)
        rango(entrada[1], entrada[2],grafo)
    
    elif comando == CLUSTERING:
        if len(entrada)>2:
            print(ERROR_PARAMETROS)
            return
        grafo_canciones =  crear_grafo_canciones(playlists)
        coeficiente_clustering(entrada[1] if entrada[1] else None,grafo)
    
    else:
        return


def main():
    tsv = open("spotify-mini.tsv")
    bipartito,playlists,usuarios = crear_grafo_usuarios(tsv)
    entrada = tsv.input().strip().split()
    while entrada:
        comandos(entrada, bipartito ,playlists,usuarios)
        entrada = tsv.input().strip().split()
    tsv.close()

main()