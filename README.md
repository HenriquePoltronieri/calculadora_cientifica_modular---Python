# 🧮 Calculadora Científica Modular

Projeto desenvolvido em Python com arquitetura modular, onde cada operação matemática é isolada em seu próprio arquivo. Ideal para aprender conceitos de organização de código, importação de módulos e funções em Python.

---

## 📁 Estrutura do Projeto

```
calculadora_cientifica/
│
├── main.py                  # Ponto de entrada do programa
├── funcao_calculadora.py    # Função principal que une todos os módulos
│
├── soma.py                  # Operação de soma
├── subtrair.py              # Operação de subtração
├── multiplicar.py           # Operação de multiplicação
├── divisao.py               # Operação de divisão (com tratamento de erro)
├── potencia.py              # Operação de potenciação
└── raizquadrada.py          # Operação de raiz quadrada (com tratamento de erro)
```

---

## ⚙️ Funcionalidades

| Operação       | Arquivo            | Observação                              |
|----------------|--------------------|------------------------------------------|
| Soma           | `soma.py`          | —                                        |
| Subtração      | `subtrair.py`      | —                                        |
| Multiplicação  | `multiplicar.py`   | —                                        |
| Divisão        | `divisao.py`       | Retorna erro se o divisor for zero       |
| Potência       | `potencia.py`      | Calcula `a ** b`                         |
| Raiz Quadrada  | `raizquadrada.py`  | Retorna erro se o número for negativo    |

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.x instalado
- (Recomendado) Ambiente virtual ativo

### Passo a passo

**1. Clone ou copie os arquivos do projeto para uma pasta:**

```bash
mkdir calculadora_cientifica
cd calculadora_cientifica
```

**2. Crie e ative um ambiente virtual:**

```bash
# Criar
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (Linux/macOS)
source venv/bin/activate
```

**3. Execute o programa:**

```bash
python main.py
```

### Exemplo de uso

```
Qual o valor do primeiro número: 9
Qual o valor do segundo número: 3

Resultados:
Soma: 12.0
Subtração: 6.0
Multiplicação: 27.0
Divisão: 3.0
Potência: 729.0
Raiz quadrada: 3.0
```

---

## 🧩 Como o Projeto Funciona

O programa segue um fluxo simples de 3 camadas:

```
main.py
  └── funcao_calculadora.py   ← importa e orquestra todos os módulos
        ├── soma.py
        ├── subtrair.py
        ├── multiplicar.py
        ├── divisao.py
        ├── potencia.py
        └── raizquadrada.py
```

1. **`main.py`** é o ponto de partida — chama a função `calculadora()`.
2. **`funcao_calculadora.py`** solicita os valores ao usuário e exibe os resultados usando as funções importadas.
3. Cada arquivo de operação contém apenas **uma função** responsável por um único cálculo.

---

## 🛡️ Tratamento de Erros

- **Divisão por zero:** caso o segundo número seja `0`, a divisão retorna a mensagem `"Erro: divisão por zero"` em vez de lançar uma exceção.
- **Raiz de número negativo:** caso o número seja negativo, a função retorna `"Erro: número negativo"`.

---

## 📚 Conceitos Abordados

- Criação e organização de módulos em Python
- Importação com `from modulo import funcao`
- Uso de `if __name__ == "__main__"`
- Funções com parâmetros e retorno de valores
- Tratamento básico de erros com condicionais
- Boas práticas de separação de responsabilidades

