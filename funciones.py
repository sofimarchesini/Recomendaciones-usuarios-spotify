from collections import*
from constantes import*
from random import randint


def devolver_camino_( padres, fin,origen):
    camino = []
    while fin != origen:
        camino.append(fin)
        fin = padres[fin]
    camino.append(origen)
    return camino[::-1]


def devolver_camino(grafo, origen, fin):
    padres = bfs_camino(grafo, origen, fin)
    if not padres: return None
    camino = devolver_camino_( padres, fin,origen)
    return camino


def bfs_camino(grafo, origen,destino):
    padres = {}
    visitados = set()
    visitados.add(origen)
    padres[origen] = None
    q = deque([])
    q.append(origen)
    while q:
        vertice = q.popleft()
        for adyacente in grafo.adyacentes(vertice):
            if adyacente not in visitados:
                padres[adyacente] = vertice
                visitados.add(adyacente)
                q.append(adyacente)
                if adyacente == destino:
                    return padres
    return None


def bfs(grafo, origen):
    padres = {}
    orden = {}
    visitados = set()
    padres[origen] = None
    orden[origen] = 0
    visitados.add(origen)
    q = deque([])
    q.append(origen)
    while q:
        v = q.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                padres[w] = v
                orden[w] = orden[v] + 1
                visitados.add(w)
                q.append(w)
    
    return orden


def dfs_ciclo(grafo, n,largo,origen,cancion, visitados, orden):

    if origen == cancion and n == largo:
        return True, [origen]

    for w in grafo.adyacentes(origen):
        if w == cancion and n != largo - 1 or orden[w] > (largo - n): 
            continue
        if w in visitados: continue
        visitados.add(w)
        ciclo,lista = dfs_ciclo(grafo,n+1, largo, w,cancion, visitados, orden)
        if ciclo:
            lista.append(origen)
            return ciclo, lista
        
        visitados.remove(w)
    
    return False, None

def devolver_ciclo(grafo,largo,cancion):
    orden = bfs(grafo,cancion)
    visitados = set()
    ciclo, lista = dfs_ciclo(grafo,0,largo, cancion, cancion, visitados,orden)
    if ciclo: lista.reverse()
    return lista


def obtener_rango(grafo,n ,origen):
    q = deque([])
    q.append(origen)
    orden = {}
    visitados = set()
    visitados.add(origen)
    orden[origen] = 0
    canciones_en_rango = 0
    while q:
        v = q.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                orden[w] = orden[v]+1
                if orden[w] == n: canciones_en_rango += 1
                if orden[w] > n: break
                q.append(w)
    return canciones_en_rango


def pagerank(grafo,canciones):
    rank = {}
    const  = 0.85
    pagerank_(grafo,float(const),rank)
    return sorted([(rank[v], v) for v in rank if v in canciones.keys()], reverse=True)


def pagerank_(grafo, const ,rank):
    
    largo_grafo = grafo._len_()
    for vertice in grafo.obtener_vertices():
        rank[vertice] = (1-const)/largo_grafo

    for _ in range(20):
        for v in grafo.obtener_vertices():
            rank[v] = (1 - const) / largo_grafo + const * sum(rank[w] /len(grafo.adyacentes(w)) for w in grafo.adyacentes(v))


def random_walks_inicializar(rank,dic):
    for i in rank:
        if i not in dic:dic[i] = 1


def pagerank_random_walks(grafo,usuarios_canciones):
    dic = {}
    for cancion in usuarios_canciones:
        camino = random_walks(grafo,cancion)
        random_walks_inicializar(camino,dic)
        pagerank_personalizado(camino,dic,grafo)
    return dic
        
def pagerank_personalizado(camino,dic,grafo):
    for j in range(20):
            i = 1
            while i <= 20:
                largo_ady = len(grafo.adyacentes(camino[i-1]))
                dic[camino[i-1]] = (dic[camino[i]] /largo_ady)
                i += 1

def random_walks(grafo,usuario_cancion):
    camino = [usuario_cancion]
    actual = usuario_cancion

    for j in range(20):
        adyacentes = grafo.adyacentes(actual)
        actual = adyacentes[(randint(0,len(adyacentes)-1))]
        camino.append(actual)

    return camino


def obtener_numero_clustering(grafo, cancion):

    adyacentes  = grafo.adyacentes(cancion)
    if len(adyacentes) < 2: return 0.000
    aristas=0
    for w in adyacentes:
        for i in adyacentes:
            if w != i:
                if grafo.es_adyacente(i,w) and i!=w:aristas+=1

    return aristas/(len(adyacentes)*(len(adyacentes)-1))