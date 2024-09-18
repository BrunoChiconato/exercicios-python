### **Exercícios de Tuplas, Listas e Dicionários em Python**

#### **1. Manipulação de Tuplas**
As tuplas são estruturas de dados imutáveis em Python, o que significa que seus elementos não podem ser alterados depois de criados. Contudo, elas podem ser utilizadas para armazenar dados que não precisam ser modificados ao longo do tempo.

- **Exercício 1.1:** Dada a seguinte tupla:

  ```python
  dados_sensor = (23.4, 25.1, 22.9, 24.5, 23.8, 26.3)
  ```

  a) Calcule a temperatura média.
  
  b) Verifique se a temperatura 24.5 está na tupla.
  
  c) Encontre o maior e o menor valor na tupla.

- **Exercício 1.2:** Crie uma função chamada `tupla_para_lista` que converta uma tupla de dados numéricos em uma lista, permitindo a manipulação posterior.

#### **2. Manipulação de Listas**
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

#### **3. Manipulação de Dicionários**
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

#### **4. Integração de Estruturas (Tuplas, Listas e Dicionários)**
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

#### **5. Análise de Dados com Dicionários**
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

#### **6. Bonus: Agrupamento de Dados**
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
