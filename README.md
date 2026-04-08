# 🧮 Calculadora Científica Modular

Projeto desenvolvido para a disciplina de programação do curso Técnico em Informática do **Colégio Cotemig**, com o objetivo de praticar modularização em Python, consumo de APIs externas e boas práticas de organização de código.

---

## 📋 Funcionalidades

- ➕ Soma
- ➖ Subtração
- ✖️ Multiplicação
- ➗ Divisão
- 🔢 Potenciação
- √ Raiz quadrada
- 💵 Cotação do dólar em tempo real (USD → BRL)

---

## 📁 Estrutura do Projeto

```
calculadora-cientifica/
│
├── main.py                  # Ponto de entrada da aplicação
├── funcao_calculadora.py    # Orquestra todas as operações
├── soma.py                  # Módulo de soma
├── subtrair.py              # Módulo de subtração
├── multiplicar.py           # Módulo de multiplicação
├── divisao.py               # Módulo de divisão
├── potencia.py              # Módulo de potenciação
├── raizquadrada.py          # Módulo de raiz quadrada
├── dolar.py                 # Módulo de cotação do dólar (API)
└── README.md
```

---

## 🌐 API Utilizada

O módulo `dolar.py` consome a **AwesomeAPI** para buscar a cotação atual do dólar:

```
GET https://economia.awesomeapi.com.br/json/last/USD-BRL
```

> Não requer autenticação. Retorna o valor de compra (`bid`) do dólar em reais.

---

## ▶️ Como executar

### Pré-requisitos

- Python 3.x instalado
- Biblioteca `requests`

### Instalação da dependência

```bash
pip install requests
```

### Rodando o projeto

```bash
python main.py
```

---

## 💡 Exemplo de uso

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
A cotação do dólar hoje é: R$ 5.73
```

---

## 🛠️ Tecnologias

- **Python 3**
- **requests** (HTTP client)
- **AwesomeAPI** (cotação de moedas)

---

## 👨‍💻 Autor

Desenvolvido por **Henrique** — Técnico em Informática · Colégio Cotemig · Belo Horizonte, MG
