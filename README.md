# API de Gerenciamento de Tarefas

Esta API fornece um sistema de gerenciamento de tarefas, permitindo a criação, listagem, atualização e exclusão de tarefas.

## Tecnologias Utilizadas

- Django Rest Framework (DRF)
- Python
- Banco de dados relacional

## Instalação e Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

5. Execute o servidor:
   ```bash
   python manage.py runserver
   ```

## Endpoints

### 1. Listar Tarefas
- **Endpoint:** `/tasks/`
- **Método:** `GET`
- **Resposta:**
  ```json
  [
    {
      "id": 1,
      "titulo": "Exemplo de Tarefa",
      "descricao": "Descrição da tarefa",
      "status": "P",
      "data_criacao": "2024-03-30T12:00:00Z",
      "data_atualizacao": "2024-03-30T12:00:00Z",
      "data_conclusao": null
    }
  ]
  ```

### 2. Criar Tarefa
- **Endpoint:** `/tasks/`
- **Método:** `POST`
- **Corpo da Requisição:**
  ```json
  {
    "titulo": "Nova Tarefa",
    "descricao": "Detalhes da nova tarefa",
    "status": "P"
  }
  ```
- **Resposta:**
  ```json
  {
    "id": 2,
    "titulo": "Nova Tarefa",
    "descricao": "Detalhes da nova tarefa",
    "status": "P",
    "data_criacao": "2024-03-30T12:10:00Z",
    "data_atualizacao": "2024-03-30T12:10:00Z",
    "data_conclusao": null
  }
  ```

### 3. Detalhar Tarefa
- **Endpoint:** `/tasks/{id}/`
- **Método:** `GET`
- **Exemplo de Resposta:**
  ```json
  {
    "id": 1,
    "titulo": "Exemplo de Tarefa",
    "descricao": "Descrição da tarefa",
    "status": "P",
    "data_criacao": "2024-03-30T12:00:00Z",
    "data_atualizacao": "2024-03-30T12:00:00Z",
    "data_conclusao": null
  }
  ```

### 4. Atualizar Tarefa
- **Endpoint:** `/tasks/{id}/`
- **Método:** `PUT`
- **Corpo da Requisição:**
  ```json
  {
    "titulo": "Tarefa Atualizada",
    "descricao": "Nova descrição",
    "status": "E"
  }
  ```
- **Nota:** Se o status for alterado para `C` (Concluída), a `data_conclusao` será preenchida automaticamente.

### 5. Excluir Tarefa
- **Endpoint:** `/tasks/{id}/`
- **Método:** `DELETE`
- **Resposta:** `204 No Content`

## Estrutura do Projeto

```
.
├── manage.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── tasks/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
```

## Considerações Finais

Esta API permite um gerenciamento eficiente de tarefas, oferecendo operações CRUD completas. Se tiver dúvidas ou sugestões, contribua com o projeto!

