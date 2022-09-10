from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20) #varchar(20)
    author = models.ForeignKey('auth.User',
                               on_delete=models.CASCADE)
    body = models.TextField()
    language = models.CharField(max_length=2,
                                default='EN',
                                choices=[
                                    ('EN', 'English'),
                                    ('RU', 'Russian'),
                                    ('KZ', 'Kazakh'),
                                    ('FR', 'French'),
                                    ('GR', 'Germanic'),
                                ])

    def __str__(self):
        return self.title
