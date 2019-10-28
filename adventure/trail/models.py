from django.contrib.auth.models import User
from django.db import models

# Create your models here.

DIFICULTY = (
    (0, ' '),
    (1, 'Bardzo łatwa'),
    (2, 'Łatwa'),
    (3, 'Średnio trudna'),
    (4, 'Dla wytrwałych'),
    (5, 'Mega')
)
TYPE = (
    (1, 'pieszo'),
    (2, 'rowerem')
)


class Trail(models.Model):
    name = models.CharField(max_length=32)
    type_tour = models.IntegerField(choices=TYPE)
    difficulty = models.IntegerField(choices=DIFICULTY)
    distance = models.IntegerField(default=0)
    time_tour = models.PositiveIntegerField(default=0)
    description = models.TextField(default="Wstaw opis", null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="gallery", null=True, blank=True)
    add_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "trails"

    def __str__(self):
        return self.name


class Comments(models.Model):
    description = models.TextField(default="Wstaw swój komentarz")
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

