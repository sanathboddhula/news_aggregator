from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title
