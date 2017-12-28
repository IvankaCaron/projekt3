from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(phone=0)

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

    #pour faire le query que pour noPhone
    #from accounts.models import UserProfile
    #UserProfile.NoPhone.all()
    noPhone = UserProfileManager()

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