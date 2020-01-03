# Imperium
> Imperium is a python package that allows you to easily evaluate python expressions

## Installation
```bash
pip install imperium
```

## Usage
```python
from imperium.evaluator import Expression

subject = {
    'name': 'iPhone',
    'model': '11 Pro',
    'price': 1299.90,
    'state': 'new'
}

expr = Expression()
if expr.evaluate('subject.state == "new"', subject): # "subject" is a reserved key
    # Your logic
```
To access the data in the given subject, use the "subject" key as shown above.

### Check if the subject has an attribute
```python
from imperium.evaluator import Expression

obj = {
    'name': 'iPhone',
    'model': '11 Pro',
    'price': 1299.90,
    'state': 'new'
}

expr = Expression()
print(expr.evaluate('exists("subject.price")'), obj) # Output: True
```

### Testing regular expressions
```python
from imperium.evaluator import Expression

obj = {
    'name': 'iPhone',
    'model': '11 Pro',
    'price': 1299.90,
    'state': 'new'
}

expression = "exists('subject.name') && matches('IPHONE', subject['name'], 'i')"

expr = Expression()
res = expr.evaluate(expression, obj)
print(res) # Output: True
```

**Imperium** has built-in functions to facilitate certain actions/verifications.
Function        |   Argument(s)                 |   Description
----------------|-------------------------------|----------------
**exists()**    | key (Ex: subject.price)       | Checks if the given attribute/key exists in the subject.
**matches()**   | regex, value, flag (i | m)    | Tests a regular expression