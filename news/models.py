from django.db import models


# Create your models here.
# News nomli jadval ustunlar (id, tittle, description, created)

class News(models.Model):
    title = models.CharField(max_length=200)
    """Для заголовок с ограничением 200 символ"""

    description = models.TextField()
    """Для текста без ограничении или же с ограничением"""

    created = models.DateTimeField()
    """Для определении даты публикации"""

    def __str__(self):
        return self.title


class Event(models.Model):
    epic_id = models.IntegerField()
    event = models.CharField(max_length=128)
    details = models.TextField(max_length=500)
    years_ago = models.IntegerField()

    def __str__(self):
        return f'{self.event}'


class EventVillian(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name}'


class Hero(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    cinema = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f'{self.first_name}'


