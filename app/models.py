from django.db import models


class Tags(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class QuestionManager(models.Manager):
    def hot_questions(self):
        return self.order_by('-votes')

    def new_questions(self):
        return self.order_by('-birth_date')

    def questions_by_tag(self, title):
        return self.filter(tags__title=title)


class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    num_ans = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)
    votes = models.IntegerField()
    tags = models.ManyToManyField(Tags)
   # user = models.ForeignKey('User', on_delete=models.CASCADE, default=None)
    objects = QuestionManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    description = models.CharField(max_length=255)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, default=None)
 #   author = models.ForeignKey('User', on_delete=models.CASCADE, null=True, verbose_name='Автор')
    votes = models.IntegerField()

    def __str__(self):
        return self.question.title


