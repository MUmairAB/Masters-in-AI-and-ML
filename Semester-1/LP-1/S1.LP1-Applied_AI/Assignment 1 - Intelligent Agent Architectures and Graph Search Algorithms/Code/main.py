"""
This code implements the DFS and BFS algorithms to find a path in a maze.
Maze is stored in a JSON file. It applies the algorithms to the maze, and prints:
    - Resultant path
    - Time taken by the algorithms to find the path
    - Number of nodes traversed by the algorithms
    - Length of the path found by the algorithms

"""

import json
import matplotlib.pyplot as plt
import time
import random


def create_adjacency_list_for_graph(edges_LIST: list) -> dict:
    """
    This function creates an adjacency list representation of the graph, where each node is mapped to its neighbors.
    Adjacecny list is technical name for graph representation.
    Actually, it returns a dictionary where the keys are the nodes and the values are the lists of neighboring nodes.
    e.g. if the edges are:
    [
        ["node1", "node2"],
        ["node1", "node3"],
        ["node2", "node3"]
    ]
    then the adjacency list will be:
    {
        "node1": ["node2", "node3"],
        "node2": ["node1", "node3"],
        "node3": ["node1", "node2"]
    }

    Args:
        edges_LIST (list): A list of pairs representing the edges.

    Returns:
        adjacency_list_DICT (dict): The adjacency list.
    """
    try:
        adjacency_list_DICT = {}
        for node_a, node_b in edges_LIST:
            # If node_a is not already present in the adjacency list, add it
            if node_a not in adjacency_list_DICT:
                adjacency_list_DICT[node_a] = []
            # Add the neighbor to the adjacency list
            adjacency_list_DICT[node_a].append(node_b)

            # If node_b is not already present in the adjacency list, add it
            if node_b not in adjacency_list_DICT:
                adjacency_list_DICT[node_b] = []
            # Add the neighbor to the adjacency list
            adjacency_list_DICT[node_b].append(node_a)
        return adjacency_list_DICT
    except Exception as e:
        print(f"The following error occurred in the create_adjacency_list_for_graph function: {e}")
        return {}


def find_path_with_dfs(adjacency_list_DICT: dict, start_node: str, goal_node: str) -> tuple:
    """
    This function applies Depth-First Search (DFS) algorithm to find a path from start_node to goal_node.
    
    "Key Difference from BFS": We need to store the nodes in the stack (Last In First Out) because we need to traverse each branch completely before moving to the next branch.
    
    Args:
        - adjacency_list_DICT (dict): An adjacency list representation of the graph.
        - start_node (str): The key of the starting node.
        - goal_node (str): The key of the goal node.

    Returns:
        - path_LIST (list): A list of node keys representing the path.
    """
    try:
        start_time_for_dfs = time.perf_counter()
        # Push the start node to the stack
        nodes_stack = [start_node]
        # Create a set for keeping track of visited nodes; initialize with the start node
        visited_nodes = {start_node}
        # Create a dictionary for keeping track of parent-child relationships; initialize with the start node
        parent_children_relationships_DICT = {start_node: None}

        while nodes_stack:
            current_node = nodes_stack.pop()
            # If the current node is the goal node, we have found the path
            if current_node == goal_node:
                # Backtrack to the start node to get the full path
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = parent_children_relationships_DICT[current_node]
                end_time_for_dfs = time.perf_counter()
                time_taken_for_dfs = str(round((end_time_for_dfs - start_time_for_dfs) * 1_000_000, 3)) + " micro seconds"
                return path[::-1], time_taken_for_dfs, len(visited_nodes) # return the path in reverse order

            # Check if the node is in the graph before accessing its neighbors
            if current_node in adjacency_list_DICT:
                # For each neighbor, if it has not been visited, add it to the visited set, update the parent-child relationship, and push it to the stack
                for neighbor in adjacency_list_DICT[current_node]:
                    if neighbor not in visited_nodes:
                        # Add the neighbor to the visited set
                        visited_nodes.add(neighbor)
                        # Update the parent-child relationship
                        parent_children_relationships_DICT[neighbor] = current_node
                        # Push the neighbor to the stack
                        nodes_stack.append(neighbor)
        
        return [], "0 micro seconds", 0 # No path found
    
    except Exception as e:
        print(f"The following error occurred in the find_path_with_dfs function: {e}")
        return [], "0 micro seconds", 0 # No path found

