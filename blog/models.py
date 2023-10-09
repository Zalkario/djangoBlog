from django.db import models

# Create your models here.


class Category(models.Model):
    """Модел(Таблица катег)
    """
    title = models.CharField(
        max_length= 255,
    )

class Post(models.Model):
    """Модел (таб катег)
    """
    category = models.ForeignKey(
        Category,
        on_delete= models.CASCADE
    )
    title = models.CharField(
        max_length= 255,
    )
    description = models.TextField(
        max_length=2000,
    )
    created_at = models.DateField(
        auto_now_add= True,
    )
    author = models.CharField(
        max_length=30,
    )