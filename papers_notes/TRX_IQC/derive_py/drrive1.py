from sympy import init_printing, Symbol, expand
from sympy.printing import latex
init_printing()
a = Symbol('a')
b = Symbol('b')
e = (a + b)**5
out = e.expand()
print(latex(out))