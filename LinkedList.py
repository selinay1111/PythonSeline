from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class _Node:
    """A node in a linked list.

    Instance Attributes:
      - item: The data stored in this node.
      - next: The next node in the list, if any.
    """
    item: Any
    next: Optional[_Node] = None  # By default, this node does not link to any other node

class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # Private Instance Attributes:
    #   - _first: The first node in this linked list, or None if this list is empty.
    _first: Optional[_Node]

    def __init__(self) -> None:
        """Initialize an empty linked list.
        """
        self._first = None

    def to_list(self) -> list:
        """Return a built-in Python list containing the items of this linked list.

        The items in this linked list appear in the same order in the returned list.
        """
        items_so_far = []

        curr = self._first
        while curr is not None:
            items_so_far.append(curr.item)
            curr = curr.next

        return items_so_far

    def __getitem__(self, i: int) -> Any:
        """... """
        # Version 2
        curr = self._first
        curr_index = 0

        while not (curr is None or curr_index == i):
            curr = curr.next
            curr_index = curr_index + 1

        assert curr is None or curr_index == i
        if curr is None:
            # index is out of bounds
            raise IndexError
        else:
            # curr_index == i, so curr is the node at index i
            return curr.item

    def append(self, item: Any) -> None:
        """..."""
        new_node = _Node(item)

        if self._first is None:
            self._first = new_node
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next

            # After the loop, curr is the last node in the LinkedList.
            assert curr is not None and curr.next is None
            curr.next = new_node

    def insert(self, item: Any, index: int) -> None:
        #TODO: this is a insert version of append, where we want to add the new item to the index mentioned,
        # if the index is out of bound, we want to raise IndexError
        new_node = _Node(item)
        if index == 0:
            # Insert the new node at the start of the linked list.
            self._first, new_node.next = new_node, self._first
        else:
            curr = self._first
            curr_index = 0
            while not (curr is None or curr_index == index - 1):
                curr = curr.next
                curr_index = curr_index + 1
            assert curr is None or curr_index == index - 1
            if curr is None:
                # index is out of bounds
                raise IndexError
            else:
                new_node.next = curr.next
                curr.next = new_node



    def delete(self, index: int) -> None:
        # TODO this function should delete the item at the specified index,
        #  if the index is out of bound, we want to raise IndexError
        curr = self._first
        prev = None
        curr_index = 0
        while not (curr is None or curr_index == index):
            prev = curr
            curr = curr.next
            curr_index = curr_index + 1
        assert curr is None or curr_index == index
        if curr is None:
            # index is out of bounds
            raise IndexError
        else:
            prev.next = curr.next

    def pop(self) -> Any:
        #TODO: this function should delete the item at the end of the list, and return it
        pass

    def visualize(self) -> None:
        """Print a visual representation of a linked list."""
        current = self._first

        while current is not None:
            print(f"[{current.item}] -> ", end="")
            current = current.next


    #TODO: Q1, find the largest item inside a given linked list
    def max_item(lst: LinkedList) -> int:
        """Return the largest item stored in the linked list starting at front.

        Preconditions:
            - front is not None
            - all items are integers
        """
        pass


    #TODO: Q2, remove all occurances of a given value from a linked list
    def remove_all(self, target: Any) -> None:
        """Return a linked list identical to front except all occurrences
        of target have been removed.
        """
        curr = self._first
        prev = None
        while not (curr is None):
            if curr.item == target:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

if __name__ == '__main__':
    # create a new linked list
    linky = LinkedList()
    linky.append(1)
    linky.append(2)
    linky.append(2)
    linky.append(2)
    linky.append(2)
    linky.append(2)
    linky.append(2)
    linky.append(3)
    print(linky.visualize())
    linky.remove_all(2)
    print(linky.visualize())
