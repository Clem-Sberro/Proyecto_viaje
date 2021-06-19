from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Country(models.Model):

    country_name = models.CharField(primary_key=True, verbose_name="Nombre", max_length=200)
    capital = models.CharField(verbose_name="Capital", max_length=200)
    main_picture = models.ImageField(
        upload_to='Articles/', verbose_name="Foto de portada"
    )
    short_description = models.CharField(
        verbose_name='Descripción', null=False, max_length=300,
        default='Debes cambiarme eh!'
    )
    slug = models.SlugField(
       max_length = 250,
       default='default-slug'
    )

# class Place(models.Model):

#     fk_country = models.CharField(primary_key=True, verbose_name="Título", max_length=200)
#     capital = models.CharField(verbose_name="Título", max_length=200)
#     main_picture = models.ImageField(
#         upload_to='Articles/', verbose_name="Foto de portada"
#     )
#     short_description = models.CharField(
#         verbose_name='Descripción', null=False, max_length=300,
#         default='Debes cambiarme eh!'
#     )