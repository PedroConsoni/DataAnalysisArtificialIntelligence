# Calculadora de IMC

Este é um projeto simples em Python que calcula o **Índice de Massa Corporal (IMC)** de uma pessoa com base no peso e na altura fornecidos pelo usuário.

---

## 📝 Descrição

O IMC é uma medida internacional usada para calcular se uma pessoa está com **peso abaixo do recomendado, normal, sobrepeso ou obesidade**.  
A fórmula utilizada é:
```
IMC = peso / (altura ** 2)
```

- **peso**: em quilogramas (kg)  
- **altura**: em metros (m)

---

## 💻 Funcionalidades

- Recebe o **peso** e a **altura** do usuário através do terminal.  
- Calcula o IMC utilizando a fórmula acima.  
- Mostra a faixa de peso do usuário:
  - Abaixo do peso  
  - Peso normal  
  - Sobrepeso  
  - Obesidade  
  - Obesidade grave  
- Mostra o IMC com **2 casas decimais** para melhor visualização.

---

## 🚀 Como usar

1. Clone o repositório ou baixe o arquivo `calculadora_imc.py`.  
2. Execute o arquivo no Python:
```
python calculadora_imc.py
```

3. Digite seu peso em kg e altura em metros quando solicitado.  
4. Confira seu IMC e a classificação do seu peso.

---

## 🛠 Tecnologias

- Python 3.x
- Terminal para entrada e saída de dados

---

## 📌 Exemplo de uso
```
Bem-vindo à calculadora de IMC!
Aqui você poderá nos dizer seu peso e sua altura e nós lhe diremos seu Índice de Massa Corporal!

Digite seu peso em KG: 70
Digite sua altura em metros: 1.75
Você está com um peso normal.
Seu IMC é: 22.86
```

---

## ✨ Considerações

Este projeto é uma ótima forma de praticar:
- Entrada de dados do usuário
- Operações matemáticas
- Estruturas condicionais (`if`, `elif`, `else`)
- Formatação de saída com **f-strings**
