from datetime import datetime

from networkx.classes import Graph

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph=Graph()
        self._idMap={}
        self.aeroports=DAO.getAllAeroports()
        for a in self.aeroports:
            self._idMap[a.ID] = a

    def getNumNodes(self):
        return len(self._graph.nodes())

    def getNumEdges(self):
        return len(self._graph.edges())

    def buildGraph(self, distanzaMinima):
        """Costruisce un grafo con nodi gli aeroporti distanti in media la distanza inserita come input e archi con peso pari alla distanza media
            param: indica la distanza minima"""
        self._graph=Graph()
        archi=DAO.getEdges(distanzaMinima)

        for a in archi:
            nodo1=self._idMap[a.OriginAirportID]
            nodo2=self._idMap[a.DestinationAirportID]
            self._graph.add_edge(nodo1, nodo2, weight=a.Distance)

    def getNodes(self):
        return self._graph.nodes()

    def getEdges(self):
        return self._graph.edges()

    def getEdgeWeight(self, edge):
        """Ritorna il peso dell'arco passato come input, pari alla distanza media dei due aeroporti collegati dall'arco"""
        return self._graph.get_edge_data(edge[0], edge[1])


if __name__=="__main__":
    grafo=Model()
    grafo.buildGraph(4000)
    print(grafo.getEdges())
    print(grafo.getNumNodes())
    print(grafo.getNumEdges())
