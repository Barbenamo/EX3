# **Object Oriented Programming 3rd assignment.**
## this assignment was coded, developed and edited by:
### 1.Bar Ben Amo.
### 2.Chaya Blank.
### 3.Dror Tapiro.
#### the assignment has 3 main parts: implementing and creating a directed weighted graph, creating various algorithms to it and comparing this assignment to  our previous assignment (EX2).

Data-Structure:
=======
the data structure that the assignment is built on is an directional weighted graph.
for info about this type of graph you can visit: [https://en.wikipedia.org/wiki/Directed_graph].
the process of building this data structrue was to implement and program the interfaces sent by Boaz-Ben-Moshe.
here are the classes of this data structure:
| class | description |
| ------|:-----------:|
| GraphElements| contains two classes, NodeData, which represents the vertex on the graph, and EdgeData, which represents the edge connecting two vertices. |
| DiGraph | this class contains various methods that can be used on the graph, such as adding/deleting a node, connects/disconnect vertices via edges etc. |
| GraphAlgo|this class contains more complex method that can be apllied on the graph, such as shortest-path algorithm and Tarjan SCC algorithm.|

Part1: the basis of the data structer:
----------------
The 1st part of the assignment is all about defining the components of the graph, which are the NodeData-the vertex and EdgeData-the edge.
The NodeData class contains various variables such as key, location, tag and info (for meta-data) and dictionaries for edges that point into the node
and out of the node.
The EdgeData class contains variables such as weight, source and destination, info and tag.
special algoroithms in these classese are **equals** which cheks whether two vertices or edges are the same.
A to-String mehtod was also apllied in order to keep track, mainly for self uses.

Part2: advanced algorithms:
----------------
The 2nd part of the assignment contains various complex algorithms.
here are some of the special methods:
----------------
1. Shortest-path: a method that calculates the shortest path between two given vertices, and retrievs a list of all the keys between them.
in order to calculate the shortest path between two given vertices on the graph, we used dijkstra's algorithm (DFS).
for info about this specific algorithm please visit: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm.
2. Connected componnent and Connected componnents: a method that divides the graph to seperate groups, each group is a strongly connected sub group.
 this method uses the Tarjan's algorithms, for more information visit: [https://en.wikipedia.org/wiki/Tarjan%27s_algorithm]
3. Load and Save: methods that serialize and deserializes the graph to a json-formated file.
4. Plot-Graph: a method that uses the **matlibplot** library to plot and visualize the graph, showing it components-the vertices and the edges.




