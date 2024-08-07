from dataclasses import dataclass

from fuel_efficency.entities.node import Node
from fuel_efficency.entities.position import Position


@dataclass(slots=True)
class UpHill(Node):
    """
    Represents an uphill node in a fuel efficiency scenario.

    Attributes:
        weight (float): The weight of the uphill, affecting fuel efficiency. Defaults to 2.
        position (Position): The position of the uphill node. Defaults to an instance of Position.

    Methods:
        __eq__(self, other): Checks equality with another node based on position and weight.
            Raises NotImplementedError if the other object is not an instance of Node and lacks `position` or `weight`.

        __lt__(self, other): Compares this node with another based on weight for sorting.
            Raises NotImplementedError if the other object is not an instance of Node and lacks `weight`.

        __hash__(self): Provides a hash based on the node's weight and position for use in collections.
    """
    weight: float = float(2)
    position: 'Position' = Position()

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
        This allows Plateau objects to be used as dictionary keys or in sets.

        Returns:
            int: A hash value for the node.
        """
        return hash((self.weight, self.position))
