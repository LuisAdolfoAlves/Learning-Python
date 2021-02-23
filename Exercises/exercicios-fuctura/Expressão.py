'''Compute a saída da seguinte expressão matemática sem realizar
nenhuma simplificação:\n","$ a^{2} + \\frac{3}{4} \\times b \\times 987(c - \\frac{10^{-9}}{\\sqrt{0.5^{3}}}) $.
Assuma que os valores das variáveis a, b e c correpondam a 2, 4 e 8, respectivamente. Armazene o resultado em uma variável.\n","\n","
Dica: consulte os operadores aritméticos disponíveis no Python. Utilize a biblioteca math para operação de raiz."]}'''

import math as m
import fractions as f
# a^{2} + \\frac{3}{4} \\times b \\times 987(c - \\frac{10^{-9}}{\\sqrt{0.5^{3}}})

a = 2
b = 4
c = 8

expressao = 1 ** 2 + f.Fraction(3, 4) * 4 * 987 * ((8 - f.Fraction(10 ** -9)) * m.sqrt(0.5 ** 3))
print(expressao)
