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
            <p>Сериализаторы(!)
            [Модели Django интуитивно представляют данные, хранящиеся в базе, но API должен передавать 
            информацию в менее сложной структуре. Хотя данные будут представлены как экземпляры классов 
                Model, их необходимо перевести в формат JSON для передачи через API.]</p><br>
            views.py - вьюхи приложения</li><br>
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
    <p>{ДОМЕН}/api/</p>
    <ul>
        <li>user</li>
        <li>auto</li>
        <li>trash_types</li>
        <li>trash_cats</li>
        <li>weight_types</li>
        <li>qodex_user</li>
        <li>operators</li>
        <li>qodex_org</li>
        <li>user_roles</li>
        <li>qodex_achive</li>
        <li>cm_events</li>
        <li>oro_info</li>
        <li>regions</li>
        <li>rfid</li>
        <li>rfid_types</li>
    </ul>
     <p>Пример ссылки: <em>example.com/api/user</em></p>
<p>Ссылки предоставляют API как в JSON формате, так и html формой.
Рекомендуемые библиотеки для связи rest_framework+JavaScript(React, Vue):</p>
    <ul>
        <li>Axios</li>
        <li>Ajax</li>
    </ul>
<h2>Взаимодействие с Rest_framework(API)</h2>
<img src="../../blob/main/pic/readpic1.png"/>
<ol>
    <li>Выбор формата данных</li>
    <li>Конфиг БД</li>
    <li>Ссылка на API</li>
    <li>Данные объектов</li>
</ol>
<p>Для получение JSON - данных, переходим по кнопке под номер один рисунка.</p>
<p>Пример полученных данных:</p>
<img src="../../blob/main/pic/readpic2.png"/>


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

