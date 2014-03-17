from django.db import models

# Create your models here.

class Entrada(models.Model):
	"""docstring for Entrada"""
	titulo=models.CharField(max_length=100)
	contenido=models.TextField()
	fecha=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.titulo
		#super(Entrada, self).__init__()
		#self.arg = arg
		