from imperium_legacy import Expression

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

expr = "exists('$subject.maker.original', $out) and $subject['maker']['original'] == 'AUDI' and matches('(diesel)', $out['energy']['original'], 'i') and in is None"

expression = Expression()
res = expression.evaluate(expr, subject)
print('Result: ', res)
