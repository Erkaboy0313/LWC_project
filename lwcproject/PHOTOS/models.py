from django.db import models

# Create your models here.

class Category(models.Model):
    Category = models.CharField(max_length=100)

    def __str__(self):
        return self.Category

class Photos(models.Model):

    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    Image = models.ImageField(null = True)
    Title = models.CharField(max_length=100)
    Description = models.TextField(max_length=1000)
    @property

    def imageURL(self):
        try:
            return self.Image.url
        except:
            return ''

    def __str__(self) :
        return self.Title