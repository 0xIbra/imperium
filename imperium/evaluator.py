from imperium.helpers import exists, matches
import parser, re

AUTHORIZED_FUNCTIONS = { 
    'exists': True,
    'matches': True
}

class Expression:

    def evaluate(self, expression, subject):
        self.expression = expression
        self.subject = subject

        matched = re.findall("([a-zA-Z_{1}][a-zA-Z0-9_]+)\s?\(", expression)
        for match in matched:
            if match not in AUTHORIZED_FUNCTIONS:
                print('[error] Unauthorized function usage "{}"'.format(match))
                exit(1)

        expression = expression.replace('$subject', 'subject')
        expr = parser.expr(expression)

        return eval(expr.compile(''))