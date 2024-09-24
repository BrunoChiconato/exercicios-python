# Sumário

- [Sumário](#sumário)
  - [Exercícios de Tuplas, Listas e Dicionários](#exercícios-de-tuplas-listas-e-dicionários)
      - [1. Manipulação de Tuplas](#1-manipulação-de-tuplas)
      - [2. Manipulação de Listas](#2-manipulação-de-listas)
      - [3. Manipulação de Dicionários](#3-manipulação-de-dicionários)
      - [4. Integração de Estruturas (Tuplas, Listas e Dicionários)](#4-integração-de-estruturas-tuplas-listas-e-dicionários)
      - [5. Análise de Dados com Dicionários](#5-análise-de-dados-com-dicionários)
      - [6. Bonus: Agrupamento de Dados](#6-bonus-agrupamento-de-dados)
  - [Exercícios voltados à Engenharia de Dados](#exercícios-voltados-à-engenharia-de-dados)
      - [1: Leitura e Escrita de Arquivos CSV](#1-leitura-e-escrita-de-arquivos-csv)
      - [2: Modularização de Funções](#2-modularização-de-funções)
      - [3: Conexão com Banco de Dados SQL](#3-conexão-com-banco-de-dados-sql)
      - [4. Manipulação de Dados com Pandas](#4-manipulação-de-dados-com-pandas)
      - [5: Criação de APIs Simples](#5-criação-de-apis-simples)
      - [6: Logs e Depuração](#6-logs-e-depuração)
      - [7: Agendamento de Tarefas](#7-agendamento-de-tarefas)
      - [8: Processamento de Dados JSON](#8-processamento-de-dados-json)
      - [9: Expressões Regulares](#9-expressões-regulares)
      - [10: Paralelismo e Multithreading](#10-paralelismo-e-multithreading)
      - [11: Tratamento de Exceções Personalizadas](#11-tratamento-de-exceções-personalizadas)
      - [12: Interação com Serviços em Nuvem (AWS S3)](#12-interação-com-serviços-em-nuvem-aws-s3)
      - [13: Uso de Variáveis de Ambiente](#13-uso-de-variáveis-de-ambiente)
      - [14: Leitura de Dados de um Web Service SOAP](#14-leitura-de-dados-de-um-web-service-soap)
      - [15: Envio de Emails Automatizados](#15-envio-de-emails-automatizados)
      - [16: Compressão e Descompressão de Arquivos](#16-compressão-e-descompressão-de-arquivos)
      - [17: Manipulação de Datas e Horas](#17-manipulação-de-datas-e-horas)
      - [18: Criação de Gráficos Simples](#18-criação-de-gráficos-simples)
      - [19: Scraping de Dados da Web](#19-scraping-de-dados-da-web)
      - [20: Configuração por Arquivo INI](#20-configuração-por-arquivo-ini)
## Exercícios de Tuplas, Listas e Dicionários

#### 1. Manipulação de Tuplas
As tuplas são estruturas de dados imutáveis em Python, o que significa que seus elementos não podem ser alterados depois de criados. Contudo, elas podem ser utilizadas para armazenar dados que não precisam ser modificados ao longo do tempo.

- **Exercício 1.1:** Dada a seguinte tupla:

  ```python
  dados_sensor = (23.4, 25.1, 22.9, 24.5, 23.8, 26.3)
  ```

  a) Calcule a temperatura média.
  
  b) Verifique se a temperatura 24.5 está na tupla.
  
  c) Encontre o maior e o menor valor na tupla.

- **Exercício 1.2:** Crie uma função chamada `tupla_para_lista` que converta uma tupla de dados numéricos em uma lista, permitindo a manipulação posterior.

#### 2. Manipulação de Listas
As listas são coleções mutáveis, o que permite modificar, adicionar ou remover elementos.

- **Exercício 2.1:** Dada a lista de números abaixo, execute as seguintes tarefas:

  ```python
  lista_numeros = [12, 15, 7, 19, 23, 5, 8, 11]
  ```

  a) Ordene a lista em ordem crescente e decrescente.

  b) Encontre os três maiores números da lista.

  c) Filtre a lista para manter apenas números maiores que 10.

  d) Adicione o número 17 à lista e depois remova o número 5.

- **Exercício 2.2:** Crie uma função chamada `multiplica_lista` que receba uma lista de números e um valor escalar, e retorne uma nova lista com cada elemento multiplicado pelo escalar.

- **Exercício 2.3:** Dada uma lista de listas (cada sublista representa um registro de dados), como abaixo:

  ```python
  dados_alunos = [
      ["Ana", 85, "A"],
      ["Carlos", 72, "B"],
      ["Marina", 90, "A"],
      ["Pedro", 65, "C"]
  ]
  ```

  a) Crie uma função que receba essa lista e retorne uma lista com o nome dos alunos que tiraram nota maior que 80.

  b) Ordene essa lista de registros por nota de forma decrescente.

#### 3. Manipulação de Dicionários
Os dicionários são estruturas que armazenam pares chave-valor, permitindo acessos rápidos e manipulações baseadas nas chaves.

- **Exercício 3.1:** Dado o dicionário de produtos e preços:

  ```python
  produtos = {
      "Arroz": 5.99,
      "Feijão": 8.49,
      "Macarrão": 4.29,
      "Azeite": 19.90,
      "Sal": 2.50
  }
  ```

  a) Adicione o produto "Açúcar" com o preço 3.60.

  b) Atualize o preço do "Arroz" para 6.29.

  c) Verifique se o produto "Macarrão" está no dicionário e exiba seu preço.

  d) Crie uma função que receba esse dicionário e retorne a soma total dos preços dos produtos.

- **Exercício 3.2:** Usando o dicionário de alunos e notas abaixo:

  ```python
  notas_alunos = {
      "Ana": 85,
      "Carlos": 72,
      "Marina": 90,
      "Pedro": 65,
      "Lucas": 88
  }
  ```

  a) Crie uma função que receba o dicionário e retorne uma lista com os nomes dos alunos que tiraram nota maior que 80.

  b) Crie uma função que ordene o dicionário por notas de forma decrescente.

#### 4. Integração de Estruturas (Tuplas, Listas e Dicionários)
Agora, vamos trabalhar com um problema mais complexo, integrando as três estruturas de dados.

- **Exercício 4.1:** Dado um dataset representado por uma lista de tuplas, onde cada tupla contém informações de um produto:

  ```python
  dados_produtos = [
      ("Arroz", "Cereais", 5.99),
      ("Feijão", "Leguminosas", 8.49),
      ("Macarrão", "Massas", 4.29),
      ("Azeite", "Óleos", 19.90),
      ("Sal", "Condimentos", 2.50)
  ]
  ```

  a) Crie uma função que receba essa lista de tuplas e retorne um dicionário onde a chave é a categoria do produto e o valor é uma lista com o nome dos produtos daquela categoria.

  b) Modifique a função para que ela também calcule o preço médio de cada categoria.

#### 5. Análise de Dados com Dicionários
- **Exercício 5.1:** Dado o seguinte dicionário representando o número de vendas de diferentes produtos em uma loja:

  ```python
  vendas_produtos = {
      "Arroz": [50, 60, 55, 70],
      "Feijão": [30, 40, 35, 50],
      "Macarrão": [20, 25, 22, 30],
      "Azeite": [5, 8, 6, 7],
      "Sal": [100, 95, 110, 105]
  }
  ```

  a) Crie uma função que calcule o total de vendas de cada produto.

  b) Crie uma função que identifique o produto com o maior número total de vendas.

#### 6. Bonus: Agrupamento de Dados
- **Exercício 6.1:** Crie um dicionário de dados representando funcionários de uma empresa, onde a chave é o nome do funcionário e o valor é uma tupla contendo o departamento e o salário.

  ```python
  funcionarios = {
      "João": ("TI", 4500),
      "Ana": ("Financeiro", 6000),
      "Carlos": ("TI", 4700),
      "Marina": ("Recursos Humanos", 5200),
      "Pedro": ("Financeiro", 6200),
      "Lucas": ("TI", 4800)
  }
  ```

  a) Crie uma função que agrupe os funcionários por departamento e calcule o salário médio de cada departamento.

---

## Exercícios voltados à Engenharia de Dados

#### 1: Leitura e Escrita de Arquivos CSV

**Contexto:**

Como engenheiro de dados, você frequentemente precisa manipular arquivos CSV para realizar ETL (Extract, Transform, Load).

**Tarefa:**

- Escreva um script em Python que leia um arquivo CSV chamado `dados_usuarios.csv`, que contém informações de usuários (ID, nome, email).
- Filtre os usuários que têm emails que terminam com `@empresa.com`.
- Escreva os dados filtrados em um novo arquivo CSV chamado `usuarios_filtrados.csv`.

**Estrutura de Pastas:**

```
projeto_etl/
├── main.py
└── dados/
    ├── dados_usuarios.csv
    └── usuarios_filtrados.csv
```

**Instruções:**

- Coloque seu script principal em `main.py`.
- Utilize o módulo `csv` do Python.
- Não se esqueça de tratar possíveis exceções, como arquivos não encontrados.

---

#### 2: Modularização de Funções

**Contexto:**

Para manter seu código organizado e reutilizável, é importante separar funções em módulos.

**Tarefa:**

- Crie um módulo chamado `transformacoes.py` que contenha uma função `normalizar_nomes(nome)` que recebe um nome e retorna ele em letras minúsculas sem espaços extras.
- No `main.py`, leia um arquivo `nomes_raw.txt` que contém um nome por linha.
- Utilize a função `normalizar_nomes` para processar cada nome.
- Escreva os nomes normalizados em um arquivo `nomes_normalizados.txt`.

**Estrutura de Pastas:**

```
projeto_transformacao/
├── main.py
├── transformacoes.py
└── dados/
    ├── nomes_raw.txt
    └── nomes_normalizados.txt
```

**Instruções:**

- Importe a função `normalizar_nomes` no `main.py`.
- Certifique-se de que o módulo `transformacoes.py` está no mesmo diretório que `main.py`.

---

#### 3: Conexão com Banco de Dados SQL

**Contexto:**

Engenheiros de dados frequentemente interagem com bancos de dados para extrair e carregar dados.

**Tarefa:**

- Escreva um script que se conecte a um banco de dados SQLite chamado `empresa.db`.
- Crie uma tabela `funcionarios` com colunas `id`, `nome`, `departamento`.
- Insira pelo menos cinco registros na tabela.
- Faça uma consulta que selecione todos os funcionários do departamento de 'Vendas'.

**Estrutura de Pastas:**

```
projeto_banco_dados/
├── main.py
└── empresa.db
```

**Instruções:**

- Utilize o módulo `sqlite3` do Python.
- Coloque todas as funções de conexão e operações com o banco de dados em um módulo separado chamado `db_operations.py`.

---

#### 4. Manipulação de Dados com Pandas

**Contexto:**

Pandas é uma biblioteca essencial para manipulação de dados em Python.

**Tarefa:**

- Leia um arquivo Excel `vendas.xlsx` que contém dados de vendas mensais.
- Calcule o total de vendas por produto.
- Gere um arquivo CSV `total_vendas_por_produto.csv` com os resultados.

**Estrutura de Pastas:**

```
projeto_pandas/
├── main.py
└── dados/
    ├── vendas.xlsx
    └── total_vendas_por_produto.csv
```

**Instruções:**

- Utilize a biblioteca Pandas (`import pandas as pd`).
- Certifique-se de instalar as dependências necessárias (`pip install pandas`).
- Trate dados faltantes (valores nulos) antes de realizar os cálculos.

---

#### 5: Criação de APIs Simples

**Contexto:**

APIs permitem que diferentes sistemas se comuniquem, e às vezes você precisa consumir dados de uma API.

**Tarefa:**

- Crie um script que faça uma requisição GET para a API pública `https://api.coindesk.com/v1/bpi/currentprice/BTC.json`.
- Extraia o preço atual do Bitcoin em dólares americanos.
- Salve o preço em um arquivo `preco_bitcoin.txt` com a data e hora da consulta.

**Estrutura de Pastas:**

```
projeto_api/
├── main.py
└── preco_bitcoin.txt
```

**Instruções:**

- Utilize o módulo `requests` (`pip install requests`).
- Trate possíveis exceções de conexão e requisição.

---

#### 6: Logs e Depuração

**Contexto:**

Registrar logs é crucial para monitorar aplicações e depurar problemas.

**Tarefa:**

- Modifique o script do Exercício 5 para incluir logs que registrem:
  - Quando a requisição à API é iniciada.
  - Se a requisição foi bem-sucedida ou não.
  - Qualquer erro que ocorra durante o processo.
- Os logs devem ser salvos em um arquivo `app.log`.

**Estrutura de Pastas:**

```
projeto_api_logging/
├── main.py
├── app.log
└── preco_bitcoin.txt
```

**Instruções:**

- Utilize o módulo `logging` do Python.
- Configure o logger para incluir timestamp e nível de severidade.

---

#### 7: Agendamento de Tarefas

**Contexto:**

Automatizar tarefas recorrentes é uma atividade comum.

**Tarefa:**

- Crie um script que execute uma determinada função a cada minuto por cinco minutos.
- A função deve escrever a hora atual em um arquivo `horarios.txt`.

**Estrutura de Pastas:**

```
projeto_agendamento/
├── main.py
└── horarios.txt
```

**Instruções:**

- Utilize o módulo `time` ou bibliotecas como `schedule` (`pip install schedule`).
- Certifique-se de que o script termina após cinco minutos.

---

#### 8: Processamento de Dados JSON

**Contexto:**

JSON é um formato de dados muito utilizado em APIs e armazenamento de configurações.

**Tarefa:**

- Leia um arquivo `config.json` que contém configurações para uma aplicação (por exemplo, parâmetros de conexão, caminhos de arquivos).
- Extraia as informações necessárias e imprima-as no console.

**Estrutura de Pastas:**

```
projeto_json/
├── main.py
└── config.json
```

**Instruções:**

- Utilize o módulo `json` do Python.
- Trate exceções caso o arquivo não esteja no formato correto.

---

#### 9: Expressões Regulares

**Contexto:**

Expressões regulares são úteis para validar e extrair padrões em textos.

**Tarefa:**

- Escreva um script que valide uma lista de endereços de email contidos no arquivo `emails.txt`.
- Utilize expressões regulares para verificar se os emails estão em um formato válido.
- Escreva os emails válidos em um arquivo `emails_validos.txt`.

**Estrutura de Pastas:**

```
projeto_regex/
├── main.py
├── emails.txt
└── emails_validos.txt
```

**Instruções:**

- Utilize o módulo `re` do Python.
- Considere emails no formato simples, como `usuario@dominio.com`.

---

#### 10: Paralelismo e Multithreading

**Contexto:**

Melhorar a performance de scripts é essencial quando lidamos com grandes volumes de dados.

**Tarefa:**

- Crie um script que faça download de imagens a partir de URLs listadas em `imagens.txt`.
- Utilize multithreading para baixar várias imagens simultaneamente.
- Salve as imagens na pasta `downloads/`.

**Estrutura de Pastas:**

```
projeto_multithreading/
├── main.py
├── imagens.txt
└── downloads/
    ├── imagem1.jpg
    ├── imagem2.jpg
    └── ...
```

**Instruções:**

- Utilize o módulo `threading` ou `concurrent.futures`.
- Trate exceções para casos em que o download falhe.

---

#### 11: Tratamento de Exceções Personalizadas

**Contexto:**

Criar exceções personalizadas ajuda a identificar erros específicos na aplicação.

**Tarefa:**

- Crie uma exceção personalizada chamada `ErroDeConexao`.
- Modifique o script de conexão com o banco de dados (Exercício 3) para lançar `ErroDeConexao` quando não for possível conectar ao banco de dados.
- Capture essa exceção e registre um log apropriado.

**Estrutura de Pastas:**

```
projeto_excecoes/
├── main.py
├── db_operations.py
└── logs/
    └── erro.log
```

**Instruções:**

- Defina a classe `ErroDeConexao` herdando de `Exception`.
- Utilize blocos `try`, `except` para capturar e tratar a exceção.

---

#### 12: Interação com Serviços em Nuvem (AWS S3)

**Contexto:**

Engenheiros de dados frequentemente interagem com serviços em nuvem.

**Tarefa:**

- Escreva um script que faça upload de um arquivo `dados.csv` para um bucket S3 na AWS.
- Liste todos os arquivos presentes no bucket após o upload.

**Estrutura de Pastas:**

```
projeto_aws_s3/
├── main.py
└── dados.csv
```

**Instruções:**

- Utilize a biblioteca `boto3` (`pip install boto3`).
- Certifique-se de configurar suas credenciais AWS corretamente (pode usar um perfil de configuração).

---

#### 13: Uso de Variáveis de Ambiente

**Contexto:**

Para manter informações sensíveis seguras, é comum usar variáveis de ambiente.

**Tarefa:**

- Modifique o script do Exercício 12 para que as credenciais AWS sejam lidas de variáveis de ambiente.
- Utilize o módulo `os` para acessar as variáveis de ambiente.

**Estrutura de Pastas:**

```
projeto_aws_s3_env/
├── main.py
└── dados.csv
```

**Instruções:**

- As variáveis de ambiente podem ser `AWS_ACCESS_KEY_ID` e `AWS_SECRET_ACCESS_KEY`.
- Documente no `README.md` como configurar as variáveis de ambiente.

---

#### 14: Leitura de Dados de um Web Service SOAP

**Contexto:**

Embora REST seja mais comum hoje, alguns serviços ainda utilizam SOAP.

**Tarefa:**

- Escreva um script que consuma um Web Service SOAP para obter a cotação atual do dólar.
- Exiba a cotação no console.

**Estrutura de Pastas:**

```
projeto_soap/
└── main.py
```

**Instruções:**

- Utilize a biblioteca `zeep` (`pip install zeep`).
- Utilize um serviço público que forneça cotações via SOAP.

---

#### 15: Envio de Emails Automatizados

**Contexto:**

Enviar notificações por email é uma tarefa comum para alertas e relatórios.

**Tarefa:**

- Escreva um script que envie um email para um endereço especificado.
- O email deve conter um relatório em anexo (`relatorio.pdf`).

**Estrutura de Pastas:**

```
projeto_email/
├── main.py
└── relatorio.pdf
```

**Instruções:**

- Utilize o módulo `smtplib` e `email`.
- Para testes, você pode usar o servidor SMTP de teste `smtp.gmail.com`.

---

#### 16: Compressão e Descompressão de Arquivos

**Contexto:**

Manipular arquivos comprimidos é útil para economizar espaço e facilitar transferências.

**Tarefa:**

- Escreva um script que comprima todos os arquivos `.log` de uma pasta em um arquivo `logs.zip`.
- Depois, escreva uma função que descomprime `logs.zip` em uma pasta `logs_descomprimidos/`.

**Estrutura de Pastas:**

```
projeto_compactacao/
├── main.py
├── logs/
│   ├── log1.log
│   ├── log2.log
│   └── ...
└── logs_descomprimidos/
```

**Instruções:**

- Utilize o módulo `zipfile` do Python.
- Certifique-se de que a compressão e descompressão mantenham a integridade dos arquivos.

---

#### 17: Manipulação de Datas e Horas

**Contexto:**

Trabalhar com datas e horas é comum em logs e agendamento de tarefas.

**Tarefa:**

- Escreva um script que calcule a diferença em dias entre duas datas fornecidas pelo usuário.
- Formate a data atual em diferentes formatos e exiba no console.

**Estrutura de Pastas:**

```
projeto_datas/
└── main.py
```

**Instruções:**

- Utilize o módulo `datetime` do Python.
- Trate entradas inválidas do usuário.

---

#### 18: Criação de Gráficos Simples

**Contexto:**

Visualização de dados é importante para análise.

**Tarefa:**

- Leia dados de um arquivo `dados.csv` e crie um gráfico de linha mostrando a evolução de um valor ao longo do tempo.
- Salve o gráfico em um arquivo `grafico.png`.

**Estrutura de Pastas:**

```
projeto_graficos/
├── main.py
├── dados.csv
└── grafico.png
```

**Instruções:**

- Utilize a biblioteca `matplotlib` (`pip install matplotlib`).
- Certifique-se de que os dados estão corretamente formatados para a criação do gráfico.

---

#### 19: Scraping de Dados da Web

**Contexto:**

Extrair dados de sites pode ser necessário quando não há uma API disponível.

**Tarefa:**

- Escreva um script que acesse uma página web e extraia todos os links presentes.
- Salve os links em um arquivo `links.txt`.

**Estrutura de Pastas:**

```
projeto_scraping/
├── main.py
└── links.txt
```

**Instruções:**

- Utilize `requests` para fazer a requisição e `BeautifulSoup` (`pip install beautifulsoup4`) para parsear o HTML.
- Respeite as políticas de scraping do site (considere fazer requests gentis e verificar o arquivo `robots.txt` se necessário).

---

#### 20: Configuração por Arquivo INI

**Contexto:**

Arquivos de configuração permitem que parâmetros sejam alterados sem modificar o código.

**Tarefa:**

- Crie um arquivo de configuração `config.ini` que contenha parâmetros como nome do banco de dados, usuário e senha.
- Modifique o script de conexão com o banco de dados para ler esses parâmetros do arquivo de configuração.

**Estrutura de Pastas:**

```
projeto_config/
├── main.py
├── config.ini
└── db_operations.py
```

**Instruções:**

- Utilize o módulo `configparser` do Python.
- Documente como o arquivo `config.ini` deve ser estruturado.

