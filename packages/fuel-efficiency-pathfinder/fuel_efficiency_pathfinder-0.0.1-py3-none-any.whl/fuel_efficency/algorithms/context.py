from dataclasses import dataclass, field
from typing import List
from fuel_efficency.algorithms.dijkstra import DijkstraStrategy
from fuel_efficency.algorithms.path_finding import PathfindingStrategy
from fuel_efficency.entities.node import Node
from fuel_efficency.entities.valley import Valley


@dataclass
class Context:
    """
    A class representing the context for pathfinding operations.

    This class encapsulates the grid, start and end nodes, and the pathfinding strategy.
    It provides properties and methods to manage and execute pathfinding operations.
    """

    _strategy: PathfindingStrategy = field(default_factory=DijkstraStrategy)
    _grid: List[List[Node]] = field(default_factory=lambda: [
                                    [Valley() for _ in range(3)] for _ in range(3)])
    _start: Node = field(default_factory=Valley)
    _end: Node = field(default_factory=Valley)

    @property
    def grid(self):
        """
        Get the current grid.

        Returns:
            List[List[Node]]: The current grid of nodes.
        """
        return self._grid

    @grid.setter
    def grid(self, new_grid: List[List[Node]]):
        """
        Set a new grid, with type checking.

        Args:
            new_grid (List[List[Node]]): The new grid to set.

        Raises:
            TypeError: If the new_grid is not a list of lists.
        """
        if not isinstance(new_grid, list):
            raise TypeError("Grid must be a list")
        if not all(isinstance(row, list) for row in new_grid):
            raise TypeError("Grid must be a list of lists")
        self._grid = new_grid

    @property
    def start(self):
        """
        Get the start node.

        Returns:
            Node: The current start node.
        """
        return self._start

    @start.setter
    def start(self, new_start: Node):
        """
        Set a new start node.

        Args:
            new_start (Node): The new start node to set.
        """
        self._start = new_start

    @property
    def end(self):
        """
        Get the end node.

        Returns:
            Node: The current end node.
        """
        return self._end

    @end.setter
    def end(self, new_end: Node):
        """
        Set a new end node.

        Args:
            new_end (Node): The new end node to set.
        """
        self._end = new_end

    @property
    def strategy(self):
        """
        Get the current pathfinding strategy.

        Returns:
            PathfindingStrategy: The current pathfinding strategy.
        """
        return self._strategy

    @strategy.setter
    def strategy(self, new_strategy: PathfindingStrategy):
        """
        Set a new pathfinding strategy, with type checking.

        Args:
            new_strategy (PathfindingStrategy): The new pathfinding strategy to set.

        Raises:
            TypeError: If the new_strategy is not an instance of PathfindingStrategy.
        """
        if not isinstance(new_strategy, PathfindingStrategy):
            raise TypeError(
                "Strategy must be an instance of PathfindingStrategy")
        self._strategy = new_strategy

    def run(self):
        """
        Execute the pathfinding strategy.

        Returns:
            The result of the pathfinding strategy's find_path method.

        Raises:
            NotImplementedError: If the strategy does not implement the find_path method.
        """
        if not hasattr(self._strategy, 'find_path'):
            raise NotImplementedError(
                "Strategy must implement the find_path method")
        return self._strategy.find_path(self.grid, self.start, self.end)
