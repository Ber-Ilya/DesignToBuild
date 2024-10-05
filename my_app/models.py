from django.db import models

# Create your models here.
class SEO(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назнавание")
    description = models.CharField(max_length=200, verbose_name="Описание")
    keywords = models.CharField(max_length=200, verbose_name="Ключевые слова")

    def __str__(self):
        return self.title




class Menu(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название компании")
    logo = models.ImageField(upload_to="static/images", verbose_name="Логотип")
    description = models.CharField(max_length=200, verbose_name="Описание")
    link = models.URLField(verbose_name="Ссылка")

    def __str__(self):
        return self.title


class Block_UTP(models.Model):
    mini_UTP = models.CharField(max_length=200, verbose_name="текст 1")
    UTP = models.CharField(max_length=400, verbose_name="УТП")
    text_button = models.CharField(max_length=100, verbose_name="Текст кнопки")
    text_near_button = models.CharField(max_length=200, verbose_name="Текст возле кнопки" )
    image = models.ImageField(upload_to="static/images", verbose_name="Изображение УТП")

    def __str__(self):
        return self.mini_UTP



class Example(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/images/', blank=True, null=True )  # Поле для изображения


    def __str__(self):
        return self.title


class SRO(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    sro = models.ImageField(upload_to='media/images/SRO', blank=True, null=True )

    def __str__(self):
        return self.title


class Stati(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title