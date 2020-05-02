# kodland

В данном репозитории представлено решение тестового задания. Согласно ТЗ реализовано:
Проект на Django с одним приложением blog. Приложение содержит одну модель post.
Реализованы 3 view:
/post/ - страница просмотра первых 10 постов
/post/create/ - страница создания нового поста
/ - редирект на /post/

Пример установки приложения можно посмотреть на сервере kodland.svertilov.ru.

Порядок установки:
- создаем virtualenv для приложения на сервере;
- устанавливаем зависимости (django, pillow);
- клонируем код из репозитория на рабочий сервер;
- настраиваем settings.py в соответствии с рабочим окружением: указываем ALLOW_HOSTS, MEDIA_ROOT, STATIC_ROOT, SECRET_KEY, настройки базы данных, пример settings.delpoy.py;
- выполняем миграцию базы данных, для работы админки создаем суперпользователя;
- настраиваем вэб-сервер для работы с приложением.

На сервере kodland.svertilov.ru использован apache и mod_wsgi. Пример конфигурации представлен в репозитарии apache/kodland.conf.
