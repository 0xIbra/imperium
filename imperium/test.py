from evaluator import Expression

subject = {
    'maker': {
        'original': 'AUDI'
    },
    'model': {
        'original': 'A4'
    },
    'gearbox': {
        'original': 'Manuelle'
    },
    'energy': {
        'original': 'Diesel'
    }
}

expression = Expression()
res = expression.evaluate("exists('subject.maker.original') and subject['maker']['original'] == 'AUDI'", subject)
print(res)