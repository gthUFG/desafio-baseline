# 📍 Calculadora de Distância entre Pontos

Projeto simples em Python para calcular a distância euclidiana entre um ponto informado pelo usuário e um ponto configurado em variáveis de ambiente.

---

## 📖 Sobre o Projeto

O sistema solicita ao usuário dois valores (`x` e `y`) representando um ponto cartesiano e calcula a distância até um ponto previamente definido em um arquivo de configuração (`config.env`).

A fórmula utilizada é:

\[
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

---

## 🗂 Estrutura do Projeto

```text
.
├── desafio-baseline/
│   └── main.py
├── config/
│   └── config.env
├── requirements.txt
├── CONFIG_MAP.md
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- python-dotenv

---

## 📦 Instalação

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Acesse a pasta do projeto:

```bash
cd desafio-baseline
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🔧 Configuração

Crie o arquivo `config.env` dentro da pasta `config/` com o seguinte conteúdo:

```env
PONTO_X=10
PONTO_Y=20
```

---

## ▶️ Execução

Execute o programa com:

```bash
python main.py
```

### Exemplo de uso

```text
Fala um ponto x: 5
Fala um ponto y: 8

Que bacana! O seu ponto é o (5,8)
A distância dele para o ponto registrado no ambiente é: 13.0
```

---

## 🧠 Funcionamento

O programa:

1. Carrega as variáveis de ambiente usando `python-dotenv`
2. Recebe coordenadas do usuário
3. Recupera o ponto configurado no ambiente
4. Calcula a distância euclidiana
5. Exibe o resultado no terminal

---

## 📌 Mapa de Configuração

O projeto segue o documento `CONFIG_MAP.md`, contendo:

- Política de versionamento baseada em SemVer
- Definição dos Itens de Configuração (ICs)
- Responsabilidades da equipe
- Controle de dependências

---

## 🔖 Política de Versionamento

Este projeto utiliza **Versionamento Semântico (SemVer)**:

```text
MAJOR.MINOR.PATCH
```

### Regras

- **MAJOR** → mudanças incompatíveis
- **MINOR** → novas funcionalidades compatíveis
- **PATCH** → correções e melhorias pequenas

### Exemplo

```text
1.0.0
```

---

## 📚 Dependências

Arquivo:

```text
requirements.txt
```

Biblioteca utilizada:

```text
python-dotenv
```

---

## 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos e de aprendizado em gerenciamento de configuração de software e Python.
