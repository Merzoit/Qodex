# Qodex
<h1>Обозначения:</h1>
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


<h1>API:</h1>
    <p>Django_rest_framework - это библиотека, которая работает со стандартными моделями Django для создания гибкого и мощного API для проекта.
    подробнее в <a href="https://www.django-rest-framework.org/api-guide/generic-views/#listapiview">документации</a> к библиотеке</p>
<h2>Ссылки API:</h2> 
    <ul>{ДОМЕН}/api/
        <li>user</li>
        <li>auto</li>
        <li>trash_types</li>
        <li>trash_cats</li>
        <li>weight_types</li></ul>
<p>Ссылки предоставляют API как в JSON формате, так и html формой.
Рекомендуемые библиотеки для связи rest_framework+JavaScript(React, Vue):</p>
    <ul>
        <li>Axios</li>
        <li>Ajax</li>
    </ul>


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
