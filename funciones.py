def dfs(grafo,v,w,visitados,lista,path):
    visitados.add(v)
    path.append(v)
    if (v==w): lista.append(path)
    else:
        for i in grafo.adyacentes(v):
            if i not in visitados: dfs(grafo,i,w,visitados,lista,path)

    visitados.remove()
    path.pop()

def camino_simple(grafo,v,w):
    visitados = set()
    path = []
    lista = []
    minimo = 999999999
    dfs(grafo,v,w,visitados,lista,path)
    for i in lista:
        if len(i) < minimo:
            minimo = i

    return minimo 


def devolver_ciclo(grafo,largo,cancion):
    visitados = set()
    camino = []
    ciclo = dfs_ciclo(grafo,cancion,cancion,visitados,camino,largo)
    return ciclo


def dfs_ciclo(grafo,origen,v,visitados,camino,largo):
    visitados.add(v)
    camino.append(v)
    if len(visitados) == largo and v==cancion:
        return camino
    for w in grafo.adyacentes(v):
        if w not in visitados:
            dfs_ciclo(grafo,origen,w,visitados,camino)
    visitados.remove(v)
    camino.pop()
    return False

def obtener_rango(grafo,n,origen):
    q = Cola()
    q.encolar(origen)
    orden = {}
    orden[origen] = 0
    q.encolar(origen)
    canciones_en_rango = 0
    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            if w not in orden:
                orden[w] = orden[v]+1
                q.encolar(w)
                if orden[w] == n:
                    canciones_en_rango += 1
                if orden[w] > n:
                    return canciones_en_rango


def pagerank(grafo):
    costante = 0,85
    rank = {}
    rank = pagerank_(grafo,costante,rank)
    return rank

def pagerank_(grafo,costante,rank):
    for vertice in grafo.obtener_vertices():
        rank[vertice] = 1/float(grafo._len_())

    for _ in range(10):
        for vertice in grafo.obtener_vertices():
            suma = 0
            rank_nuevo = node.get('rank')
            for w in grafo.adyacentes(vertice):
                cant_ady = len(grafo.adyacentes(w))
                if cant_ady > 0:
                    suma += rank_nuevo[w]/ float(cant_ady)) * ranks[n[1]]
            else: 
                adyacentes = grafo[vertice]
                for n in adyacentes:
                    if rank[n] is not None:
                        cant = len(grafo.adyacentes(n))
                        suma += (1 / float(cant)) * rank[n]
        
            rank[vertice] = ((1 - float(costante)) * (1/float(grafo._len_()))) + costante*suma
    return rank

def pagerank_random_walks(grafo, long, cant_caminos,usuarios_canciones):
    rank = []
    vertices = grafo.obtener_vertices()
    for i in range(cant_caminos):
        camino = []
        actual = vertice_aleatorio(vertices)
        camino.append(verticeActual)
        for j in range(long):
            adyacentes = actual.adyacentes()
            if adyacentes:
                actual = choice(actual.obtener_adyacentes())
                camino.append(actual)
        rank.append(camino)

    return rank

def coeficiente_clustering(cancion,grafo):

    adyacentes = grafo.adyacentes(cancion)
    if len(adyacentes) < 2: return 0
    cont = 0
    for vertice in adyacentes:
        for i in adyacentes:
            if grafo.es_adyacente(vertice,i):
                cont += 0,5
    
    return 2.0*cont/(len(adyacentes)*(len(adyacentes)-1))
