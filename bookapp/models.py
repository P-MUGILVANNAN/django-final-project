from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    published_date = models.DateField()
    page_count = models.IntegerField()
    genre = models.CharField(max_length=100)
    cover_image = models.CharField(max_length=200)
    language = models.CharField(max_length=100)

    class Meta:
        db_table = "books"