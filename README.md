# Graph Search Algorithms

This Python script provides implementations of two graph search algorithms - A* (A-star) and Breadth-First Search (BFS) - to find the shortest path between nodes in a graph.

## Prerequisites

- Python 3.x
- `questionary` library for interactive input

Install `questionary` using pip:

```pip install questionary```


## Usage

Run the script `graph_search.py` with Python.

``` python astar.py```


Follow the prompts to select an algorithm and provide the starting location and destination. The script will then find the shortest path using the chosen algorithm and display the result.

## Supported Algorithms

1. **A* (A-star)**:
   - A heuristic search algorithm that finds the shortest path between nodes in a graph. It uses both the actual cost of the path from the start node (g) and an estimated cost to the goal node (h).
   
2. **Breadth-First Search (BFS)**:
   - A simple graph search algorithm that explores all neighbor nodes at the present depth before moving on to nodes at the next depth level.

## Graph Representation

The graph used in this script is a simplified representation of the map of Romania, as described in the book "Artificial Intelligence: A Modern Approach" by Stuart Russell and Peter Norvig. It contains cities as nodes and the distances between them as edges.

Graph:

<div id="header" align="center">
  <img src="https://files.passeidireto.com/11663385-7d41-4b2d-b6e4-3c1cd985cc41/bg5.png" width="500"/>
</div>


If you want to change the graph in use just add the coordinates of your map to the graph function in main in the following format:

```{"Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},```

! The option to input those informations is a work in progress.

## Example

``` python astar.py```
This command will prompt you to select an algorithm and provide the starting location and destination. After inputting the required information, the script will find and display the shortest path between the specified nodes.

## Graph Representation

The graph is represented as a dictionary where each node is a key and its neighbors are the corresponding values. The edge costs between nodes are also specified in the graph.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Derick G. Andrighetti**
- GitHub: [@Rideckszz](https://github.com/Rideckszz)
- Date: 14/03/2024


