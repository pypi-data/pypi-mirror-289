from dataclasses import dataclass
from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position


@dataclass(frozen=True)
class Valley(Node):
    """
    Represents a valley node in a pathfinding grid.

    This class implements the Node protocol and represents a type of terrain
    that has a standard difficulty to traverse, similar to a plateau.

    Attributes:
        weight (float): The cost of traversing this node. Defaults to 1.0, 
                        representing standard difficulty terrain.
        position (Position): The position of this node in the grid. Defaults to Position().

    Methods:
        __eq__(self, other): Defines equality comparison between nodes.
        __lt__(self, other): Defines less than comparison between nodes based on their weights.
        __hash__(self): Defines a hash value for the node based on its weight and position.

    Note:
        This class is frozen (immutable) for thread-safety and to allow its use as
        a dictionary key or in sets.
    """

    weight: float = 1.0
    position: Position = Position()

    def __eq__(self, other):
        """
        Check if this node is equal to another node.

        Equality is based on both position and weight.

        Args:
            other: Another object to compare with this node.

        Returns:
            bool: True if the nodes have the same position and weight, False otherwise.

        Raises:
            NotImplementedError: If the other object is not a Node or lacks required attributes.
        """
        if not isinstance(other, Node):
            raise NotImplementedError(
                "Missing `position` or `weight` attribute")
        return self.position == other.position and self.weight == other.weight

    def __lt__(self, other):
        """
        Check if this node's weight is less than another node's weight.

        This method is used for comparisons in priority queues or sorting.

        Args:
            other: Another node to compare with this node.

        Returns:
            bool: True if this node's weight is less than the other node's weight, False otherwise.

        Raises:
            NotImplementedError: If the other object is not a Node or lacks the weight attribute.
        """
        if not isinstance(other, Node):
            raise NotImplementedError("Missing `weight` attribute")
        return self.weight < other.weight

    def __hash__(self):
        """
        Compute a hash value for this node.

        The hash is based on both the weight and position of the node.
        This allows Valley objects to be used as dictionary keys or in sets.

        Returns:
            int: A hash value for the node.
        """
        return hash((self.weight, self.position))
