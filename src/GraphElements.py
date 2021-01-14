class NodeData:
    """A class which represents data according to a vertex in the graph"""
    def __init__(self, key: int, location: tuple = None):
        self.key = key
        if isinstance(location, str):
            self.location = tuple(location.split(","))
        else:
            self.location = location
        self.parent = None
        self.weight = float("inf")
        self.tag = -1
        self.info = "white"
        self.neighbors = {}
        self.guests = {}

    def add_nei(self, dest: int, weight: float):
        """
        add an adjacent node to our node
        :param dest: the adjacent node
        :param weight: weight of the edge
        :return:
        """
        if not self.has_nei(dest):
            self.neighbors[dest] = weight

    def add_guest(self, src: int, weight: float):
        """
        function which adds a parallel node which is adjacent to our node, in the wrong direction
        :param src: the node which is adjacent
        :param weight: the weight of the edge
        """
        if not self.has_guest(src):
            self.guests[src] = weight

    def remove_nei(self, key: int):
        """
        remove an adjacent node
        :param key: the node to be removed
        """
        if self.has_nei(key):
            self.neighbors.pop(key)

    def remove_guest(self, key: int):
        """
        remove the parallel to an adjacent node
        :param key: the node to be removed
        """
        if self.has_guest(key):
            self.guests.pop(key)

    def has_nei(self, key: int) -> bool:
        """
        check if a node is adjacent to our node
        :param key: the node to be checked
        :return: True if the node is adjacent, otherwise, False
        """
        return self.neighbors.__contains__(key)

    def has_guest(self, key: int) -> bool:
        """
        check if the parallel a node is adjacent to our node
        :param key: the node to be checked
        :return: True if the node is adjacent, otherwise, False
        """
        return self.guests.__contains__(key)

    def __eq__(self, other):
        if isinstance(other, NodeData):
            if self.key == other.key and self.location == other.location:
                return True
        return False

    def __repr__(self):
        node_info = {"id": self.key, "pos": self.location}
        return node_info.__str__()

    def node_info(self) -> dict:
        """
        return the info of the node
        :return: dict of the id and pos of the node
        """
        location_str = f"{self.location[0]},{str(self.location[1])},{str(self.location[2])}"
        return {"id": self.key, "pos": location_str}

    def __lt__(self, other):
        return self.weight < other.weight
