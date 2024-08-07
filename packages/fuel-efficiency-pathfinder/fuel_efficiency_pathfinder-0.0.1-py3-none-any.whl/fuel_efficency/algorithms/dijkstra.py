import heapq
import math
from typing import List
from fuel_efficency.algorithms.path_finding import PathfindingStrategy
from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position


class DijkstraStrategy(PathfindingStrategy):
    """
    A class implementing the Dijkstra pathfinding algorithm.

    This strategy finds the shortest path between two nodes in a grid,
    considering movement in eight directions (including diagonals).
    """

    cardinal_directions = [Position(-1, -1), Position(-1, 0), Position(-1, 1),
                           Position(0, -1), Position(0, 1),
                           Position(1, -1), Position(1, 0), Position(1, 1)]

    @staticmethod
    def find_path(grid: List[List[Node]], start: Node, end: Node) -> List[Node]:
        """
        Find the shortest path from start to end using Dijkstra's algorithm.

        Args:
            grid (List[List[Node]]): The 2D grid of nodes.
            start (Node): The starting node.
            end (Node): The target node.

        Returns:
            List[Node]: The shortest path from start to end, or an empty list if no path is found.
        """
        heap = [(0, start)]
        came_from = {}
        cost_so_far = {start: 0}

        while heap:
            current_cost, current_node = heapq.heappop(heap)

            if current_node == end:
                path = []
                while current_node != start:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.reverse()
                return path

            for neighbor in DijkstraStrategy.get_neighbors(grid, current_node):
                new_cost = cost_so_far[current_node] + \
                    DijkstraStrategy.calculate_distance(current_node, neighbor)
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost
                    heapq.heappush(heap, (priority, neighbor))
                    came_from[neighbor] = current_node

        return []  # No path found

    @staticmethod
    def get_neighbors(grid: List[List[Node]], node: Node) -> List[Node]:
        """
        Get all valid neighboring nodes for a given node.

        Args:
            grid (List[List[Node]]): The 2D grid of nodes.
            node (Node): The node to find neighbors for.

        Returns:
            List[Node]: A list of valid neighboring nodes.
        """
        neighbors = []
        for direction in DijkstraStrategy.cardinal_directions:
            new_pos = Position(node.position.x + direction.x,
                               node.position.y + direction.y)
            if 0 <= new_pos.x < len(grid) and 0 <= new_pos.y < len(grid[0]):
                neighbors.append(grid[new_pos.x][new_pos.y])
        return neighbors

    @staticmethod
    def calculate_distance(node1: Node, node2: Node) -> float:
        """
        Calculate the Euclidean distance between two nodes.

        Args:
            node1 (Node): The first node.
            node2 (Node): The second node.

        Returns:
            float: The Euclidean distance between the two nodes.
        """
        return math.sqrt((node1.position.x - node2.position.x)**2 +
                         (node1.position.y - node2.position.y)**2)
