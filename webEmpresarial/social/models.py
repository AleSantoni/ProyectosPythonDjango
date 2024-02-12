from django.db import models

# Create your models here.
class Links(models.Model):
    link = models.SlugField( verbose_name="Nombre Clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Nombre", max_length=200)
    url= models.URLField(verbose_name="Emlace", max_length=200, null=True, blank=True)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name= 'Enlace'
        verbose_name_plural= 'Enlaces'
        ordering = ['created']
    
    def __str__(self):
        return self.name