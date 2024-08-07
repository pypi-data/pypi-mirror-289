from typing import Protocol, runtime_checkable
from fuel_efficency.entities.position import Position


@runtime_checkable
class Node(Protocol):
    """
    A protocol defining the interface for a Node in a pathfinding grid.

    This protocol specifies the attributes and methods that any concrete Node implementation
    must have to be compatible with the pathfinding algorithms.

    Attributes:
        weight (float): The cost or difficulty of traversing this node.
        position (Position): The position of this node in the grid.

    Methods:
        __eq__(self, other): Defines equality comparison between nodes.
        __lt__(self, other): Defines less than comparison between nodes.
        __hash__(self): Defines a hash value for the node.

    Note:
        This is a runtime-checkable protocol, which means it can be used with isinstance()
        and issubclass() at runtime to check if an object implements this interface.
    """

    weight: float
    position: Position

    def __eq__(self, other):
        """
        Define equality comparison between nodes.

        Args:
            other: Another object to compare with this node.

        Returns:
            bool: True if the nodes are equal, False otherwise.
        """
        ...

    def __lt__(self, other):
        """
        Define less than comparison between nodes.

        This is typically used for sorting nodes or in priority queues.

        Args:
            other: Another node to compare with this node.

        Returns:
            bool: True if this node is less than the other node, False otherwise.
        """
        ...

    def __hash__(self):
        """
        Define a hash value for the node.

        This allows nodes to be used as dictionary keys or in sets.

        Returns:
            int: A hash value for the node.
        """
        ...
