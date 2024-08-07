import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    """
    Represents a 2D position in a grid.

    This immutable class defines a position with x and y coordinates. It provides
    methods for basic arithmetic operations between positions.

    Attributes:
        x (int): The x-coordinate of the position. Defaults to sys.maxsize.
        y (int): The y-coordinate of the position. Defaults to sys.maxsize.

    Methods:
        __add__(self, other): Adds two positions.
        __sub__(self, other): Subtracts one position from another.

    Note:
        This class is frozen (immutable) for thread-safety and to allow its use as
        a dictionary key or in sets.
    """

    x: int = sys.maxsize
    y: int = sys.maxsize

    def __add__(self, other: 'Position') -> 'Position':
        """
        Add this position to another position.

        Args:
            other (Position): The position to add to this one.

        Returns:
            Position: A new Position object with the sum of the x and y coordinates.

        Raises:
            NotImplementedError: If 'other' is not a Position object.

        Example:
            >>> p1 = Position(1, 2)
            >>> p2 = Position(3, 4)
            >>> p1 + p2
            Position(x=4, y=6)
        """
        if not isinstance(other, Position):
            raise NotImplementedError(f"Cannot add Position and {type(other)}")
        return Position(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other: 'Position') -> 'Position':
        """
        Subtract another position from this position.

        Args:
            other (Position): The position to subtract from this one.

        Returns:
            Position: A new Position object with the difference of the x and y coordinates.

        Raises:
            NotImplementedError: If 'other' is not a Position object.

        Example:
            >>> p1 = Position(5, 5)
            >>> p2 = Position(2, 1)
            >>> p1 - p2
            Position(x=3, y=4)
        """
        if not isinstance(other, Position):
            raise NotImplementedError(
                f"Cannot subtract Position and {type(other)}")
        return Position(x=self.x - other.x, y=self.y - other.y)
