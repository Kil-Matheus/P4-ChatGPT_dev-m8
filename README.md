# P4-ChatGPT_dev-m8

## Descrição

Este projeto é uma implementação de um chatbot utilizando a API do GPT-3.5 integrado a um framework de front-end Gradio.

## Desenvolvimento do Ambiente

Foi seguido os tutoriais disponibilizados pelo Professor Nicola durante as aulas, para a criação do ambiente de desenvolvimento. Para está ponderada, foi entrege a versão com a API OpenAI.
O segundo ambiente utilizando o Ollama foi criado, mas não completamente concluido.

### Dotenv (dotenv)

O código utiliza a biblioteca `dotenv` para carregar variáveis de ambiente a partir de um arquivo `.env`. Este arquivo armazena informações sensíveis, como chaves de API, de forma a manter essas informações seguras e separadas do código fonte.

### OpenAI API

Para utilizar a API do OpenAI, é necessário criar uma conta no site da [OpenAI](https://openai.com/), e criar uma chave de API. Esta chave deve ser armazenada no arquivo `.env` com o nome `OPENAI_API_KEY`.

**1° Observação**: A chave de API é sensível e não deve ser compartilhada. 

**2° Observação**: A chave de API possui um perído de teste, limitado a uma cota de 5 dólares para o uso dos modelos. Para mais informações, consulte a [documentação](https://beta.openai.com/docs/developer-quickstart/your-api-keys).

### Anaconda

Para a instalação do Anaconda, foi seguido o tutorial disponibilizado pelo Professor Nicola, durante as aulas.

1. Baixar o instalador do Anaconda:

    ```bash
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && bash Miniconda3-latest-Linux-x86_64.sh
    ```

2. Criar um ambiente virtual:

    ```bash
    conda create -n llm python=3.11
    ```

3. No meu ambiente, eu precisei utilizar um 3° comando não disponibilizado no tutorial, para que o ambiente fosse criado:

    ```bash
    export PATH="$HOME/miniconda3/bin:$PATH"
    ```
4. Ativar o ambiente virtual:

    ```bash
    conda activate llm
    ```
5. Executar o Ambiente:

    ```bash
    python3 lang_streaming.py
    ```
**Observação**: O ambiente virtual deve ser ativado sempre que for executar o código e a aplicação necessita de uma chave de acesso para funcionar.

## Link do funcionamento da aplicação

[Link do funcionamento da aplicação](https://drive.google.com/file/d/1Gu8OcqP2MsUbIuJhF1IHnstAazz-T5YW/view?usp=sharing)