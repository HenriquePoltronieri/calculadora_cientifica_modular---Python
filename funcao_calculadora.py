from soma import somar
from subtrair import subtrair
from multiplicar import multiplicar
from divisao import dividir
from potencia import potencia
from raizquadrada import raiz_quadrada
from dolar import cotacao_dolar

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

    cotacao = cotacao_dolar()
    if cotacao is not None:
        print(f"A cotação do dólar hoje é: R$ {cotacao:.2f}")