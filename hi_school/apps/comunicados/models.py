from django.db import models

# Create your models here.
class Comunicados(models.Model):
	asunto = models.CharField(max_length=50)
	mensaje = models.CharField(max_length=50)
	fecha_envio = models.DateTimeField(auto_now_add=True, blank=True)
