package Lab_9;

import java.util.AbstractMap;
import java.util.Map;
import java.util.Stack;
import java.util.stream.Stream;

import static java.util.AbstractMap.SimpleEntry;
import static java.util.stream.Collectors.toMap;

class RPNConverter {
    private Stack<Character> operatorStack;
    private static Map<Character, Integer> OPERATOR_PRIOR = Stream.of(
            new AbstractMap.SimpleEntry<>('+', 1),
            new AbstractMap.SimpleEntry<>('-', 1),
            new AbstractMap.SimpleEntry<>('*', 2),
            new AbstractMap.SimpleEntry<>('/', 2),
            new AbstractMap.SimpleEntry<>('(', -1),
            new AbstractMap.SimpleEntry<>(')', -1)
    ).collect(toMap(SimpleEntry::getKey, SimpleEntry::getValue));

    RPNConverter() {
        this.operatorStack = new Stack<>();
    }

    String convert(String e) {
        StringBuilder builder = new StringBuilder();

        while (!e.isEmpty()) {
            char c = e.charAt(0);

            if (Character.isDigit(c) || Character.isSpaceChar(c))
                builder.append(c);
            else if (OPERATOR_PRIOR.containsKey(c))
                builder.append(processOperator(c));
            else throw new IllegalArgumentException("Niewiadomy symbol: " + c);

            e = e.substring(1);
        }

        while (!operatorStack.empty())
            builder.append(" ").append(operatorStack.pop());
        return builder.toString();
    }

    private String processOperator(char operator) {
        if (operatorStack.empty() || operator == '(') {
            operatorStack.push(operator);
        } else {
            Character topOp = operatorStack.peek();
            if (OPERATOR_PRIOR.get(operator) > OPERATOR_PRIOR.get(topOp)) {
                operatorStack.push(operator);
            } else {
                String operators = "";

                while (!operatorStack.empty() && OPERATOR_PRIOR.get(operator) <= OPERATOR_PRIOR.get(topOp)) {
                    operators += " " + operatorStack.pop();
                    if (!operatorStack.empty())
                        topOp = operatorStack.peek();
                    if (topOp == '(') {
                        operatorStack.pop();
                        break;
                    }
                }

                if (operator != ')') operatorStack.push(operator);
                return operators;
            }
        }
        return "";
    }
}
