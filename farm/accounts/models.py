from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    pseudo =models.CharField(max_length=15, default='')
 #   birthDate = models.DateField(default=0)
    description = models.CharField(max_length=300, default='')
    favouritePlace = models.CharField(max_length=100, default='')
    favouritProduit = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

   # class Foo(models.Model):
    #    GENDER_CHOICES = (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    #  )
# gender = models.ChoiceField(max_length=1, choices=GENDER_CHOICES)