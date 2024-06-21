from django.db import models

# Create your models here.


class Product(models.Model):
    immagine = models.ImageField()
    nome = models.CharField(max_length=30)
    descrizione = models.CharField(max_length=200)
    prezzo = models.FloatField()

    def __str__(self):
        return self.nome
