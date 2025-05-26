import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._allNodi = None
        self._idMapAlbum = {}

    def buildGraph(self, dMin):
        self._graph = nx.Graph()
        self._allNodi = DAO.getAlbums(dMin)
        self._graph.add_nodes_from(self._allNodi)
        for nodo in self._allNodi:
            self._idMapAlbum[nodo.AlbumId] = nodo
        archi = DAO.getAllEdges(self._idMapAlbum)
        self._graph.add_edges_from(archi)

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getNodi(self):
        return self._graph.nodes()

    def getComponenteConnessa(self, nodo):
        vicini = nx.neighbors(self._graph, nodo)
        dimensione = 1
        durata = nodo.dTot
        for vicino in vicini:
            dimensione += 1
            durata += vicino.dTot
        return dimensione, durata