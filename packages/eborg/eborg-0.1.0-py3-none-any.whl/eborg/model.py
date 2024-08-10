"""Define the data models of the program."""

import logging
from typing import List, Optional, Tuple

from pydantic import BaseModel

log = logging.getLogger(__name__)


class Highlight(BaseModel):
    section_id: str
    position: str
    text: str

    def parse_position(self) -> Tuple[int, ...]:
        """
        Parse the position string into a tuple of integers for comparison.

        Returns:
            Tuple[int, ...]: A tuple of integers representing the position.
        """
        # Remove any leading slashes and split by '/'
        parts = self.position.replace(":", "/").strip("/").split("/")
        return tuple(int(part) for part in parts)

    def __lt__(self, other: "Highlight") -> bool:
        """
        Less-than comparison based on the position.

        Args:
            other (Highlight): The other Highlight object to compare against.

        Returns:
            bool: True if this Highlight's position is less than the other's position.
        """
        return self.parse_position() < other.parse_position()

    def __repr__(self) -> str:
        """
        Representation of the Highlight object.

        Returns:
            str: A string representation of the Highlight object.
        """
        return f"Highlight(section_id='{self.section_id}', position='{self.position}', text='{self.text}')"


class Section(BaseModel):
    id: str
    title: str
    content: Optional[str] = None
    sections: List["Section"] = []
    highlights: List[Highlight] = []

    def __repr__(self) -> str:
        return self.title


class Book(BaseModel):
    title: str
    author: str
    toc: List[Section]