def find_path_with_bfs(adjacency_list_DICT: dict, start_node: str, goal_node: str) -> tuple:
    """
    This function applies Breadth-First Search (BFS) algorithm to find a path from start_node to goal_node.
    
    "Key Difference from DFS": We need to store the nodes in the queue (First In First Out) because we need to visit all the nodes at the same level before moving to the next level.
    
    Args:
        - adjacency_list_DICT (dict): An adjacency list representation of the graph.
        - start_node (str): The key of the starting node.
        - goal_node (str): The key of the goal node.

    Returns:
        - path_LIST (list): A list of node keys representing the path.
    """
    try:
        start_time_for_bfs = time.perf_counter()
        # Push the start node to the queue
        nodes_queue = [start_node]
        # Create a set for keeping track of visited nodes; initialize with the start node
        visited_nodes = {start_node}
        # Create a dictionary for keeping track of parent-child relationships; initialize with the start node
        parent_children_relationships_DICT = {start_node: None}

        while nodes_queue:
            current_node = nodes_queue.pop(0) # Pop the first node from the queue
            # If the current node is the goal node, we have found the path
            if current_node == goal_node:
                # Backtrack to the start node to get the full path
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = parent_children_relationships_DICT[current_node]
                end_time_for_bfs = time.perf_counter()
                time_taken_for_bfs = str(round((end_time_for_bfs - start_time_for_bfs) * 1_000_000, 3)) + " micro seconds"
                return path[::-1], time_taken_for_bfs, len(visited_nodes) # return the path in reverse order

            # Check if the node is in the graph before accessing its neighbors
            if current_node in adjacency_list_DICT:
                # For each neighbor, if it has not been visited, add it to the visited set, update the parent-child relationship, and push it to the queue
                for neighbor in adjacency_list_DICT[current_node]:
                    if neighbor not in visited_nodes:
                        # Add the neighbor to the visited set
                        visited_nodes.add(neighbor)
                        # Update the parent-child relationship
                        parent_children_relationships_DICT[neighbor] = current_node
                        # Push the neighbor to the queue
                        nodes_queue.append(neighbor)
        
        return [], "0 micro seconds", 0 # No path found
    
    except Exception as e:
        print(f"The following error occurred in the find_path_with_bfs function: {e}")
        return [], "0 micro seconds", 0 # No path found


def plot_maze_and_path(nodes_DICT: dict, edges_LIST: list, solution_path: list, start_node_key: str, goal_node_key: str, plot_title: str) -> None:
    """
    This function plots the maze and the path, if provided.
    """
    try:
        zorder = 0 # We need to plot the maze, and solition on the same plot, so we need to keep track of the order
        
        # Create a new plot
        fig, ax = plt.subplots(figsize=(10, 5))

        # Plot the edges as gray lines
        for edge in edges_LIST:
            # Segregate the edges into two nodes
            node_a = edge[0]
            node_b = edge[1]
            
            # Get the coordinates of the nodes
            ca, ra = nodes_DICT[node_a]['c'], nodes_DICT[node_a]['r']
            cb, rb = nodes_DICT[node_b]['c'], nodes_DICT[node_b]['r']
            zorder += 1
            ax.plot([ca, cb], [ra, rb], color='gray', zorder=zorder)

        # Plot all the nodes as black dots
        for node_key in nodes_DICT:
            c, r = nodes_DICT[node_key]['c'], nodes_DICT[node_key]['r']
            zorder += 1
            ax.plot(c, r, 'o', color='black', markersize=6, zorder=zorder)

        # If a path is provided, plot it
        if solution_path:
            # Plot the path edges in orange
            for i in range(len(solution_path) - 1):
                node_a = solution_path[i]
                node_b = solution_path[i+1]
                c1, r1 = nodes_DICT[node_a]['c'], nodes_DICT[node_a]['r']
                c2, r2 = nodes_DICT[node_b]['c'], nodes_DICT[node_b]['r']
                zorder+=1
                ax.plot([c1, c2], [r1, r2], '*', color='orange', markersize=10, zorder=zorder)
        zorder += 1
        # Highlight the start node in red
        start_c, start_r = nodes_DICT[start_node_key]['c'], nodes_DICT[start_node_key]['r']
        ax.plot(start_c, start_r, 'o', color='red', markersize=8, zorder=zorder)

        # Highlight the goal node in blue
        goal_c, goal_r = nodes_DICT[goal_node_key]['c'], nodes_DICT[goal_node_key]['r']
        ax.plot(goal_c, goal_r, 'o', color='blue', markersize=8, zorder=zorder)

        # Configure and display the plot
        ax.invert_yaxis()
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(plot_title)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"The following error occurred in the plot_maze_and_path function: {e}")
        pass


