from django.db import models

class Question(models.Model):
    """docstring for Question."""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
#models.model    def __init__(self, arg):
        #super(Question, models.model).__init__()
        #question_text = models.CharFiel
        #self.arg = arg
        #question_text = models.CharFiel


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
