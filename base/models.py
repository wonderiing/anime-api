from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=55, null=False,blank=False, unique=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

class BaseModel(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False, unique=True)
    choices = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10')
    ]
    rating = models.CharField(max_length=2, choices=choices)
    image = models.ImageField(upload_to='anime_images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_favorite = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Base'
        verbose_name_plural = 'Bases'
        abstract = True