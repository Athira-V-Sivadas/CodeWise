from django.db import models

# Create your models here.
"""
Scheme: QuestionsDb
Fields:title,language,notes,difficulty_level,sample_input,sample_output,topic,published_date,is_active

"""
class QuestionsDb(models.Model):

    title=models.CharField(max_length=100)

    LANGUAGE_CHOICES=(
        ("python","Python"),     #1st val store in db,2nd val in dropdown
        ("java","Java"),
        ("javascript","JavaScript")
    )

    language=models.CharField(max_length=100,choices=LANGUAGE_CHOICES,default="python")

    DIFFICULTY_CHOICES=(
        ("easy","easy"),
        ("medium","medium"),
        ("hard","hard")
    )

    difficulty_level=models.CharField(max_length=100,choices=DIFFICULTY_CHOICES)

    topic = models.CharField(max_length =100)

    notes = models.TextField()

    sample_input = models.TextField()

    sample_output = models.TextField()

    published_date = models.DateTimeField(auto_now_add =True)

    is_active = models.BooleanField(default=True)