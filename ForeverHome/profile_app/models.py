from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError("Users must have an email adress.")
        if not username:
            raise ValueError("Users must have a username.")
        user = self.model(email =  self.normalize_email(email), username=username,)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(email =  self.normalize_email(email), username=username, password=password)
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

def get_profile_image_filepath(self, filename):
    return f'static/profile_app/profile_pictures/{self.pk}/{"profile_picture.png"}'

LOCATION_CHOICES = [
        ("FARGO", "Fargo"),
        ("MINOT", "Minot"),
        ("BISMARCK", "Bismarck"),
        ("DICKINSON", "Dickinson"),
        ("WILLISTON", "Williston"),
        ("DEVILS_LAKE", "Devils Lake"),
    ]

class Profile(AbstractBaseUser):
    userID = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name="email", unique=True, max_length = 60)  
    username = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(verbose_name = " Date Joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=500)
    profile_picture = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default="")
    location = models.CharField(max_length=30, choices=LOCATION_CHOICES, default="FARGO")
    liked_posts = models.ManyToManyField('pet_post_app.Post', blank=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_profile_image_filename(self):
        return str(self.profile_picture)[str(self.profile_picture).index(f'profile_pictures/{self.pk}/'):]

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
