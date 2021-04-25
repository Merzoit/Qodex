# Qodex
<h1>Обозначения:<h1>
    <ul>
        <li>Core - ядро приложения.</li>
        <li>Frontend - UI приложения.</li>
        <li>Qodex - проект.</li>
    </ul>

<h1>Архитектура:</h1>
    <ul>
        <li>Core<br>
            admin.py - регистрация моделей<br>
            urls.py - урлы приложения Core<br>
            models.py - модели БД<br>
            serializers.py - сериализеры для формирования API для моделей<br><br>
            Сериализаторы(!)
            [Модели Django интуитивно представляют данные, хранящиеся в базе, но API должен передавать 
            информацию в менее сложной структуре. Хотя данные будут представлены как экземпляры классов 
            Model, их необходимо перевести в формат JSON для передачи через API.]<br>
            -views.py - вьюхи приложения</li><br>
        <li>Frontend<br>
             Фронтенд</li><br>
        <li>Qodex<br>
            settings.py - конфигурация проекта<br>
            urls.py - урлы проекта<br>
            manage.py - сердце проекта</li>
</ul>


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
