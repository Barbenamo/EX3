from src.GraphElements import NodeData as ND
from src.GraphInterface import GraphInterface
import json


class DiGraph(GraphInterface):
    """This abstract class represents an interface of a graph."""

    def __init__(self):
        self.graph = {}
        self.MC = 0
        self.numOfEdges = 0
        self.last_pos = (0, 0, 0)

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self.graph)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.numOfEdges

    def get_all_v(self) -> dict:
        """
        return a dictionary of all the nodes in the Graph, each node is represented using a pair  (key, node_data)
        """
        return self.graph

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
         """
        if self.graph.__contains__(id1):
            return self.graph.get(id1).guests
        return {}

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
        weight)
        """
        if self.graph.__contains__(id1):
            return self.graph.get(id1).neighbors
        return {}

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.MC

    def add_edge(self, src: int, dest: int, w: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if not self.graph.__contains__(src) or not self.graph.__contains__(dest):
            return False
        if self.graph.get(src).has_nei(dest) or src == dest:
            return False
        self.graph.get(src).add_nei(dest, w)
        self.graph.get(dest).add_guest(src, w)
        self.numOfEdges += 1
        self.MC += 1
        return True

    def add_node(self, id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        if self.graph.__contains__(id):
            return False
        if pos is None:
            pos = self.last_pos
        else:
            self.last_pos = (pos[0] + 1, pos[1] + 1, pos[2] + 1)
        node = ND(id, pos)
        self.graph[id] = node
        self.MC += 1

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        if not self.graph.__contains__(node_id):
            return False
        neighbors = [key for key in self.graph.get(node_id).neighbors]
        guests = [key for key in self.graph.get(node_id).guests]
        for runner in neighbors:
            self.remove_edge(node_id, runner)
        for runner in guests:
            self.remove_edge(runner, node_id)
        self.graph.pop(node_id)
        self.MC += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        if not self.has_edge(node_id1, node_id2):
            return False
        self.graph.get(node_id1).remove_nei(node_id2)
        self.graph.get(node_id2).remove_guest(node_id1)
        self.numOfEdges -= 1
        return True

    def has_edge(self, src: int, dest: int) -> bool:
        """
        check if a certain edge is in the graph
        :param src: the source node
        :param dest: the destination node
        :return: True if the edge is in the graph, otherwise return False
        """
        if not self.graph.__contains__(src) or not self.graph.__contains__(dest):
            return False
        if not self.graph.get(src).has_nei(dest):
            return False
        else:
            return True

    def get_node(self, key: int) -> ND:
        """
        get a node from the graph
        :param key: the node we want to get
        :return: the node, None if the node is not in the graph
        """
        if self.has_node(key):
            return self.graph.get(key)
        else:
            return None

    def has_node(self, key: int) -> bool:
        """
        check if a node is in the graph
        :param key: the node id to be checked
        :return: True if the node is in the graph, otherwise False
        """
        return self.graph.__contains__(key)

    def __str__(self):
        view_graph = self.as_dict()
        return view_graph.__str__()

    def __eq__(self, other):
        if not isinstance(other, DiGraph):
            return False
        if self.v_size() != other.v_size() or self.e_size() != other.v_size():
            return False
        for node in self.get_all_v().values():
            if other.get_node(node.key) is None:
                return False
            edges = self.all_out_edges_of_node(node.key).items()
            other_edges = other.all_out_edges_of_node(node.key).items()
            if len(edges) != len(other_edges):
                return False
            if not edges.__eq__(other_edges):
                return False
        return True

    def as_dict(self) -> dict:
        """
        insert a graph to a dictionary according to the JSON format
        :return: dict representing the graph
        """
        nodes = []
        edges = []
        for runner in self.get_all_v().values():
            nodes.append(runner.node_info())
            my_edges = self.all_out_edges_of_node(runner.key)  # {"1": 5, "2": 4}
            for key, value in my_edges.items():  # {(1, 5), (2, 4)}
                edge_info = {"src": runner.key, "dest": key, "w": value}
                edges.append(edge_info)
        view_graph = {"Nodes": nodes, "Edges": edges}
        return view_graph
