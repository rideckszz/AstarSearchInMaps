import heapq
from questionary import prompt, Choice

class Node:
    def __init__(self, name, g=0, h=0):
        self.name = name
        self.g = g  # cost of the path from the initial node to the current node
        self.h = h  # estimated cost from the current node to the goal node

    def __lt__(self, other):
        # Comparison for the priority queue
        return (self.g + self.h) < (other.g + other.h)

def astar(start, goal, graph):
    open_list = []
    closed_list = set()
    came_from = {}  # Dictionary to track where each node came from
    cost_so_far = {start: 0}  # Dictionary to track the accumulated cost of each node

    start_node = Node(start, 0, heuristic(start, goal, graph))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.name == goal:
            # Reconstructing the path traveled and calculating the total cost
            path = []
            total_cost = 0
            while current_node is not None:
                path.append(current_node.name)
                total_cost += current_node.g
                current_node = came_from.get(current_node.name)
            return path[::-1], total_cost  # Reversing the list to get the correct path

        closed_list.add(current_node.name)

        for neighbor, cost in graph[current_node.name].items():
            if neighbor not in closed_list:
                g = current_node.g + cost
                h = heuristic(neighbor, goal, graph)
                new_node = Node(neighbor, g, h)
                heapq.heappush(open_list, new_node)
                came_from[neighbor] = current_node
                cost_so_far[neighbor] = g

    return None, None  # Path not found

def heuristic(current, goal, graph):
    # Check if the distance between the locations is in the graph
    if (current, goal) in graph:
        return graph[(current, goal)]
    elif (goal, current) in graph:
        return graph[(goal, current)]
    else:
        # If there is no entry in the graph, we return a minimum estimate of 1
        return 1

def bfs(start, goal, graph):
    open_list = [start]
    closed_list = set()

    came_from = {}
    while open_list:
        current_node = open_list.pop(0)

        if current_node == goal:
            path = [current_node]
            while current_node != start:
                current_node = came_from[current_node]
                path.append(current_node)
            return path[::-1], len(path) - 1

        closed_list.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in closed_list and neighbor not in open_list:
                open_list.append(neighbor)
                came_from[neighbor] = current_node

    return None, None



def main():
    # Define the graph with locations, neighbors, and costs
    graph = {
        "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
        "Zerind": {"Arad": 75, "Oradea": 71},
        "Oradea": {"Zerind": 71, "Sibiu": 151},
        "Timisoara": {"Arad": 118, "Lugoj": 111},
        "Lugoj": {"Timisoara": 111, "Mehadia": 70},
        "Mehadia": {"Lugoj": 70, "Drobeta": 75},
        "Drobeta": {"Mehadia": 75, "Craiova": 120},
        "Craiova": {"Drobeta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
        "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
        "Rimnicu Vilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
        "Fagaras": {"Sibiu": 99, "Bucharest": 211},
        "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
        "Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85},
        "Giurgiu": {"Bucharest": 90},
        "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
        "Hirsova": {"Urziceni": 98, "Eforie": 86},
        "Eforie": {"Hirsova": 86},
        "Vaslui": {"Urziceni": 142, "Iasi": 92},
        "Iasi": {"Vaslui": 92, "Neamt": 87},
        "Neamt": {"Iasi": 87}
    }

    algorithm = prompt([
        {
            "type": "select",
            "name": "algorithm",
            "message": "Select an algorithm:",
            "choices": [
                Choice("A*", "astar"),
                Choice("Breadth-First Search (BFS)", "bfs")
            ]
        }
    ])["algorithm"]

    start = input("Enter the starting location: ") # Initial location
    goal = input("Enter the destination: ")   # Final destination

    if algorithm == "astar":
        path, total_cost = astar(start, goal, graph)
    else:
        path, total_cost = bfs(start, goal, graph)

    if path is not None:
        print("Shortest path from", start, "to", goal, ":")
        print(" -> ".join(path))
        print("Total cost of the path:", total_cost)
    else:
        print("Path not found")

if __name__ == "__main__":
    main()