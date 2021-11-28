from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage as storage
from PIL import Image


class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     image = models.ImageField(default='avatar.png', upload_to='profile_pics')

     def __str__(self):
         return f'{self.user.username} Profile'

     def save(self, *args, **kwargs):
         if not self.user.username:
             return

         super(Profile, self).save()
         if self.image:
             size = 200, 200
             image = Image.open(self.image)
             image.thumbnail(size, Image.ANTIALIAS)
             fh = storage.open(self.image.name, "w")
             format = 'png'
             image.save(fh, format)
             fh.close()

