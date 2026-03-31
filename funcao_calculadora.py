from soma import somar
from subtrair import subtrair
from multiplicar import multiplicar
from divisao import dividir
from potencia import potencia
from raizquadrada import raiz_quadrada

def calculadora():
    a = float(input("Qual o valor do primeiro número: "))
    b = float(input("Qual o valor do segundo número: "))

    print("\nResultados:")
    print("Soma:", somar(a, b))
    print("Subtração:", subtrair(a, b))
    print("Multiplicação:", multiplicar(a, b))
    print("Divisão:", dividir(a, b))
    print("Potência:", potencia(a, b))
    print("Raiz quadrada:", raiz_quadrada(a))
