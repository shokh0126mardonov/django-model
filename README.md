# django-model

django-models
qadamlar
project ni yaratdik: django-admin startproject core .
app ni yaratdik: django-admin startapp app
add ni settings ga qoshdik : core/settings.py -> 'INSTALLED_APPS += ['app.apps.AppConfig']`
postgresql ni sozladik:
.env ga DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME larni yozdik
core/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
    }
}
psql postgres shell ga kirib db yaratib oldik
app/models.py da model class yaratdik
sql structure ga ogirdik modellarni: python manage.py makemigrations
sql strukturadagi kodlarni postgresql da run qildik: python manage.py migrate
runserver: python manage.py runserver
models larni admin panelga qoshidik app/admin.py:
from .models import Task
admin.site.register(Task)
admin panel uchun super user yaratidik: python manage.py createsuperuser