### Todo-list simples (pelo fato de ser simples)
Este é um projeto desenvolvido com python 3.12 utilizando FastAPI e PostgreSQL.
E tentando copiar a arquitetura nativa do NestJS pelo qual acho muito limpa e organizada.
Sim, tenho preferência por arquitetura monolítica e modular.

#### Requisitos
Antes de rodar o projeto, você ter instalado:
- [Python](https://www.python.org/downloads/) (claro)
- [PostgreSQL](https://www.postgresql.org/download/) (Mas se quiser usar outro banco, tudo bem, o chatGPT pode ajudar a configurar, escolhi o postgres, pelo fato de gostar mais dele)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), não obrigatório, mas é recomendado para o versionamento

#### Como baixar este bendito projeto
0 - Vá até o diretório da sua máquina onde você deseja baixar o projeto (de preferência no cmd)

1 - Clone o repositório para sua máquina local com o código:
    ```git clone https://github.com/p3dru/template_fastapi_todo.git

2 - Acesse a pasta template_fastapi_todo onde você salvou

3 - Abra a pasta no seu editor de código

4 - Instalar as dependências:
    4.1 - Se estiver no windows:
        4.1.1 - Crie um ambiente virtual via cmd (isola o ambiente e evita conflitos entre outros ambientes):
        ```python -m venv [nome_do_seu_ambiente]
        4.1.2 - Ative o ambiente:
        ```[nome_do_ambiente]/Scripts/activate
        4.1.3 - Para desativar:
        ```[nome_do_ambiente]/Scripts/deactivate

    4.2 - Se estiver no Linux/Mac:
        4.1.1 - Crie um ambiente virtual via cmd (isola o ambiente e evita conflitos entre outros ambientes):
        ```python3 -m venv 
        [nome_do_seu_ambiente]
        4.1.2 - Ative o ambiente:
        ```source [nome_do_ambiente]/bin/activate
        4.1.3 - Para desativar:
        ```source [nome_do_ambiente]/bin/deactivate

    4.3 - Instale as bibliotecas e dependências do projeto:
        ```pip install -r requirements.txt

        Aqui, instala todas as dependências de uma vez, sem precisar instalar manualmente de um por um.

5 - Feito tudo isso, agora é só rodar o projeto:
    ```uvicorn app.main:app -reload

Feito isso, tudo deve rodar perfeitamente em http://localhost:8000/.
Para ver todos os endpoints e para realizar testes manuais, basta acessar http://localhost:8000/docs para visualizar o Swagger. 
Se quiser rodar em outra porta que não seja a 8000, use: 
    ```uvicorn main:app --reload --port [numero_da_porta]

Caso tenha alguma coisa errada, foi mal, me manda uma mensagem no [Linkedin](https://www.linkedin.com/in/p3dru/).

#### Testando a aplicação
Na raiz do projeto, no seu cmd (ou no seu editor), digite: 
    ```pytest
E daí os testes serão rodados tranquilamente.

#### Licença
Pode passar. Esse negócio é livre.
Faça o que quiser com esse código.

#### Explicação de arquivos e suas funções:
##### main.py
É o ponto de entrada da aplicação. É responsável por iniciar o FastAPI, configurar os middlewares e incluir os routers da aplicação.

##### database.py
Gerencia a conexão com o banco de dados. Aqui é onde a engine do SQLAlchemy é configurada e a sessão do banco de dados é criada.

##### models.py
Define os modelos de dados da aplicação, geralmente usando SQLAlchemy para mapear tabelas no banco de dados.

##### controllers.py
Pode ser usado para definir a lógica de negócios, separando da camada de roteamento. Algumas pessoas combinam controllers e services.

##### routers.py
Define os endpoints da API (rotas). Cada recurso tem um arquivo próprio.

##### schemas.py
Define os esquemas (schemas) de entrada e saída de dados com Pydantic.

##### dependencies.py
Armazena algumas funções de dependências utilizadas nesse projeto, como se fosse um arquivo utils.

##### services.py
Define serviços auxiliares, como hashing de senha, CRUD/manipulação de elementos.

##### __init__.py
Esse arquivo pode estar presente em cada pasta (modules, routers, etc.) e serve para indicar que a pasta deve ser tratada como um módulo Python.