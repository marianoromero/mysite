from django.db import models

class Question(models.Model):
    # ...
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # ...
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text