# BuscaSyn

Bem-vindo ao **BuscaSyn**!

O BuscaSyn é um projeto que apresenta um algoritmo de busca semântica, utilizando tecnologias de Processamento de Linguagem Natural (NLP) para oferecer resultados de pesquisa mais inteligentes e relevantes. Com o BuscaSyn, você pode realizar buscas de forma autônoma, sem a necessidade de integrar uma API ou instalar o Python e suas dependências, pois disponibilizamos executáveis pré-compilados para Windows, Linux e macOS.

---

## Índice

- [BuscaSyn](#buscasyn)
  - [Índice](#índice)
  - [Introdução](#introdução)
  - [Recursos](#recursos)
  - [Instalação](#instalação)
    - [Download da Release](#download-da-release)
    - [Compilando a Partir do Código Fonte](#compilando-a-partir-do-código-fonte)
  - [Como Usar](#como-usar)
    - [Preparação do schema.json](#preparação-do-schemajson)
      - [Exemplo](#exemplo)
    - [Integração](#integração)
    - [Execução do Programa](#execução-do-programa)
      - [Windows](#windows)
      - [Linux/MacOS](#linuxmacos)
  - [Contribuindo](#contribuindo)
  - [Licença](#licença)

---

## Introdução

O **BuscaSyn** foi desenvolvido para atender à necessidade de desenvolvedores que, em determinadas situações, precisam de uma busca mais inteligente. Utilizando bibliotecas como spaCy e NLTK, nosso objetivo é transformar a forma como você pesquisa informações, fornecendo resultados mais relevantes. Por exemplo, ao buscar o termo "casa", o algoritmo é capaz de trazer resultados como apartamento, condomínio, moradia, lar, entre outros, ampliando as possibilidades de consulta em seu banco de dados.



---

## Recursos

- **Buscador Avançado**  
  Uma combinação de um processamento de linguagem natural com spaCy e NLTK para obter resultados mais inteligentes.

- **Compatibilidade Multi-Plataforma:**  
  Executáveis disponíveis para Windows, Linux e macOS.

- **Execução Independente:**  
  Não requer instalação prévia do Python ou de bibliotecas adicionais.

---

## Instalação

### Download da Release

Para usuários que desejam utilizar o **BuscaSyn** sem compilar o código:

1. Acesse a [página de Releases](https://github.com/seu-usuario/BuscaSyn/releases) do repositório.
2. Baixe o arquivo correspondente ao seu sistema operacional, por exemplo:
   - **windows:**
   `bs.zip`
   - **Linux/MacOS**
   `bs.tar.gz`
3. Extraia o arquivo baixado.
4. Siga as instruções de execução (veja a seção [Como Usar](#como-usar)).

### Compilando a Partir do Código Fonte

Caso você prefira compilar o **BuscaSyn**:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/BuscaSyn.git
   cd BuscaSyn
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   python -m spacy download pt_core_news_lg
   python -m nltk.downloader rslp wordnet omw-1.4
   ```

3. **Compile o Executável:** Utilize o PyInstaller com o arquivo de especificações (`main.spec`)
   ```bash
   pyinstaller main.spec
   ```

---

## Como Usar

Após a instalação ou compilação, você pode executar o BuscaSyn conforme seu sistema operacional:

### Preparação do schema.json

Antes de executar o BuscaSyn, é essencial converter a tabela de dados desejada em um arquivo JSON. Esse arquivo, que pode ter o nome que preferir, deve conter os dados em seu formato bruto, possibilitando que o programa os processe corretamente.

#### Exemplo

✅ Forma aceita:

```json
[
    {
      "id": 1,
      "titulo": "Vazamento em casa",
      "descricao": "Identificado vazamento no banheiro da residência.",
      "categoria": "Manutenção",
      "local": "Casa"
    },
    {
      "id": 2,
      "titulo": "Problema no apartamento",
      "descricao": "O ar-condicionado do apartamento não está funcionando.",
      "categoria": "Eletrônica",
      "local": "Apartamento"
    }
]

```

❌ Forma não aceita

```json
[
    {
        "data":[
            {
                "id": 1,
                "titulo": "Infiltração no condomínio",
                "descricao": "Múltiplos relatos de infiltrações no prédio do condomínio.",
                "categoria": "Infraestrutura",
                "local": "Condomínio"
            },
            {
                "id": 2,
                "titulo": "Reforma no lar",
                "descricao": "Solicitação de reforma geral no imóvel.",
                "categoria": "Reforma",
                "local": "Lar"
            }
        ]
    }
]
```

### Integração
Após preparar o arquivo JSON, integre o programa ao ambiente da linguagem ou framework que você utiliza, garantindo que o BuscaSyn tenha acesso ao arquivo corretamente.

**Em caso de dúvida:** teste o programa separadamente antes de integrá-lo à sua aplicação. Assim, você poderá verificar seu funcionamento e, posteriormente, adicioná-lo ao seu projeto conforme sua necessidade.

### Execução do Programa

Após a preparação do schema.json e a instalação ou compilação do BuscaSyn, você pode executar o programa de acordo com o seu sistema operacional:

#### Windows 
Execute o arquivo (`run.bat`) que, por exemplo, pode conter

    @echo off
    BuscaSyn.exe --arquivo [caminho_do_arquivo] --termo [palavra_digitada]
    pause

#### Linux/MacOS
No terminal, dê permissão de execução (se necessário) e execute

    ./BuscaSyn --arquivo [caminho_do_arquivo] --termo [palavra_digitada]

---

## Contribuindo
Contribuições são muito bem-vindas! Para ajudar a melhorar o BuscaSyn, siga os passos abaixo:

1. Faça um fork deste repositório.
2. Crie uma branch para a sua feature ou correção:
   ```bash
    git checkout -b minha-feature
3. Realize os commits com as suas alterações:
   ```bash
    git commit -m "Descrição da alteração"
4. Envie sua branch para o repositório remoto:
   ```bash
    git push origin minha-feature
5. Abra um Pull Request para que possamos revisar e integrar as suas alterações.


**OBS:** Por favor coloque descrição para que possamos entender o que está sendo feito.

---

## Licença

Este projeto está licenciado sob a MIT License.
Sinta-se à vontade para usar, modificar e distribuir o BuscaSyn conforme suas necessidades.


