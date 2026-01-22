from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return str(self.image)

class ImageQRCode(models.Model):
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return str(self.image)
class ImageIcons(models.Model):
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return str(self.image)
    