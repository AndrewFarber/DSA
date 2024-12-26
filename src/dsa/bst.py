"""
This module provides an implementation for a binary search tree.
"""

from __future__ import annotations
from typing import Any


class Node:
    def __init__(self, key: Any) -> None:
        self.key: Any = key
        self.left: Node | None = None
        self.right: Node | None = None

    def __repr__(self) -> str:
        return f"<Node(key={self.key})>"


class BinarySearchTree:
    def __init__(self) -> None:
        self._root: Node | None = None

    @property
    def root(self) -> Node | None:
        """
        The root node of the BST.
        """
        return self._root

    def _insert(self, node: Node | None, key: Any) -> Node | None:
        if node is None:
            return Node(key)
        if key == node.key:
            return node
        elif key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def insert(self, key: Any) -> None:
        """
        Insert a node with the specified key.
        """
        self._root = self._insert(self._root, key)

    def _search(self, node: Node | None, key: Any) -> Node | None:
        if node is None:
            return None
        elif node.key == key:
            return node
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def search(self, key: Any) -> Node | None:
        """
        Search for a node with the specified key.
        Returns None if the node does not exist.
        """
        return self._search(self._root, key)

    def _successor(self, node: Node) -> Node:
        """Returned successor is the smallest of the larger keys."""
        # _successor only called with node has left & right children.
        # The returned node is always a leaf.
        assert node.right is not None
        node = node.right
        while node is not None and node.left is not None:
            node = node.left
        return node

    def _delete(self, node: Node | None, key: Any) -> Node | None:
        # key not in BST
        if node is None:
            return None

        if node.key > key:
            node.left = self._delete(node.left, key)
        elif node.key < key:
            node.right = self._delete(node.right, key)
        else:
            # Found key in BST. Skip
            # over the node to delete
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = self._successor(node)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        return node

    def delete(self, key: Any) -> None:
        """
        Remove a node with the specified key.
        """
        self._delete(self._root, key)

    def _preorder(self, node: Node | None, lst: list[Any]) -> None:
        if node is None:
            return
        lst.append(node.key)
        self._preorder(node.left, lst)
        self._preorder(node.right, lst)

    def preorder(self) -> list[Any]:
        """
        Pre-order traversal of the BST.
        Returns a list containing all keys.
        """
        lst: list[Any] = list()
        self._preorder(self._root, lst)
        return lst

    def _inorder(self, node: Node | None, lst: list[Any]) -> None:
        if node is None:
            return
        self._inorder(node.left, lst)
        lst.append(node.key)
        self._inorder(node.right, lst)

    def inorder(self) -> list[Any]:
        """
        In-order traversal of the BST.
        Returns a list containing all keys.
        """
        lst: list[Any] = list()
        self._inorder(self._root, lst)
        return lst

    def _postorder(self, node: Node | None, lst: list[Any]) -> None:
        if node is None:
            return
        self._postorder(node.left, lst)
        self._postorder(node.right, lst)
        lst.append(node.key)

    def postorder(self) -> list[Any]:
        """
        Post-order traversal of the BST.
        Returns a list containing all keys.
        """
        lst: list[Any] = list()
        self._postorder(self._root, lst)
        return lst
