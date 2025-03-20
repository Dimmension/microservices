# Лабораторная работа №1

REST API сервер

Балансировщик нагрузки

Упаковка приложения в Docker-контейнер

Запуск проекта в Docker Compose

### **Пример тестовых запросов**

#### Для `Contact`:
- Создание:
  ```bash
  curl -X POST http://localhost:6080/api/v1/contact \
  -H "Content-Type: application/json" \
  -d '{"ID": 1, "Username": "test"}'
  ```

- Получение:
  ```bash
  curl -X GET http://localhost:6080/api/v1/contact/1
  ```

- Обновление:
  ```bash
  curl -X PUT http://localhost:6080/api/v1/contact/1 \
  -H "Content-Type: application/json" \
  -d '{"ID": 1, "Username": "updated"}'
  ```

- Удаление:
  ```bash
  curl -X DELETE http://localhost:6080/api/v1/contact/1
  ```

#### Для `Group`:
- Создание:
  ```bash
  curl -X POST http://localhost:6080/api/v1/group \
  -H "Content-Type: application/json" \
  -d '{"ID": 1, "Title": "Test Group"}'
  ```

- Получение:
  ```bash
  curl -X GET http://localhost:6080/api/v1/group/1
  ```

- Обновление:
  ```bash
  curl -X PUT http://localhost:6080/api/v1/group/1 \
  -H "Content-Type: application/json" \
  -d '{"ID": 1, "Title": "Updated Group"}'
  ```

- Удаление:
  ```bash
  curl -X DELETE http://localhost:6080/api/v1/group/1
  ```
