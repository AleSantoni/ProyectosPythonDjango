from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name= 'Categoria'
        verbose_name_plural= 'Categorias'
        ordering = ['created'] 
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    published= models.DateTimeField( verbose_name='Fecha de Publicacion', default= now)
    image= models.ImageField(upload_to='posts', verbose_name='Imagen', null=True, blank=True)# lo pongo porque no voy a obligar a poner una imagen en la noticia
    author= models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    categories= models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_posts')
    created= models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated= models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
   
   
    
    class Meta:
        verbose_name= 'Entrada'
        verbose_name_plural= 'Entradas'
        ordering = ['created']  # Corregido
    
    def __str__(self):
        return self.title
   
