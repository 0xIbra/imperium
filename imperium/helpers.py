import re

def exists(key, subject):
    split = key.split('.')
    for value in split:
        if value == 'subject':
            continue

        if not value in subject:
            return False
        
        subject = subject[value]
    
    return True

def matches(expr, subject, flag=None):
    flag = flag.lower()
    if flag is not None:
        if flag == 'i':
            result = re.match(expr, subject, re.IGNORECASE)
        elif flag == 'm':
            result = re.match(expr, subject, re.MULTILINE)
    else:
        result = re.match(expr, subject)

    if result:
        return True
    else:
        return False