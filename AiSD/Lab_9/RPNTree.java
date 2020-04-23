package Lab_9;

import java.util.List;

class RPNTree extends Tree<String> {
    private List<Character> OPERATORS = List.of('+', '-', '/', '*');

    RPNTree(Node<String> node) {
        super(node);
    }

    double solve() {
        Node<String> copy = root;
        return solve(copy);
    }

    private double solve(Node<String> node) {
        if (node.left.elem.length() == 1 && OPERATORS.contains(node.left.elem.charAt(0))) {
            solve(node.left);
        }

        if (node.right.elem.length() == 1 && OPERATORS.contains(node.right.elem.charAt(0))) {
            solve(node.right);
        }

        double left = Double.parseDouble(node.left.elem);
        double right = Double.parseDouble(node.right.elem);
        double result = calculate(node.elem.charAt(0), left, right);

        node.elem = String.valueOf(result);
        return result;
    }

    private double calculate(char operator, double val1, double val2) {
        switch (operator) {
            case '+':
                return val1 + val2;
            case '-':
                return val1 - val2;
            case '*':
                return val1 * val2;
            case '/':
                if (val2 == 0) {
                    System.err.println("Nie wolno dzielic przez zero.");
                    System.exit(-1);
                }
                return val1 / val2;
            default:
                throw new IllegalStateException("Niewiadomy operator " + operator);
        }
    }
}
