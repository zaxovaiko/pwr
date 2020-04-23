package Lab_5;

class InfixtoPostfix {
    private Stos<Character> stos;
    private String postfix;

    class Expression {
        String op, ex;
        int precedence = 3;

        Expression(String e) {
            ex = e;
        }

        Expression(String e1, String e2, String o) throws Exception {
            ex = String.format("%s %s %s", e1, o, e2);
            op = o;
            precedence = precedence(o.charAt(0));
        }

        @Override
        public String toString() {
            return ex;
        }
    }

    String reverseConvert(String tofix) throws Exception {
        Stos<Expression> expression = new Stos<>();

        for (String token : tofix.split("\\s")) {
            char c = token.charAt(0);                      // Pierwszy symbol
            int prec = isOperator(c) ? precedence(c) : -1; // Priorytet operatora albo -1

            if (prec != -1 && token.length() == 1) {
                Expression r = expression.pop(); // Pierwsze wyrażenie
                Expression l = expression.pop(); // Drugie wyrażenie

                if (l.precedence <= prec) l.ex = '(' + l.ex + ')';
                if (r.precedence <= prec) r.ex = '(' + r.ex + ')';

                expression.push(new Expression(l.ex, r.ex, token));
            } else {
                expression.push(new Expression(token));
            }
        }
        return expression.peek().ex;
    }

    String convert(String infix) throws Exception {
        stos = new Stos<>();
        postfix = "";

        for (char c : infix.toCharArray()) {
            if (isOperator(c)) {
                postfix += " ";
                processOperator(c);
            } else if (Character.isDigit(c))
                postfix += c;
            else throw new Exception("Niepoprawne wyrażenie.");
        }

        while (!stos.empty()) {
            char topOp = stos.pop();
            if (topOp != '(' && topOp != ')') {
                postfix += " " + topOp;
            }
        }

        return postfix;
    }

    double calc() throws Exception {
        Stos<Double> stos = new Stos<>();

        for (String c : postfix.split("\\s")) {
            if (c.length() != 0 && isOperator(c.charAt(0))) {
                double arg2 = stos.pop();
                double arg1 = stos.pop();
                double result;

                if (c.equals(Character.toString('+')))
                    result = arg1 + arg2;
                else if (c.equals(Character.toString('-')))
                    result = arg1 - arg2;
                else if (c.equals(Character.toString('*')))
                    result = arg1 * arg2;
                else if (c.equals(Character.toString('/')))
                    if (arg2 != 0)
                        result = arg1 / arg2;
                    else
                        throw new Exception("Nie wolno dzielić przez 0");
                else if (c.equals(Character.toString('%')))
                    result = arg1 % arg2;
                else
                    throw new Exception("Nie ma takiego operatora");

                stos.push(result);
            } else if (!c.equals("")) {
                stos.push(Double.parseDouble(c));
            }
        }
        return stos.pop();
    }

    private int precedence(char op) throws Exception {
        switch (op) {
            case '+':
                return 1;
            case '-':
                return 1;
            case '*':
                return 2;
            case '/':
                return 2;
            case '%':
                return 2;
            case '(':
                return -1;
            case ')':
                return -1;
            default:
                throw new Exception("Niewiadomy operator.");
        }
    }

    private void processOperator(char o) throws Exception {
        if (stos.empty() || o == '(') {
            stos.push(o);
        } else {
            char topOp = stos.peek();
            int topOpPrior = precedence(topOp);
            int curOpPrior = precedence(o);

            if (curOpPrior > topOpPrior) {
                stos.push(o);
            } else {
                while (!stos.empty() && curOpPrior <= topOpPrior) {
                    topOp = stos.pop();
                    if (topOp == '(') {
                        break;
                    }
                    topOpPrior = precedence(topOp);
                    postfix += topOp + " ";
                }
                if (o != ')') {
                    stos.push(o);
                }
            }
        }
    }

    private boolean isOperator(char c) {
        return c == '+' || c == '-' || c == '/' || c == '*' || c == '%' || c == '(' || c == ')';
    }
}