# API de Gerenciamento de Tarefas

Esta API fornece um sistema de gerenciamento de tarefas, permitindo a criação, listagem, atualização e exclusão de tarefas. Agora com autenticação via **JWT** e documentação interativa com **Swagger**.

## Tecnologias Utilizadas

- Django
- Django Rest Framework (DRF)
- JWT (`djangorestframework-simplejwt`)
- Swagger (`drf-yasg`)
- Python
- Banco de dados relacional (SQLite por padrão)

---

## Instalação e Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/DiegoFChaggas/Tasks.git
   cd Tasks
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

5. Crie um superusuário (opcional, mas recomendado):
   ```bash
   python manage.py createsuperuser
   ```

6. Execute o servidor:
   ```bash
   python manage.py runserver
   ```

---

## Autenticação com JWT

A API utiliza JWT para proteger os endpoints. Para obter um token de acesso:

1. Faça uma requisição `POST` para:
   ```
   /api/token/
   ```

   **Body da requisição:**
   ```json
   {
     "username": "seu_usuario",
     "password": "sua_senha"
   }
   ```

2. O retorno conterá os tokens:
   ```json
   {
     "refresh": "token_refresh",
     "access": "token_access"
   }
   ```

3. Para autenticar chamadas protegidas, envie o token no header:
   ```
   Authorization: Bearer seu_token_access
   ```

---

## Swagger UI

Documentação interativa disponível em:

```
/swagger/
```

Você pode autenticar-se diretamente por lá clicando em **Authorize** e fornecendo o token JWT no formato:

```
Bearer SEU_TOKEN
```

---

## Endpoints

### 1. Listar Tarefas (requer autenticação)
- **GET** `/api/v1/tasks/`

### 2. Criar Tarefa (requer autenticação)
- **POST** `/api/v1/tasks/`

### 3. Detalhar Tarefa (requer autenticação)
- **GET** `/api/v1/tasks/{id}/`

### 4. Atualizar Tarefa (requer autenticação)
- **PUT** `/api/v1/tasks/{id}/`

### 5. Excluir Tarefa (requer autenticação)
- **DELETE** `/api/v1/tasks/{id}/`

---

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

---

## Considerações Finais

Esta API agora oferece autenticação segura com JWT e uma interface amigável com Swagger para facilitar testes e integração. Sinta-se à vontade para contribuir ou enviar sugestões!