if __name__ == "__main__":
    try:
        # Load the maze data from the JSON file
        with open('maze.json', 'r') as f:
            maze_data = json.load(f)
        
        # Extract nodes, edges, start, and goal information from the loaded maze data
        nodes = maze_data['nodes']
        edges = maze_data['edges']
        
        """
        What path DFS generates depends upon the order of the edges.
        If the edges are shuffled, the resulting path will be different.
        If the edges are not shuffled, the resulting path will be the same everytime the code is run.
        """
        #random.shuffle(edges) 
        
        start_node_key = maze_data['start']
        goal_node_key = maze_data['goal']

        # Plot the maze
        plot_maze_and_path(nodes, edges, None, start_node_key, goal_node_key, "Original Maze")

        # Create the adjacency list for the given maze
        adjacency_list_DICT = create_adjacency_list_for_graph(edges)
        
        # Find the path using DFS
        dfs_path_for_maze, time_taken_for_dfs, num_visited_nodes_for_dfs = find_path_with_dfs(adjacency_list_DICT, start_node_key, goal_node_key)
        if dfs_path_for_maze:
            print("Resultant path found by DFS:", dfs_path_for_maze)
            print(f"DFS found the path for Maze in {time_taken_for_dfs}, and visited {num_visited_nodes_for_dfs} nodes. The final path is {len(dfs_path_for_maze)} nodes long.")
            # Plot the maze and the path
            plot_maze_and_path(nodes, edges, dfs_path_for_maze, start_node_key, goal_node_key, f"DFS Path for Maze \n(Length of path: {len(dfs_path_for_maze)}, Time taken: {time_taken_for_dfs}, Number of nodes traversed: {num_visited_nodes_for_dfs})")
        else:
            print("DFS did not find the path for Maze.")

        # Find the path using BFS
        bfs_path_for_maze, time_taken_for_bfs, num_visited_nodes_for_bfs = find_path_with_bfs(adjacency_list_DICT, start_node_key, goal_node_key)
        if bfs_path_for_maze:
            print("Resultant path found by BFS:", bfs_path_for_maze)
            print(f"BFS found the path for Maze in {time_taken_for_bfs}, and visited {num_visited_nodes_for_bfs} nodes. The final path is {len(bfs_path_for_maze)} nodes long.")
            # Plot the maze and the path
            plot_maze_and_path(nodes, edges, bfs_path_for_maze, start_node_key, goal_node_key, f"BFS Path for Maze \n(Length of path: {len(bfs_path_for_maze)}, Time taken: {time_taken_for_bfs}, Number of nodes traversed: {num_visited_nodes_for_bfs})")
        else:
            print("BFS did not find the path for Maze.")

    except Exception as e:
        print(f"The following error occurred in the main function: {e}")
        pass
