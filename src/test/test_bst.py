import pytest

from dsa.bst import BinarySearchTree


@pytest.fixture
def bst():
    """Fixture to create a BST with predefined nodes for testing."""
    tree = BinarySearchTree()
    for key in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(key)
    return tree


def test_insert(bst):
    bst.insert(25)
    assert bst.search(25) is not None
    assert bst.search(25).key == 25


def test_search_existing_key(bst):
    node = bst.search(70)
    assert node is not None
    assert node.key == 70


def test_search_nonexistent_key(bst):
    node = bst.search(100)
    assert node is None


def test_delete_leaf_node(bst):
    bst.delete(20)  # Leaf node
    assert bst.search(20) is None
    assert bst.inorder() == [30, 40, 50, 60, 70, 80]


def test_delete_node_with_one_child(bst):
    bst.insert(65)
    bst.delete(60)  # Node with one child
    assert bst.search(60) is None
    assert bst.inorder() == [20, 30, 40, 50, 65, 70, 80]


def test_delete_node_with_two_children(bst):
    bst.delete(70)
    assert bst.search(70) is None
    assert bst.inorder() == [20, 30, 40, 50, 60, 80]


def test_preorder_traversal(bst):
    assert bst.preorder() == [50, 30, 20, 40, 70, 60, 80]


def test_inorder_traversal(bst):
    assert bst.inorder() == [20, 30, 40, 50, 60, 70, 80]


def test_postorder_traversal(bst):
    assert bst.postorder() == [20, 40, 30, 60, 80, 70, 50]


def test_delete_root_node():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.delete(10)
    assert bst.search(10) is None
    assert bst.inorder() == [5, 15]
