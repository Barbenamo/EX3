from typing import List
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.GraphElements import NodeData as ND
import json
import queue as q
import heapq as hq
import matplotlib.pyplot as plt
import time


class GraphAlgo(GraphAlgoInterface):
    """This abstract class represents an interface of a graph."""

    def __init__(self):
        self.graph = DiGraph()
    """
    return: the directed graph on which the algorithm works on.
    """
    def get_graph(self) -> DiGraph:
        return self.graph

    """
    Loads a graph from a json file.
    @param file_name: The path to the json file
    @returns True if the loading was successful, False o.w.
    """
    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as open_file:
                view_graph = json.load(open_file) #{"Nodes" : [{"id":1, "pos":55.2}], "Edges": [{"src":1, "dest": 4, "weight": 45.6}]}
                nodes = view_graph['Nodes']
                edges = view_graph['Edges']
                for node in nodes:
                    self.graph.add_node(**node) #{"id":1, "pos":55.2} ->
                for edge in edges:
                    self.graph.add_edge(**edge)
            return True
        except IOError:
            return False


    """
    Saves the graph in JSON format to a file
    @param file_name: The path to the out file
    @return: True if the save was successful, False o.w.
    """
    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as open_file:
                json.dump(self.get_graph().as_dict(), fp=open_file, indent=4)
            return True
        except IOError:
            return False

    """
    Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
    @param id1: The start node id
    @param id2: The end node id
    @return: The distance of the path, a list of the nodes ids that the path goes through
    Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
    Notes:
    If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
    More info:
    https://en.wikipedia.org/wiki/Dijkstra's_algorithm
    """
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.graph is None or not self.graph.has_node(id1) or \
                not self.graph.has_node(id2):
            return float('inf'), []
        if id1 == id2:
            return 0, [id1]
        queue = q.PriorityQueue()
        setattr(ND, "__lt__", lambda this, other: this.weight < other.weight)
        parents = {}
        node = self.graph.get_node(id1)
        node.weight = 0
        node.info = "grey"
        queue.put(node)
        while queue:
            node = queue.get()
            for dest, w in self.graph.all_out_edges_of_node(node.key).items():
                weight = node.weight + w
                temp = self.graph.get_node(dest)
                if temp.weight > weight and temp.info != "black":
                    temp.weight = weight
                    parents[temp.key] = node.key
                    queue.put(temp)
            node.info = "black"
            if node.key == id2:
                s_path = []
                distance = node.weight
                key = id2
                while key != id1:
                    s_path.insert(0, key)
                    key = parents[key]
                s_path.insert(0, id1)
                self.reset()
                return distance, s_path
        self.reset()
        return float('inf'), []

    def findShortestPath(self, src, dest):
        if len(self.graph.graph) == 0 or not self.graph.has_node(src) or \
                not self.graph.has_node(dest):
            return float('inf'), []
        if src == dest:
            return 0, [src]
        # Create a queue for BFS
        queue = [src]
        node = self.graph.get_node(src)
        node.info = "black"

        while queue:
            s = queue.pop(0)

            # if s = dest then print the path and return
            if s == dest:
                path_len = 0
                my_path = []
                node = self.graph.get_node(src)
                while node is not None:
                    my_path.insert(0, node.key)
                    node = node.parent
                    path_len += 1
                return path_len, my_path

                # Get all adjacent vertices of the dequeued vertex s
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for nei_key in self.graph.get_node(s):
                nei = self.graph.get_node(nei_key)
                if nei.info == "white":
                    queue.append(nei_key)
                    nei.info = "black"
                    nei.parent = self.graph.get_node(s)


    """
    Finds the Strongly Connected Component(SCC) that node id1 is a part of.
    @param id1: The node id
    @return: The list of nodes in the SCC
    Notes:
    If the graph is None or id1 is not in the graph, the function should return an empty list []
    """
    def connected_component(self, id1: int, check_tag: bool = False) -> list:
        if self.graph is None or not self.graph.has_node(id1):
            return []
        from_dfs = self.dfs(id1)
        to_dfs = self.reverse_dfs(id1)
        component = set(from_dfs).intersection(to_dfs)
        if check_tag:
            for c in component:
                self.graph.get_node(c).tag = 1
        return list(component)

    """
    Finds all the Strongly Connected Component(SCC) in the graph.
    @return: The list all SCC
    Notes:
    If the graph is None the function should return an empty list []
    """
    def connected_components(self) -> List[list]:
        if self.graph is None:
            return []
        components = []
        for v in self.graph.get_all_v().values():
            if v.tag == -1:
                component = self.connected_component(v.key, True)
                components.append(component)
        self.reset_tag()
        return components

    """
    Plots the graph.
    If the nodes have a position, the nodes will be placed there.
    Otherwise, they will be placed in a random but elegant manner.
    @return: None
    """

    def plot_graph(self) -> None:
        x = []
        y = []
        keys = []
        for node in self.graph.get_all_v().values():
            if node.location is not None:
                x.append(node.location[0])
                y.append(node.location[1])
            elif len(x) == 0:
                x.append(0.0)
                y.append(0.0)
            else:
                x.append(x[len(x) - 1] + 1.0)
                y.append(y[len(y) - 1] + 1.0)
            keys.append(node.key)
        plt.scatter(x, y, s=500, facecolors='none', edgecolors='k')

        for index in range(len(x)):
            plt.text(x[index] - 0.0004, y[index] + 0.000001, str(keys[index]))

        for node in self.graph.get_all_v().values():
            for edge in self.graph.all_out_edges_of_node(node.key).items():
                dest = self.graph.get_node(edge[0])
                weight = edge[1]
                dx = dest.location[0] - node.location[0]
                dy = dest.location[1] - node.location[1]
                plt.arrow(node.location[0] + 0.000000625, node.location[1] + 0.000000625, dx - 0.000000625, dy - 0.000000625, width=0.0001, length_includes_head=True,
                          color='b')
        plt.legend()
        plt.show()

    def reset_tag(self):
        for node in self.graph.get_all_v().values():
            node.tag = -1

    def reset(self):
        for node in self.graph.get_all_v().values():
            node.info = "white"
            node.weight = float('inf')
            node.parent = None

    def dfs(self, src: int):
        queue = [src]
        node = self.graph.get_node(src)
        node.info = "grey"
        while queue:
            node = self.graph.get_node(queue[0])
            for nei in node.neighbors.keys():
                temp = self.graph.get_node(nei)
                if temp.info == "white":
                    queue.append(nei)
                    temp.info = "grey"
            self.graph.get_node(queue.pop(0)).info = "black"
        visited = []
        for v in self.graph.get_all_v().values():
            if v.info == "black":
                visited.append(v.key)
        self.reset()
        return visited

    def reverse_dfs(self, src: int):
        queue = [src]
        node = self.graph.get_node(src)
        node.info = "grey"
        while queue:
            node = self.graph.get_node(queue[0])
            for gue in node.guests.keys():
                temp = self.graph.get_node(gue)
                if temp.info == "white":
                    queue.append(gue)
                    temp.info = "grey"
            self.graph.get_node(queue.pop(0)).info = "black"
        visited = []
        for v in self.graph.get_all_v().values():
            if v.info == "black":
                visited.append(v.key)
        self.reset()
        return visited




if __name__ == '__main__':
    g_algo = GraphAlgo()
    start = time.time()
    file = "C:/Users/chaya/PycharmProjects/ex3/data/G_30000_240000_1.json"
    print("loaded successfully? " + str(g_algo.load_from_json(file)))
    dist, path = g_algo.shortest_path(0, 30000-1)
    print("got path: " + str(dist) + ", " +str(path))

    # print(g_algo.graph.get_node(416).neighbors)
    """dist, path = g_algo.shortest_path(0, 2)
    print(dist, path)
    # the node does not exist
    dist, path = g_algo.shortest_path(0, 7)
    print(dist, path)
    # there isn't a path
    dist, path = g_algo.shortest_path(1, 3)
    print(dist, path)"""

   # graph_scc = g_algo.connected_components()

    #print("connected components: " + str(graph_scc))
    print("--- %s seconds ---" % (time.time() - start))
    # g_algo.plot_graph()"""
