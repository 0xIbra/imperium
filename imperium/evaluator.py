import parser, re

class Expression:

    def evaluate(self, expression, subject):
        self.expression = expression
        self.subject = subject

        matches = re.findall("([a-zA-Z_{1}][a-zA-Z0-9_]+)\s?\(", expression)
        for match in matches:
            if match == 'print':
                continue

            expression = expression.replace('{}('.format(match), 'self.{}('.format(match))

        expr = parser.expr(expression)

        return eval(expr.compile(''))

    def exists(self, path):
        subject = self.subject
        split = path.split('.')
        for value in split:
            if value == 'subject':
                continue

            if not value in subject:
                return False
            
            subject = subject[value]
        
        return True

    def matches(self, expr, value, flag=None):
        if flag is not None:
            if flag == 'i':
                result = re.match(expr, value, re.IGNORECASE)
            elif flag == 'm':
                result = re.match(expr, value, re.MULTILINE)
        else:
            result = re.match(expr, value)

        if result:
            return True
        else:
            return False