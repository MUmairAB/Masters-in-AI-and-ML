# Assignment 1: Intelligent Agent Architectures and Graph Search Algorithms

This assignment explores two fundamental AI concepts: 

1. **Intelligent Agent Architectures** (reflex vs. utility-based agents), and

2. **Graph Search Algorithms** (BFS vs. DFS) for maze solving.

## Part 1: Shopping Assistant Agent

### Problem 1.1: Reflex Agent

A simple reflex agent makes purchase decisions by comparing budget vs. price for each item individually, without planning or goal consideration.

**Starting State**: `budget = 20`, `basket = []`, `overall_satisfaction = 0`

**Condition-Action Rules**:
- If `price < budget`: Buy item, update budget and satisfaction
- If `price > budget`: Skip item

**Implementation Example**:
| Item | Price | Satisfaction | Action | Final State |
|------|-------|--------------|--------|-------------|
| Bread | 5 | 6 | Buy | budget=15, basket=['bread'], satisfaction=6 |
| Milk | 4 | 7 | Buy | budget=11, basket=['bread','milk'], satisfaction=13 |
| Eggs | 6 | 8 | Buy | budget=5, basket=['bread','milk','eggs'], satisfaction=21 |
| Chocolate | 8 | 9 | Skip | unchanged |

**Final State**: `budget = 5`, `basket = ['bread', 'milk', 'eggs']`, `overall_satisfaction = 21`

### Problem 1.2: Utility-Based Agent

A utility-based agent strategically maximizes satisfaction while staying within budget by evaluating all possible basket combinations.

**Utility Function**: Maximize `U(basket) = Σ satisfaction` subject to `Σ price ≤ 20`

**Satisfaction-Price Ratios**:
| Item | Price | Satisfaction | Ratio |
|------|-------|--------------|-------|
| Milk | 4 | 7 | 1.75 |
| Eggs | 6 | 8 | 1.333 |
| Bread | 5 | 6 | 1.2 |
| Chocolate | 8 | 9 | 1.125 |

**Optimal Basket**: Milk-Eggs-Chocolate (Total: $18, Satisfaction: **24**)

**Comparison**: The utility-based agent achieves higher satisfaction (24 vs. 21) by strategically evaluating all combinations rather than making greedy decisions.

## Part 2: Graph Search Algorithms - Maze Solving

This section is about graph-based search algorithms, and involves solving a maze using **Breadth First Search (BFS)** and **Depth First Search (DFS)** in **Python**.

### 2.1 Problem Statement

We need to solve the following maze using BFS and DFS:

<figure>
  <img src="./Original Maze.png" alt="Original Maze" />
  <figcaption><b>Figure 1:</b> Original maze to be solved using BFS and DFS algorithms.</figcaption>
</figure>

### 2.2 Implementation Details

#### 2.2.1 Graph Representation

The maze is represented as a graph where each cell is a node and connections between adjacent cells are edges. The graph is provided to the algorithms through an **adjacency list** representation, which maps each node to its list of neighboring nodes.

The adjacency list is created from the edge list stored in `maze.json` using the `create_adjacency_list_for_graph()` function. This function creates a bidirectional graph representation where each edge connects two nodes in both directions.

The maze's connections were manually mapped from the original maze and are visualized in the following figure:

<figure>
  <img src="./Maze Edge Mapping.jpeg" alt="Maze Edge Mapping" />
  <figcaption><b>Figure 2:</b> Visual representation of the maze's graph structure showing node connections (edges) mapped from the original maze.</figcaption>
</figure>


#### 2.2.2 Algorithm Overview

Both **DFS** and **BFS** algorithms follow a similar structure but differ in their node exploration strategy:

##### A) Key Components:

- **Visited Set**: Tracks which nodes have been explored to avoid revisiting them
- **Parent-Child Dictionary**: Maintains relationships between nodes to reconstruct the path once the goal is found
- **Data Structure**: 
  - **DFS** uses a **stack** (Last In First Out - LIFO) to explore deeply before backtracking
  - **BFS** uses a **queue** (First In First Out - FIFO) to explore level by level

##### B) Algorithm Flow:

1. Initialize with the start node in the data structure (stack/queue) and mark it as visited
2. While the data structure is not empty:
   - Pop/dequeue the next node
   - If it's the goal node, backtrack using parent relationships to reconstruct the path
   - Otherwise, add all unvisited neighbors to the data structure and mark them as visited
3. Return the path, execution time, and number of nodes visited

##### C) Key Difference:

- **DFS**: Explores one branch completely before moving to the next (depth-first), implemented using a stack
- **BFS**: Explores all nodes at the current level before moving to the next level (breadth-first), implemented using a queue. BFS guarantees finding the shortest path in an unweighted graph.

The main implementation functions are:
- `find_path_with_dfs()` - DFS algorithm implementation
- `find_path_with_bfs()` - BFS algorithm implementation
- `plot_maze_and_path()` - Visualization function for the maze and solution paths

### 2.3 Depth First Search Result

The code is available in the [code directory's main.py](./Code/main.py) file. DFS implementation is handled in the **find_path_with_dfs()** function.

The final path found by DFS is:

<figure>
  <img src="./DFS Solution.png" alt="DFS Solution" />
  <figcaption><b>Figure 3:</b> Solution path found by Depth First Search (DFS) algorithm. The path is highlighted in orange, with the start node in red and goal node in blue.</figcaption>
</figure>

### 2.4 Breadth First Search Result

The code is available in the [code directory's main.py](./Code/main.py) file. BFS implementation is handled in the **find_path_with_bfs()** function.

The final path found by BFS is:

<figure>
  <img src="./BFS Solution.png" alt="BFS Solution" />
  <figcaption><b>Figure 4:</b> Solution path found by Breadth First Search (BFS) algorithm. BFS guarantees the shortest path in an unweighted graph. The path is highlighted in orange, with the start node in red and goal node in blue.</figcaption>
</figure>

### 2.5 How to Run

1. Clone the repository, and Navigate to the `Code` directory
2. Ensure you have the required dependencies installed:
   - Python 3.x
   - matplotlib
   - json (built-in)
3. Run the code:
   ```bash
   python main.py
   ```

### 2.6 Output

The program outputs:
- The resultant path found by each algorithm
- Time taken by each algorithm to find the path (in microseconds)
- Number of nodes traversed by each algorithm
- Length of the path found by each algorithm
- Visual plots showing the original maze and the solutions found by DFS and BFS