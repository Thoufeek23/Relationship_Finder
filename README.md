# Relationship Finder 👨‍👩‍👧‍👦

## What it is
Relationship Finder is a Python-based console application that calculates and identifies the exact familial relationship between two individuals within a predefined family tree. By inputting two names, the system computes their connection and outputs their specific relationship status (e.g., "Person A is the uncle of Person B" or "Person A is the granddaughter of Person B").

## Tech Stack
* **Language:** Python 3
* **Libraries:** `heapq` (Python Standard Library)
* **Concepts:** Graph Theory, Data Structures, Pathfinding Algorithms

## How it is Built
The core of the application relies on representing the family tree as a **Weighted Undirected Graph**. 

1. **Graph Construction:** Every person is added as a "node" in the graph, and their immediate relationships are added as "edges" with specific numerical weights (e.g., a weight of `1` indicates a spousal link, while a weight of `2` typically indicates a parent-child link).
2. **Pathfinding Algorithm:** The system utilizes **Dijkstra's Algorithm** (implemented via a priority queue using Python's `heapq` module) to calculate the shortest path—or minimum distance—between the starting person and the target person.
3. **Relationship Inference:** To accurately translate a numerical distance into a human-readable relationship, the script categorizes all nodes into predefined lists:
   * **Gender classifications:** Males (`m`) and Females (`f`).
   * **Generational tiers:** Grandparents (`a`), Parents (`b`), and Children (`c`).
4. **Resolution:** By combining the minimum distance calculated by the algorithm with the gender and generational data of the two nodes, the program navigates a detailed decision tree to output the exact relationship (ranging from immediate family like Mother/Son to extended family like Cousin, Uncle, or In-laws).
