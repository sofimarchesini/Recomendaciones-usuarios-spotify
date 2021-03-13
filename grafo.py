class Grafo:
    #Faltan los pesos de las aristas que son el valor del diccionario de cada vertice 
    def __init__(self, vertices = []):
        self.vertices = {}
        for v in vertices:
            self.vertices[v] = {}
    
    def _len_(self):
		return len(self.vertices)
        
    def insertar_vertice(self, vertice):
        if not vertice in self.vertices:
            self.vertices[vertice] = {}     
        
    def insertar_arista(self, vertice1, vertice2):
        if not self.es_adyacente( vertice1,vertice2):
            self.vertices[vertice1][vertice2] = ""
        
    def borrar_vertice(self,vertice):
        for i in self.vertices:
            if vertice in i:
                del self.vertices[i][vertice]
        del self.vertices[vertice]
    
    def validar_vertice(self, v):
        if v not in self: return False
        return True

    def borrar_arista(self, vertice1, vertice2):
        if not self.es_adyacente(vertice1,vertice2): return
        del self.vertices[vertice1][vertice2]


    def es_adyacente(self, vertice1, vertice2):
        return self.vertices[vertice1][vertice2] != None

    def obtener_vertices(self):
        return list(self.vertices.keys())

    def adyacentes(self, vertice):
        return list(self.vertices[vertice].keys())