# Qodex
// Обозначения: //
Core - ядро приложения.
Frontend - UI приложения.
Qodex - проект.


// Архитектура: //
Core-
    -admin.py - регистрация моделей
    -urls.py - урлы приложения Core
    -models.py - модели БД
    -serializers.py - сериализеры для формирования API для моделей
    Сериализаторы(!)
    [Модели Django интуитивно представляют данные, хранящиеся в базе, но API должен передавать 
    информацию в менее сложной структуре. Хотя данные будут представлены как экземпляры классов 
    Model, их необходимо перевести в формат JSON для передачи через API.]
    -views.py - вьюхи приложения
Frontend-
        - Фронтенд -
Qodex-
    -settings.py - конфигурация проекта
    -urls.py - урлы проекта
manage.py - сердце проекта


// API: //
Django_rest_framework - это библиотека, которая работает со стандартными моделями Django для создания гибкого и мощного API для проекта.
подробнее в документации к библиотеке(https://www.django-rest-framework.org/api-guide/generic-views/#listapiview)
Ссылки API: 
{ДОМЕН}/api/-
            -user
            -auto
            -trash_types
            -trash_cats
            -weight_types
Ссылки предоставляют API как в JSON формате, так и html формой.
Рекомендуемые библиотеки для связи rest_framework+JavaScript(React, Vue):
    1. Axios
    2. Ajax


// Расшифровка полей БД: //
    USER
(api-link: "api/user")
username - Логин пользователя
password - Пароль пользователя
is_active(true/false) - Проверка аутентификации пользователя
groups - Разграничение доступа пользователей
is_superuser(true/false) - Права модератора(сис.админ) пользователю
is_staff(true/false) - Права персонала пользователю
user_permissions - Иные права пользователю
