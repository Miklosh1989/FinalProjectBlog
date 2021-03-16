Web-приложение Blog

Getting Started

# Скачать проект к себе на компьютер
1.Check out from version Control ---> Git
  url =  "https://github.com/Miklosh1989/FinalProjectBlog"	
  
# Установить модуль Python MySQLdb с помощью pip
2.pip install mysqlclient

# Конфигурация БД
'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost'

# Создаем миграции с БД
3. python manage.py migrate

# Создаем админа
4. python manage.py createsuperuser # указываем имя, email, пароль

# Запускаем сервер
5. python manage.py runserver

6. Откроем  http://127.0.0.1:8000/admin/ и авторизируемся

7. Переходим на главную страницу http://127.0.0.1:8000/mainBlog/
