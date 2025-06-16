# 📈 BayesInvest – Previsão de Investimentos com Teorema de Bayes
O BayesInvest é uma aplicação interativa desenvolvida com Streamlit que estima a probabilidade de um investimento ter retorno positivo, utilizando uma abordagem baseada no Teorema de Bayes (modelo Naive Bayes). O sistema considera variáveis como o tipo de investimento, o perfil de risco e o tempo de aplicação, com uma interface simples e intuitiva.

## 🎯 Objetivo

- Desenvolver um sistema inteligente e acessível que:

- Permita ao usuário inserir características do investimento.

- Utilize o Teorema de Bayes para prever a probabilidade de retorno positivo.

- Sirva como ferramenta educacional ou de simulação de cenários de investimento.


## 🛠️ Tecnologias Utilizadas

- Python: Linguagem principal

- Streamlit: Criação da interface web

- Pandas: Manipulação de dados

- Scikit-learn: Modelo Naive Bayes com CategoricalNB

 
 ## 💡 Lógica do Sistema

 Entradas do usuário:

- Tipo de Investimento: Ações, Criptomoedas, Renda Fixa

- Perfil de Risco: Baixo, Médio, Alto

- Tempo de Investimento: Curto, Médio, Longo Prazo

Processamento:

- Geração de uma base de dados fictícia com essas variáveis.

- Codificação categórica com LabelEncoder.

- Treinamento de um classificador CategoricalNB.

- Predição da probabilidade de retorno positivo.


## 💻 Interface do Usuário

- A aplicação possui uma interface amigável e direta:

- Menu com campos para seleção das opções.

- Resultado da probabilidade exibido em formato percentual com destaque visual.

- Código executável diretamente do navegador via Streamlit.


## 🚀 Como Executar o Projeto

### 1. Clone este repositório

```bash
git clone https://github.com/seu-usuario/bayesinvest.git
cd bayesinvest
```
### 2. Instale os pacotes necessários:

```bash
pip install streamlit scikit-learn pandas
```
### 3. Execute a aplicação:
```bash
streamlit run bayesinvest_app.py
```

Acesse no navegador: [http://localhost:8501](http://localhost:8501)

## 🧪 Exemplo de Uso

Suponha que o usuário selecione:

- Tipo: Criptomoedas

- Perfil de Risco: Alto

- Tempo: Longo Prazo

O sistema retorna, por exemplo:

*Chance de Retorno Positivo: 78.33%*

## 🛠️ Compilação (opcional)

Para transformar o projeto em um executável .exe:

### 1. Instale o PyInstaller:

```bash
pip install pyinstaller
```
### 2. Gere o executável:

```bash
pyinstaller --onefile bayesinvest_app.py
```
O executável estará na pasta dist/.

## 📂 Organização dos Arquivos do Projeto

```
bayesinvest/
│
├── README.md    
├──  index.html
├──  invest.py              
└──  style.css      
```

## ✅ Conclusão

O BayesInvest é uma aplicação simples e funcional que demonstra como a inteligência artificial e a estatística podem ser aplicadas ao mundo dos investimentos. O sistema combina conceitos matemáticos com uma interface acessível, oferecendo uma experiência prática e educativa.


