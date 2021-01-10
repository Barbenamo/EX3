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

Part 1: the basis of the data-structure.
========
The 1st part of the assignment is all about defining the components of the graph, which are the NodeData-the vertex and EdgeData-the edge.<br />
The NodeData class contains various variables such as key, location, tag and info (for meta-data) and dictionaries for edges that point into the node
and out of the node. <br />
The EdgeData class contains variables such as weight, source and destination, info and tag.
special algoroithms in these classese are **equals** which cheks whether two vertices or edges are the same.
A to-String mehtod was also apllied in order to keep track, mainly for self uses. 

GraphElements Class methods:
------------------
**The NodeData offers these methods:**
* ```__init__```: A constructor to initiate a NodeData object.
* ```add_nei```: A method that recievs an integer key and a float weight that belnogs to an edge that comes out from the node.<br />
the method also updates the dictionary 
of the specific node.<br />
* ```add_guest``` : A method that recieves an integer key and a float weight that belongs to an edge that comes into the node.<br />
* ```remove_nei```: A method to remove a certain edge that comes from the specific node.
* ```remove_guest```: A method to remove a certain edge that come into the specific node.
* ```has_nei```: A method to check if a certain edge that comes into the node exists on the node's dictionary.
* ```has_guest```: A method to check if a certain edge that comes out of the node exists on the node's dictionary.<br />

Class DiGraph:
--------------
After defining its components, the class DiGraph implements the GraphInterface interface.<br />
the class contains 3 variables: a dictionary, to represent the graph.<br />
An mc integer, to count the number of changes made on the graph.<br />
The number of edges exists on the graph.<br />
**The DiGraph class offers these methods:**
* ```__init__```: A method to initiate a the class object-directed graph.
* ```v_size```: A method to get the number of vertices on the graph.
* ```get_all_v```: A method to get a dictionary that contains the node itself and it's key.
* ```all_in_edges_of_node```: A method to get a dictionary that contains all of the edges that comes into a specific node.
* ```all_out_edges_of_node```: A method to get a dictionary that contains all of the edges that comes out from a specific node.
* ```add_edge```: A method to add an edge between two vertices, considers both the source and the destination's neighbors.
* ```add_node```: A method to add a node to the graph, checks first if the node already exists to avoid collisons.
* ```remove_node```: A method to remove a node from the graph, the method considers each neighbor or guest that are attached to the node.
* ```remove_edge```: A method to disconnect two vertices by removing the edge between them, checks first wheter they were connectet before trying to remove.
* ```has_edge```: A method to check whether are two vertices are connected via an edge.
* ```get_node```: A method to get a specific node from the graph, using it key as identifier.
* ```as_dict```: A metheod to transfer the graph objcet to a dictionary that customized especially for the json format.

Part 2: advanced algorithms.
==========================
The 2nd part of the assignment contains various complex algorithms.
here are some of the special methods:
----------------
* ```shortest_path```: A method that calculates the shortest path between two given vertices, and retrievs a list of all the keys between them.
in order to calculate the shortest path between two given vertices on the graph, we used dijkstra's algorithm (DFS).<br />
for info about this specific algorithm please visit: [https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm].
* ```connected_component```: a method that divides the graph to seperate groups, each group is a strongly connected sub group.
 this method uses the Tarjan's algorithms to retrieve a single connected componnent, for more information visit: [https://en.wikipedia.org/wiki/Tarjan%27s_algorithm]<br />
* ```connected_components```: a method that gathers all of the SCC's in the graph to a list
* ```reset```: a method to reset every node meta-data (tag, info), after performing algorithms on the graph.
* ```load_from_json```: a method to deserialize the graph from a given json-formated file.
* ```save_to_json```: a method to serialize the graph to a json-formated file.
* ```plot_graph```: a method that uses the **matlibplot** library to plot and visualize the graph, showing it components-the vertices and the edges.
* ```dfs```: depth-first-search, an algorithm that runs from a given source or a random one, and go through every node, iteretivly.
* ```reverse_dfs```: a method to run dfs on the reverse graph-mainly used for SCC algorithms.
* ```fill_stack```: a recursive method to recure on a given node and change the node's info and add it to a stack. (used in SCC).




