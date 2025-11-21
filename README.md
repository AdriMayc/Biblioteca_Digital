#  🔷 Biblioteca Digital

Este repositório contém um sistema completo de gerenciamento de biblioteca, que possibilita o cadastro de livros e usuários, o registro de empréstimos e devoluções, além da geração de relatórios detalhados. Tudo isso é feito por meio de estruturas de dados eficientes, modularização e interface gráfica utilizando Tkinter.

Condições estabelecidas para a realização do projeto:

- Uso de múltiplas estruturas de dados
- Modularização completa
- Código eficiente e comentado
- Relatórios e documentação
- Aplicação prática no contexto de Ciência de Dados

Imagens prévias do projeto:
> - [Biblioteca Digital](00-biblioteca.md)

##  🔶 Documentação por Módulo
Cada arquivo contém um conjunto de responsabilidades:
 
1. [livros.py](01-livros.md)
2. [usuarios.py](02-usuarios.md)
3. [emprestimos.py](03-emprestimos.md)
4. [relatorios.py](04-relatorios.md)
5. [gerenciador.py](05-gerenciador.md)
6. [console.py](06-console.md)
7. [helpers.py](07-helpers.md)
8. [main.py](08-main.md)

##  🔶 Estruturas Utilizadas


- Lista ``(list)``
> Usada para armazenar coleções de livros, usuários e histórico.

- Dicionário ``(dict)``
> Utilizado para representar entidades como:

``{"id": 1, "titulo": "1984", "autor": "George Orwell", "disponivel": True}``

Justificativa:

- A busca por atributos é rápida e sem necessidade de modelagem complexa.
- Listas mantêm ordem e permitem iterações eficientes.
- Para o tamanho do projeto, são as estruturas mais adequadas e simples de manter.

> Todos os critérios sobre estruturas de dados são atendidos.

##  🔶 Organização do Código

A arquitetura segue o padrão modular:

```` 
BIBLIOTECA_DIGITAL/
│
├── data/
│   ├── emprestimos.json
│   ├── livros.json
│   └── usuarios.json
│
├── readmes/
│
├── src/
│   ├── componentes/
│   │   ├── console.py
│   │   ├── emprestimos.py
│   │   ├── gerenciador.py
│   │   ├── livros.py
│   │   ├── relatorios.py
│   │   └── usuarios.py
│   │
│   ├── styles/
│   │   └── colors.py
│   │
│   ├── utils/
│   │   └── helpers.py
│   │
│   |── views/
│   |    ├── base_view.py
│   |    ├── emprestimos_view.py
│   |    ├── livros_view.py    
│   |    ├── relatorios_view.py
│   |    └── usuarios_view.py
│   └── main.py
|
├── venv/
├── .gitignore
├── README.md
└── requirements.txt

````

Cada módulo contém apenas suas responsabilidades, melhorando:

- Reutilização
- Clareza
- Manutenção
- Testabilidade

##  🔶 Complexidade e Eficiência

As operações principais são:

| Operação             | Módulo         | Estrutura    | Complexidade |
| -------------------- | -------------- | ------------ | ------------ |
| Buscar livro por ID  | livros.py      | lista        | **O(n)**     |
| Buscar usuário       | usuarios.py    | lista        | **O(n)**     |
| Registrar empréstimo | emprestimos.py | lista + dict | **O(n)**     |
| Listar livros        | livros.py      | lista        | **O(n)**     |
| Gerar relatórios     | relatorios.py  | lista        | **O(n)**     |

> Para o escopo do trabalho (pequeno volume de dados), O(n) é aceitável e totalmente eficiente.
 

##  🔶 Motivação

Imagine uma biblioteca universitária em crescimento, ou até mesmo um pequeno acervo pessoal que se tornou público. Com o aumento do número de livros e usuários, surgem problemas comuns:

- 📚 **Controle manual complicado**: livros sendo emprestados e devolvidos sem registro centralizado, o que gera confusão sobre disponibilidade e histórico de uso.
- ⏳ **Perda de tempo**: funcionários ou usuários precisam consultar planilhas ou cadernos físicos para verificar se o livro está disponível.
- ❌ **Erros frequentes**: livros duplicados, informações inconsistentes sobre autores ou datas de devolução, dificultando relatórios e tomadas de decisão.
- 📊 **Dificuldade em análise**: sem um registro estruturado, não é possível gerar relatórios rápidos sobre livros disponíveis, empréstimos ativos e histórico de movimentações.

O **Sistema Biblioteca Digital** surge para resolver essas questões de forma clara e eficiente:

- Centraliza todas as informações em estruturas de dados simples, mas poderosas (listas e dicionários).
- Permite cadastrar livros e usuários rapidamente, registrar empréstimos e devoluções, sem precisar do terminal.
- Gera relatórios completos e confiáveis, permitindo visualizar o acervo disponível, os livros emprestados e o histórico detalhado de movimentações.
- Cria um fluxo organizado, que evita erros e melhora a experiência de quem gerencia ou utiliza a biblioteca.

> Em resumo, este sistema transforma uma gestão manual e propensa a erros em um processo automatizado, eficiente e fácil de usar, garantindo confiabilidade e praticidade para bibliotecas de qualquer tamanho.

##  🔶 Relatório Final

O relatório completo com explicações técnicas, justificativas e análise de desempenho encontra-se em:

> [Relatório do Projeto](relatorio.md)

## 🔷 Encerramento

A Biblioteca Digital ilustra como um sistema bem organizado pode tornar a gestão de um acervo um processo eficaz, seguro e de fácil compreensão.  Com o uso estratégico de listas e dicionários, é possível centralizar dados sobre livros, usuários e movimentações, o que possibilita a geração de relatórios detalhados e o controle total sem a necessidade de processos manuais.
 
 Além de atender aos critérios técnicos de estruturas de dados, modularização e eficiência, este projeto oferece uma interface amigável que simplifica a interação do usuário e proporciona uma experiência completa de gerenciamento.

A execução deste sistema é resultado do trabalho colaborativo de:

🔹**Adriano Mayco** – Desenvolveu a estrutura principal do projeto, integrou e modularizou os módulos, criou a interface visual em Tkinter, supervisionou as branches no GitHub e revisou a documentação.

🔹**Alex Mender** - Desenvolvimento de funções específicas, com ênfase na criação de empréstimos e elaboração de relatórios.

🔹**João Vitor Domingue** - Desenvolvimento de funções associadas a usuários e livros, assegurando que o registro, a listagem e a manipulação de dados fossem precisos.

Agradecemos por dedicar seu tempo para conhecer este projeto. Esperamos que a leitura tenha sido clara e que o sistema demonstre boas práticas de desenvolvimento, organização de código e design de interfaces. Seu interesse é muito importante para nós!

<hr style="height:2px; background-color:#807f7e; border:none;">

