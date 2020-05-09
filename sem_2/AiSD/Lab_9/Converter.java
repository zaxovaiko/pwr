package Lab_9;

import java.util.List;
import java.util.Stack;

class Converter {
    private List<Character> OPERATORS = List.of('+', '-', '/', '*');

    RPNTree convert(String expression) {
        Stack<RPNTree.Node<String>> stack = new Stack<>();
        String[] array = expression.split("\\s+");

        for (String s : array) {
            RPNTree.Node<String> node = new RPNTree.Node<>(s);

            if (s.length() == 1 && OPERATORS.contains(s.charAt(0))) {
                node.right = stack.pop();
                node.left = stack.pop();
            }
            stack.push(node);
        }

        return new RPNTree(stack.pop());
    }
}
