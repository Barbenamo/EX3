import unittest
from src.DiGraph import DiGraph
from src.GraphElements import NodeData as ND


class TestDiGraph(unittest.TestCase):

    def test_nodes(self):
        graph = DiGraph()
        for i in range(5):
            graph.add_node(i, (i, i+1, i+2))
        graph.add_node(1, (0, 0, 0))
        self.assertEqual(5, graph.v_size())
        graph.remove_node(1)
        graph.remove_node(2)
        graph.remove_node(3)
        graph.remove_node(7)
        self.assertEqual(2, graph.v_size())
        self.assertIsNone(graph.get_node(1))
        self.assertDictEqual({0: ND(0, (0, 1, 2)), 4: ND(4, (4, 5, 6))}, graph.get_all_v())

    def test_edges(self):
        graph = DiGraph()
        for i in range(5):
            graph.add_node(i, (i, i + 1, i + 2))
        graph.add_edge(0, 1, 58.265)
        graph.add_edge(1, 4, 35.2563)
        graph.add_edge(1, 3, 32.361)
        graph.add_edge(2, 4, 45.2623)
        graph.add_edge(1, 2, 49.66523)
        graph.add_edge(1, 1, 52.3651)
        graph.add_edge(1, 7, 60.26)
        self.assertEqual(5, graph.e_size())
        self.assertFalse(graph.has_edge(1, 7))
        graph.remove_edge(1, 3)
        self.assertEqual(4, graph.e_size())
        self.assertFalse(graph.has_edge(1, 3))
        self.assertTrue(graph.has_edge(1, 2))

    def test_graph(self):
        graph = DiGraph()
        nodes = []
        edges = []
        for i in range(5):
            graph.add_node(i, (i, i + 1, i + 2))
            node_info = {"id": i, "pos": f"{i},{i + 1},{i + 2}"}
            nodes.append(node_info)
        graph.add_edge(0, 1, 58.265)
        graph.add_edge(1, 4, 35.2563)
        graph.add_edge(1, 3, 32.361)
        graph.add_edge(2, 4, 45.2623)
        graph.add_edge(1, 2, 49.66523)
        edges.append({"src": 0, "dest": 1, "w": 58.265})
        edges.append({"src": 1, "dest": 4, "w": 35.2563})
        edges.append({"src": 1, "dest": 3, "w": 32.361})
        edges.append({"src": 1, "dest": 2, "w": 49.66523})
        edges.append({"src": 2, "dest": 4, "w": 45.2623})
        dict_graph = graph.as_dict()
        self.assertListEqual(nodes, dict_graph.get("Nodes"))
        self.assertListEqual(edges, dict_graph.get("Edges"))


if __name__ == '__main__':
    unittest.main()
