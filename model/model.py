import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._allNodi = None

    def buildGraph(self, dMin):
        self._graph = nx.Graph()
        self._allNodi = DAO.getAlbums(dMin)
        self._graph.add_nodes_from(self._allNodi)

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()