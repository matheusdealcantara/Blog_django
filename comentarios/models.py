from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from posts.models import Post


# Create your models here.
class Comentario(models.Model):
    nome_comentario = models.CharField(
        max_length=150, default=None, verbose_name='Nome')
    email_comentario = models.EmailField(default=None, verbose_name='Email')
    comentario = models.TextField(verbose_name='Comentario')
    post_comentario = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='Post')
    usuario_comentario = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, default=None,
        verbose_name='Usuario', blank=True, null=True)
    data_comentario = models.DateField(
        default=timezone.now, verbose_name='Data')
    publicado_comentario = models.BooleanField(
        default=False, verbose_name='Publicado')

    def __str__(self) -> str:
        return self.nome_comentario
