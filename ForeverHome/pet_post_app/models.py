from django.db import models

PERSONALITY_CHOICES = [
    ("COUCH_POTATOE", "Couch potatoe"),
    ("ENERGETIC", "Energetic"),
    ("SOCIABLE", "Sociable"),
    ("CUDDLY", "Cuddly"),
    ("PLAYFUL", "Playful"),
    ("PROTECTIVE", "Protective"),
    ]
SIZE_CHOICES = [
    ("SM", "Small"),
    ("MD", "Medium"),
    ("LG", "Large"),
]

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    picture_of_dog = models.ImageField(upload_to="pet_post_app/post_pictures", default="")
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    personality = models.CharField(max_length=40, choices= PERSONALITY_CHOICES, default="CALM")
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default="MD")
    description = models.CharField(max_length=500)
    profile_that_posted_pet = models.ForeignKey('profile_app.Profile', on_delete=models.CASCADE)
    good_with_pets = models.BooleanField()
    good_with_kids = models.BooleanField()
    problems_and_disabilities = models.CharField(max_length=500)