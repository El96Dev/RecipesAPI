# Описание
RecipesAPI — это RESTful API для создания, хранения и управления кулинарными рецептами. Проект предоставляет возможность пользователям добавлять рецепты, 
искать их по категориям, а также делиться своими кулинарными идеями.
# Инструкция по запуску
Для запуска приложения необходимо установить Docker. Далее в папке с проектом откройте терминал и введите команды 
```
docker compose -f docker-compose.yml build
docker compose -f docker-compose.yml up
```
После успешного запуска проекта документация swagger будет доступна по адресу http://0.0.0.0:8000/docs#/
# Тесты
Для запуска тестов в папке с проектом необходимо ввести в терминал команды
```
docker compose -f docker-compose.test.yml build
docker compose -f docker-compose.test.yml up
```
