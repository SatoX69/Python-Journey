def compute(n1=None, n2=None, operator=None):
    if not operator:
        return "Include Operator:\n\tAdd, Sub, Mul, Div"
    elif not n1 or not n2:
        return "Pass the first two numeric args"
    switch = {
         'add': n1 + n2,
         'sub': n1 - n2,
         'mul': n1 * n2,
         'div': n1 / n2
         }
    return int(switch.get(operator))

result = compute(operator='div', n1=10, n2=2)
print(result)