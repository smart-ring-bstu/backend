# Smart Ring — Backend

Бэкенд-сервис проекта Smart Ring (учебный проект БГТУ).

**Стек:** Java 21, Spring Boot, Maven, Docker.

## Быстрый старт

Нужен только установленный [Docker](https://www.docker.com/products/docker-desktop/). JDK и Maven ставить не нужно.

Собрать образ:

```bash
docker build -t backend:local .
```

> Первая сборка долгая (около 3 минут): скачиваются базовые образы и зависимости Maven. Повторные сборки быстрее благодаря кэшу.

Запустить приложение (будет доступно на http://localhost:8080):

```bash
docker run --rm -p 8080:8080 backend:local
```

Проверка. Не закрывая первый терминал, откройте второй и выполните:

```bash
curl localhost:8080/api/hello
curl localhost:8080/actuator/health
```

Ожидаемый результат: `Hello from backend` и `{"status":"UP", ...}`.

Остановить приложение: `Ctrl+C` в первом терминале.

## Деплой

Деплой на стенд выполняется через Jenkins (настраивается в репозитории `infra`).
Подробности появятся после настройки CI/CD.
