# napoleon-test
Тестовое задание на стажировку в Napoleon IT.

## Развертывание
Для запуска необходимо установить Docker и docker-compose.
В каталоге проекта необходимо создать файл `.env` со следующим содержанием:

```
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=password
DATABASE_HOST=db
DATABASE_PORT=5432
DATABASE_NAME=postgres
```

Затем из командной строки в каталоге приложения выполнить команду:

```
$ docker-compose up
```

После этого приложение будет доступно по адресу [http://localhost:80/](http://localhost:80/).
