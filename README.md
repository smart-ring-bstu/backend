# Smart Ring — Backend

Бэкенд-сервис проекта Smart Ring (учебный проект БГТУ).

**Стек:** Java 21, Spring Boot, Maven, Docker.

В проекте два способа запуска:

- **Локальная разработка**: для повседневной работы, запуск из IntelliJ IDEA.
- **Запуск через Docker**: так приложение работает на сервере.

---

## Локальная разработка (первый запуск)

### Шаг 1. Установите IntelliJ IDEA

https://www.jetbrains.com/idea/download

### Шаг 2. Склонируйте репозиторий и откройте его в IDEA

```bash
git clone https://github.com/smart-ring-bstu/backend.git
```

В IDEA: **File → Open**, выберите папку `backend`. Зависимости Maven подтянутся автоматически.

### Шаг 3. Выберите JDK 21

**File → Project Structure → Project → SDK**: Java 21. Если его нет в списке, нажмите **Add SDK → Download JDK**.

### Шаг 4. Запустите приложение

Откройте класс `SmartRingApplication` и запустите его (зелёный треугольник).

Ожидаемый результат: в окне **Run** появилась строка вида:

```
Started SmartRingApplication in 1.3 seconds
```

### Шаг 5. Проверьте результат

Откройте в браузере http://localhost:8080/actuator/health

Ожидаемый результат:

```json
{"groups":["liveness","readiness"],"status":"UP"}
```

---

## Запуск через Docker (как на сервере)

Команды выполняются в корне репозитория, там, где лежит `Dockerfile`. Их можно вводить в терминале IDEA (вкладка **Terminal**).

### Шаг 1. Установите Docker и проверьте установку

Docker Desktop: https://www.docker.com/products/docker-desktop/

```bash
docker --version
```

Ожидаемый результат: версия Docker.

```
Docker version 28.0.1, build 068a01e
```

### Шаг 2. Соберите образ

```bash
docker build -t backend:local .
```

Первая сборка занимает около 3 минут: скачиваются базовые образы и зависимости Maven.

Ожидаемый результат: сборка завершается без `ERROR`, в конце есть строка:

```
=> => naming to docker.io/library/backend:local
```

### Шаг 3. Запустите контейнер

```bash
docker run --rm -p 8080:8080 backend:local
```

Ожидаемый результат: в терминале логи Spring Boot, среди них строка:

```
Started SmartRingApplication in 1.3 seconds
```

### Шаг 4. Проверьте результат

Откройте в браузере http://localhost:8080/actuator/health

Ожидаемый результат:

```json
{"groups":["liveness","readiness"],"status":"UP"}
```