// Обозначения: //
Core - ядро приложения.
Frontend - UI приложения.
Qodex - приложение.



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