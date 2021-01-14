import unittest
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(unittest.TestCase):
    def test_save_load(self):
        graph_algo = GraphAlgo()
        graph = graph_algo.get_graph()
        for i in range(5):
            graph.add_node(i, (i, i+1, i+2))
        graph.add_edge(0, 1, 58.265)
        graph.add_edge(1, 4, 35.2563)
        graph.add_edge(1, 3, 32.361)
        graph.add_edge(2, 4, 45.2623)
        graph.add_edge(1, 2, 49.66523)
        graph_algo.save_to_json("MyGraph.txt")
        new_graph_algo = GraphAlgo()
        new_graph_algo.load_from_json("MyGraph.txt")
        self.assertEqual(graph_algo.graph, new_graph_algo.graph)

    def test_shortest_path(self):
        graph_algo = GraphAlgo()
        graph = graph_algo.get_graph()
        for i in range(5):
            graph.add_node(i, (i, i + 1, i + 2))
        graph.add_edge(0, 1, 58.265)
        graph.add_edge(1, 4, 35.2563)
        graph.add_edge(1, 3, 32.361)
        graph.add_edge(2, 4, 45.2623)
        graph.add_edge(1, 2, 49.66523)
        self.assertTupleEqual((93.5213, [0, 1, 4]), tuple(graph_algo.shortest_path(0, 4)))
        graph.remove_edge(1, 4)
        graph.add_edge(1, 4, 160.256)
        self.assertTupleEqual((153.19253, [0, 1, 2, 4]), tuple(graph_algo.shortest_path(0, 4)))
        self.assertTupleEqual((float('inf'), []), tuple(graph_algo.shortest_path(1, 7)))
        self.assertTupleEqual((0, [2]), tuple(graph_algo.shortest_path(2, 2)))

    def test_connected_components(self):
        graph_algo = GraphAlgo()
        graph = graph_algo.get_graph()
        for i in range(5):
            graph.add_node(i, (i, i + 1, i + 2))
        graph.add_edge(1, 0, 58.265)
        graph.add_edge(0, 2, 35.2563)
        graph.add_edge(2, 1, 32.361)
        graph.add_edge(0, 3, 45.2623)
        graph.add_edge(3, 4, 49.66523)
        self.assertListEqual([3], graph_algo.connected_component(3))
        self.assertListEqual([[0, 1, 2], [3], [4]], graph_algo.connected_components())


if __name__ == '__main__':
    unittest.main()
