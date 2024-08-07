import heapq
from typing import List
from fuel_efficency.algorithms.path_finding import PathfindingStrategy
from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position


class AStarStrategy(PathfindingStrategy):
    """
    A* pathfinding strategy implementation.
    """

    allowed_directions = [
        Position(-1, 0), Position(0, -1), Position(0, 1), Position(1, 0)]

    @staticmethod
    def find_path(grid: List[List[Node]], start: Node, end: Node) -> List[Node]:
        """
        Find the optimal path from start to end using A* algorithm.

        Args:
            grid (List[List[Node]]): The 2D grid of nodes.
            start (Node): The starting node.
            end (Node): The target node.

        Returns:
            List[Node]: The optimal path from start to end, or an empty list if no path is found.
        """
        def heuristic(node: Node) -> float:
            """
            Calculate the heuristic value (Manhattan distance) for a given node.

            Args:
                node (Node): The node to calculate the heuristic for.

            Returns:
                float: The Manhattan distance between the node and the end node.
            """
            return abs(node.position.x - end.position.x) + abs(node.position.y - end.position.y)

        def get_key(node: Node) -> tuple:
            """
            Get a tuple key for a node, prioritizing right and down movements.

            Args:
                node (Node): The node to get the key for.

            Returns:
                tuple: A tuple containing the node's x and y coordinates.
            """
            return (node.position.x, node.position.y)

        open_set = []
        heapq.heappush(open_set, (0, get_key(start), start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: heuristic(start)}

        while open_set:
            current = heapq.heappop(open_set)[2]

            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]

            for neighbor in AStarStrategy.get_neighbors(grid, current):
                tentative_g_score = g_score[current] + \
                    AStarStrategy.calculate_distance(current, neighbor)

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor)
                    heapq.heappush(
                        open_set, (f_score[neighbor], get_key(neighbor), neighbor))

        return []  # No path found

    @staticmethod
    def get_neighbors(grid: List[List[Node]], node: Node) -> List[Node]:
        """
        Get the valid neighboring nodes for a given node.

        Args:
            grid (List[List[Node]]): The 2D grid of nodes.
            node (Node): The node to find neighbors for.

        Returns:
            List[Node]: A list of valid neighboring nodes, sorted to prefer right and down movements.
        """
        neighbors = []
        for direction in AStarStrategy.allowed_directions:
            new_pos = Position(node.position.x + direction.x,
                               node.position.y + direction.y)
            if 0 <= new_pos.x < len(grid) and 0 <= new_pos.y < len(grid[0]):
                neighbors.append(grid[new_pos.x][new_pos.y])

        # Sort neighbors to prefer right and down movements
        neighbors.sort(key=lambda n: (-n.position.x, -n.position.y))
        return neighbors

    @staticmethod
    def calculate_distance(node1: Node, node2: Node) -> float:
        """
        Calculate the Manhattan distance between two nodes.

        Args:
            node1 (Node): The first node.
            node2 (Node): The second node.

        Returns:
            float: The Manhattan distance between the two nodes.
        """
        return abs(node1.position.x - node2.position.x) + abs(node1.position.y - node2.position.y)
