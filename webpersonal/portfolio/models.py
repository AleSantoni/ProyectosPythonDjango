from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.CharField(max_length=250, verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to="projects")
    url = models.URLField(blank=True, null=True, verbose_name='URL')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['created']
    def __str__(self):
        return self.title
