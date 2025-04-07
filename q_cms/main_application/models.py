from django.db import models

# Create your models here.


class TestTable(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    adresse = models.CharField(max_length=255)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
    
class Property(models.Model):
    # Table des biens immobiliers
    name = models.CharField(max_length=255)
    address = models.TextField()
    price = models.FloatField()
    description = models.TextField()
    surface = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)