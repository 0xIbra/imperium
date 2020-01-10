# Imperium
> Imperium is a python package that allows you to easily evaluate python expressions

## Installation
```bash
pip install imperium
```

## Usage
```python
from imperium.evaluator import Expression

obj = {
    'name': 'iPhone',
    'model': '11 Pro',
    'price': 1299.90,
    'state': 'new'
}

expr = Expression()
if expr.evaluate('$subject.state == "new"', obj): # "$subject" is a reserved key
    # Your logic
```
To access the data in the given subject, use the "$subject" key as shown above.

### Check if the subject has an attribute
```python
from imperium.evaluator import Expression

obj = {
    'name': 'iPhone',
    'model': '11 Pro',
    'price': 1299.90,
    'state': 'new'
}

someother_obj = {
    'name': 'John Doe'
}

expr = Expression()
res = expr.evaluate('exists("$subject.price", $subject)', subject=obj, source=someother_obj) # REMINDER: "$subject" key let's you access the object that you passed to the evaluate method (obj in this case)
print(res) # Output: True
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

buyer = {
    'fullname': 'John Doe'
}

# Passing the name attribute of the subject
# REMINDER: "$subject" let's you access the object/subject passed to the evaluate method (obj in this case)
# and "$source" let's you access the optional source object passed to the evaluate method 
expression = "exists('$subject.name', $subject) && matches('IPHONE', $subject['name'], 'i')"

expr = Expression()
res = expr.evaluate(expression, subject=obj, source=buyer)
print(res) # Output: True
```

**Imperium** has built-in functions to simplify certain actions/verifications.

Function        |   Argument(s)                             |   Description
----------------|-------------------------------------------|----------------
**exists()**    | key (Ex: $subject.price), $subject        | Checks if the given attribute/key exists in the given subject.
**matches()**   | regex, value, flag (**i** or **m**)       | Tests a regular expression