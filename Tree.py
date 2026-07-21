from __future__ import annotations
from typing import Any, Optional


class Tree:
    """A recursive tree data structure.

    Representation Invariants:
        - self._root is not None or self._subtrees == []
    """
    # Private Instance Attributes:
    #   - _root:
    #       The item stored at this tree's root, or None if the tree is empty.
    #   - _subtrees:
    #       The list of subtrees of this tree. This attribute is empty when
    #       self._root is None (representing an empty tree). However, this attribute
    #       may be empty when self._root is not None, which represents a tree consisting
    #       of just one item.
    _root: Optional[Any]
    _subtrees: list[Tree]

    def __init__(self, root: Optional[Any], subtrees: list[Tree]) -> None:
        """Initialize a new Tree with the given root value and subtrees.

        If root is None, the tree is empty.

        Preconditions:
            - root is not none or subtrees == []
        """
        self._root = root
        self._subtrees = subtrees

    def is_empty(self) -> bool:
        """Return whether this tree is empty.
        """
        return self._root is None

    def __len__(self) -> int:
        """Return the number of items contained in this tree.

        >>> t1 = Tree(None, [])
        >>> len(t1)
        0
        >>> t2 = Tree(3, [Tree(4, []), Tree(1, [])])
        >>> len(t2)
        3
        """
        if self.is_empty():
            return 0
        else:
            return 1 + sum(subtree.__len__() for subtree in self._subtrees)

    def __str__(self) -> str:
        """Return a string representation of this tree.
        """
        return self._str_indented()

    def _str_indented(self, depth: int = 0) -> str:
        """Return an indented string representation of this tree.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return ''
        else:
            str_so_far = '  ' * depth + f'{self._root}\n'
            for subtree in self._subtrees:
                # Note that the 'depth' argument to the recursive call is modified.
                str_so_far += subtree._str_indented(depth + 1)
            return str_so_far

    def remove(self, item: Any) -> bool:
        """..."""
        if self.is_empty():
            return False
        elif self._root == item:
            self._delete_root()  # delete the root
            return True
        else:
            for subtree in self._subtrees:
                deleted = subtree.remove(item)
                if deleted and subtree.is_empty():
                    # The item was deleted and the subtree is now empty.
                    # We should remove the subtree from the list of subtrees.
                    # Note that mutate a list while looping through it is
                    # EXTREMELY DANGEROUS!
                    # We are only doing it because we return immediately
                    # afterwards, and so no more loop iterations occur.
                    self._subtrees.remove(subtree)
                    return True
                elif deleted:
                    # The item was deleted, and the subtree is not empty.
                    return True

            # If the loop doesn't return early, the item was not deleted from
            # any of the subtrees. In this case, the item does not appear
            # in this tree.
            return False

    def _delete_root(self) -> None:
        """..."""
        if self._subtrees == []:
            self._root = None
        else:
            # Get the last subtree in this tree.
            chosen_subtree = self._subtrees.pop()

            self._root = chosen_subtree._root
            self._subtrees.extend(chosen_subtree._subtrees)

    def insert(self, item: Any) -> bool:
        if self.is_empty():
            self._root = item
            return True
        else:
            if len(self._subtrees) < 2:
                self._subtrees.append(Tree(item, []))
                return True
            else:
                for subtree in self._subtrees:
                    inserted = subtree.insert(item)
                    if inserted:
                        return True
                    else:
                        continue
                return False
        #TODO: currently this insert doesnt exactly work as intended, it is repeatedly adding new nodes to only the left
        # side of the tree, this is likely because the if check only checks the current node and not the subtrees,
        # so it will always add to the leftmost node that has less than 2 children.

if __name__ == "__main__":
    t2 = Tree(1, [Tree(2, []), Tree(3, [])])
    print(t2)
    t2.insert(4)
    print(t2)
    t2.insert(5)
    print(t2)
    t2.insert(6)
    print(t2)
    t2.insert(7)
    print(t2)
