package Lab_9;

import java.util.LinkedList;
import java.util.Queue;

class Tree<T> {
    Node<T> root;

    Tree(Node<T> node) {
        this.root = node;
    }

    void printInOrder() {
        printInOrder(root);
    }

    private void printInOrder(Node<T> root) {
        if (root.left != null) {
            System.out.print("(");
            printInOrder(root.left);
        }
        System.out.print(root.elem);
        if (root.right != null) {
            printInOrder(root.right);
            System.out.print(")");
        }
    }

    void printPostOrder() {
        printPostOrder(root);
    }

    private void printPostOrder(Node<T> node) {
        if (node.left != null)
            printPostOrder(node.left);
        if (node.right != null)
            printPostOrder(node.right);

        System.out.printf("%s ", node.elem);
    }

    int leafs() {
        return leafs(root);
    }

    private int leafs(Node<T> node) {
        if (node == null)
            return 0;

        if (node.left == null && node.right == null)
            return 1;

        return leafs(node.left) + leafs(node.right);
    }

    int nodes() {
        return nodes(root);
    }

    private int nodes(Node<T> node) {
        int nodes = 1;
        if (node.right != null) nodes += nodes(node.right);
        if (node.left != null) nodes += nodes(node.left);
        return nodes;
    }

    int height() {
        return height(root);
    }

    private int height(Node<T> node) {
        if (node == null) return -1;
        int left = height(node.left);
        int right = height(node.right);
        return Math.max(left, right) + 1;
    }

    void printHorizontally() {
        Queue<Node<T>> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            Node<T> temp = queue.poll();
            System.out.print(temp.elem + " ");
            if (temp.left != null) queue.add(temp.left);
            if (temp.right != null) queue.add(temp.right);
        }
    }

    static class Node<T> {
        T elem;
        Node<T> left;
        Node<T> right;

        Node(T elem) {
            this.elem = elem;
        }

        @Override
        public String toString() {
            return elem.toString();
        }
    }
}