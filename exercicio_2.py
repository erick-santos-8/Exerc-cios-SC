import math
import itertools
from collections import Counter

def cifrar_transposicao(texto, chave):
  cifra = ''
  n_col = len(chave)
  n_lin = math.ceil(len(texto) / n_col)
  preenchimento = n_lin * n_col
  texto = texto.ljust(preenchimento)

  matriz = [list(texto[i:i+n_col]) for i in range(0, len(texto), n_col)]
    
  chave_ordem = sorted(list(enumerate(chave)), key=lambda x: x[1])
  for i, _ in chave_ordem:
      for linha in matriz:
          cifra += linha[i]
  return cifra

print(cifrar_transposicao("criptografia", [2, 0, 1]))
print(cifrar_transposicao("abc", [1,0]))
print(cifrar_transposicao("a cifra por transposicao e um metodo classico de criptografia", [3,1,0,2]))