from django import forms

from pet_post_app.models import POST
class PostForm():
    picture_of_dog = forms.ImageField()
    name = forms.CharField()
    breed = forms.CharField()
    age = forms.IntegerField()
    personality = forms.ChoiceField()
    size = forms.ChoiceField()
    description = forms.CharField()
    good_with_pets = forms.BooleanField()
    good_with_kids = forms.BooleanField()
    problems_and_disabilities = forms.CharField()

    class Meta:
        model = POST
        fields('picture_of_dog', 'name', 'breed', 'age', 'personality', 
               'size', 'description','good_with_pets','good_with_kids','problems_and_disabilities')