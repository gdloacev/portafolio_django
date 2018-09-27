from django.db import models

# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Persona'
        verbose_name_plural = 'People'
        ordering=["lastname"]

    def __str__(self):
        return self.lastname + " " + self.firstname


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(verbose_name='Project Image', upload_to='projects')
    link = models.URLField(null=True, blank=True, verbose_name='Project URL')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title