# Техническое задание Bewise
### Используемые Версии:
```
    Docker: version 24.0.2, build cb74dfc
    Docker-Compose: version v2.21.0
    Python: 3.11.5
```
### Используемые инструменты:
```
    alembic==1.12.0
    asyncpg==0.28.0
    fastapi==0.103.2
    httpx==0.25.0
    uvicorn==0.23.2
    sqlmodel==0.0.8
```

### Инструкция по запуску:
```
    1. Зайдите в корень проекта
    2. Создайте файл .env, пример содержимого снизу.
    3. Выполните следующую команду: sudo docker-compose up --build
    4. Перейдите http://localhost:8000/docs
    
    Чтобы подключиться к postgres DB:
        1. Выполните в корне следующие комманды:
            docker ps
            docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id>
```

### Примеры:
#### .env:
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_SERVER=db
POSTGRES_PORT=5432
POSTGRES_DB=postgres
URL_API=https://jservice.io/api
```