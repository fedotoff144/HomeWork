public class RedBlackTree<T extends Comparable<T>> {

    private static final boolean RED = true;
    private static final boolean BLACK = false;

    private class Node {
        T value;
        Node left, right;
        boolean color;

        Node(T value, boolean color) {
            this.value = value;
            this.color = color;
        }
    }

    private Node root;

    public void insert(T value) {
        root = insert(root, value);
        root.color = BLACK;
    }

    private Node insert(Node node, T value) {
        if (node == null) {
            return new Node(value, RED);
        }

        if (value.compareTo(node.value) < 0) {
            node.left = insert(node.left, value);
        } else if (value.compareTo(node.value) > 0) {
            node.right = insert(node.right, value);
        } else {
            node.value = value;
        }

        if (isRed(node.right) && !isRed(node.left)) {
            node = rotateLeft(node);
        }
        if (isRed(node.left) && isRed(node.left.left)) {
            node = rotateRight(node);
        }
        if (isRed(node.left) && isRed(node.right)) {
            flipColors(node);
        }

        return node;
    }

    private boolean isRed(Node node) {
        if (node == null) {
            return false;
        }
        return node.color == RED;
    }

    private Node rotateLeft(Node node) {
        Node x = node.right;
        node.right = x.left;
        x.left = node;
        x.color = node.color;
        node.color = RED;
        return x;
    }

    private Node rotateRight(Node node) {
        Node x = node.left;
        node.left = x.right;
        x.right = node;
        x.color = node.color;
        node.color = RED;
        return x;
    }

    private void flipColors(Node node) {
        node.color = RED;
        node.left.color = BLACK;
        node.right.color = BLACK;
    }
}