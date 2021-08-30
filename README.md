```bash
# Запуск tron fullnode и тестового приложения (делает вывод и завершается с кодом 0).
# При необходимости преесобирает нужные images.
docker-compose up
```

```bash
# Повторный запуск тестового приложения (хорошо подходит для быстрых правок скрипта).
docker-compose run client
```

```bash
# Запуск консоли внутри контейнера fullnode
docker-compose exec fullnode bash
```

```bash
# Просмотр отладочных логов fullnode
docker-compose exec fullnode less logs/tron.log
```

```bash
# Запуск контейнеров по отдельности
docker-compose up -d fullnode
docker-compose run client
```