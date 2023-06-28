# School-CRM

## Установка и запуск

Необходимые зависимости: git, docker, docker-compose

Для запуска проекта, нужно склонировать репозиторий, перейти в директорию с файлом docker-compose.yml и в терминале ввести:

```shell
$ docker compose up -d (-d для возможности пользоваться терминалом)
```
Если не вышло 

- System check identified no issues (0 silenced).
- Django version 4.2.2, using settings 'school_proj.settings'
- Starting development server at http://0.0.0.0:8000/
- Quit the server with CONTROL-C.

То 
- ctrl+c
- docker-compose up -d

Перейти по адресу localhost:8000.

## Использование

Для создания суперадмина, нужно ввести в терминал:

```shell
$ docker exec -it <container_id> python manage.py createsuperuser
```

Далее ввести валидные номер телефона и пароль (номера телефонов должны быть корректными и соблюдать международный формат, например +996709128723).

При входе на сайт в верхнем меню учителю можно зарегистрироваться через номер телефона. Далее нужно авторизоваться (кнопка Login) для использвания всего функционала.

На главной странице можно увидеть список всех учеников.
Поиск осуществляется по имени или классу ученика.

---
При создании ученика, ему на почту приходит письмо. Для реализации использовались django signals. Также в профиле у учителя есть возможность сделать рассылку сообщения на все 
электронные письма учеников.

Для учеников доступны все CRUD операции, для классов и школ только CRD (немного не успел).

Также django signals используются для обновления экземпляра класса при изменении этого поля в ученике или учителе. 

Для аутентификации использовались стандартные средства Django.

В файле .env я использовал актуальные данные моей почты и временный пароль. Надеюсь ничего не сломается :D